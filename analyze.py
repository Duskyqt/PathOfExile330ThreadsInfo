"""Inference over the map log: Thread mixes, juice mods and pair coverage.

usage:  python -I analyze.py [--log PATH] [--juice PATH] [--suggest N]

Reads maplog.jsonl (one record per map-state version, written by the map logger)
and juice-mods.json (the RandomJuiceMod definitions exported from Mods.dat). Both default to data/
next to this script.
Only each map's last version is analysed, and only maps carrying map_tier.

Sections:
  maps         each map's area level, atlas tree index, Thread mix (per-league count) and juice mods
  stat set     the hidden per-league Thread stats (damage, tankiness, rarity) by that league's count
  thread-only  per league and count, stats only that league's Threads bring (after juice is removed)
  juice        per league: how often each juice mod rolled, out of the maps that league was in
  pairs        which of the 45 league pairs have shared a map, and triples that would fill the gaps
  pair-only    stats seen only when two specific leagues share a map (mixing-mechanic candidates)

Every run also rewrites permutations.md next to the log: the running list of which league
combinations have been run at each even split and which are left. Maps hold three leagues. Pair
coverage is done for both 3/3/3 and 6/6/6 (GOAL_SPLIT; its goal section reads "Done" once met).

Juice detection is by stat signature, after subtracting what the Threads give on their own
(THREAD_BASE). A mod matches when every stat it grants is present and some roll count k fits all
of them: k*min <= value <= k*max. Juice mods appear able to roll more than once with their stats
adding up, so k > 1 is shown as xk. Single-stat mods that share a stat (Bestiary's two red-beast
mods) are fitted together, taking the fewest total rolls that add up to the value. A "partial" hit
means the stats are present but nothing fits, which is what another source stacking on the same
stat looks like; partials are listed, never counted.
Findings so far are in findings/.
"""
import argparse
import functools
import itertools
import json
import os
import random
from collections import Counter, defaultdict

# The data/ snapshot in this repo. Pass --log/--juice to read other files instead.
CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
LEAGUES = ["abyss", "bestiary", "betrayal", "blight", "breach", "expedition", "incursion", "legion", "ritual", "ultimatum"]
SET_STATS = {
    "damage": "map_{}_monster_damage_+%",
    "tankiness": "map_{}_monster_difficulty_tankiness_+%",
    "rarity": "map_{}_monster_from_league_item_rarity_+%_permyriad",
}


def load_maps(path, since=None, until=None):
    """Each map's last version, for maps carrying map_tier. since/until bound the record time
    (ISO, compared as text, e.g. 2026-11-18T17:15): records carry no game version, so a patch is
    told apart by time alone."""
    last = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                record = json.loads(line)
                if (since and record["time"] < since) or (until and record["time"] >= until):
                    continue
                last[record["areaHash"]] = record
    return [r for r in last.values() if "map_tier" in r["stats"]]


def mix(stats):
    """League -> Thread count, from map_<league>_scarab_count (the game's own per-league tally)."""
    return {lg: stats["map_%s_scarab_count" % lg] for lg in LEAGUES if stats.get("map_%s_scarab_count" % lg)}


# What a league's Threads put on a map by themselves, by Thread count, wherever a juice mod uses the
# same stat. It is subtracted before juice matching. Without it, Legion's own 2 extra spawns at 3
# Threads would hide every roll of AdditionalLegion (+1). None means the amount varies from map to
# map, so juice mods on that stat can't be told apart and are skipped. Measured: 3 from the 3/3/3
# run; 6 read 1, 2, 3, 4 and 4 in the 6/6/6 run (and 4 on a solo map). Extend this as the
# "Thread-only stats" section shows new counts.
THREAD_BASE = {
    "legion": {
        2: {"map_legion_league_extra_spawns": None},  # read 2 and 1 on two solo maps
        3: {"map_legion_league_extra_spawns": 2},
        6: {"map_legion_league_extra_spawns": None},
        8: {"map_legion_league_extra_spawns": None},  # read 3, 4, 3, 4, 3 across five 8/8/8 maps
        10: {"map_legion_league_extra_spawns": None},  # read 4, 5, 4, 4, 4 across five solo maps
    },
}

# Juice mods appear able to roll more than once on one map, and their stats then add up
# (33 research chest clusters is two rolls of 14-18). Most rolls tried per mod.
MAX_ROLLS = 5


def base_for(mx):
    """Stat -> amount the map's Threads supply on their own, from THREAD_BASE (None: varies)."""
    base = Counter()
    for lg, n in mx.items():
        for stat, value in THREAD_BASE.get(lg, {}).get(n, {}).items():
            if value is None or base[stat] is None:
                base[stat] = None
            else:
                base[stat] += value
    return base


def rolls(mod, stats, base):
    """How many times `mod` rolled: the smallest k with k*min <= value <= k*max for every stat,
    after removing the Threads' own share. 0 when it didn't roll, None when its stats are present
    but no k fits (another source on the same stat). Ranges can be negative (FreeTowers is -100)."""
    values = [stats[s["id"]] - base[s["id"]] for s in mod["stats"]]
    if all(v == 0 for v in values):
        return 0
    for k in range(1, MAX_ROLLS + 1):
        if all(k * s["min"] <= v <= k * s["max"] for s, v in zip(mod["stats"], values)):
            return k
    return None


def split_rolls(mods, value):
    """Roll counts for single-stat mods that share one stat, whose rolls all add into it: the fewest
    total rolls with sum(k*min) <= value <= sum(k*max). Bestiary's red-beast mods are the case:
    28 is one RedBeastInvasion (18-20) plus two ExtraRedBeasts (2-4 each). None when nothing fits."""
    if value == 0:
        return [0] * len(mods)
    best = None
    for ks in itertools.product(range(MAX_ROLLS + 1), repeat=len(mods)):
        lo = sum(k * m["stats"][0]["min"] for k, m in zip(ks, mods))
        hi = sum(k * m["stats"][0]["max"] for k, m in zip(ks, mods))
        if lo <= value <= hi and (best is None or sum(ks) < sum(best)):
            best = ks
    return best


def juice_hits(stats, juice, base):
    """(mod, rolls) for every mod that fits, and the mods that are present but don't fit."""
    full, partial = [], []
    single = defaultdict(list)  # stat -> the single-stat mods using it, fitted together
    for mod in juice:
        if all(s["id"] in stats for s in mod["stats"]):
            if any(base.get(s["id"], 0) is None for s in mod["stats"]):
                continue  # the Threads' own share of this stat varies, so a roll can't be seen
            if len(mod["stats"]) == 1:
                single[mod["stats"][0]["id"]].append(mod)
                continue
            k = rolls(mod, stats, base)
            if k:
                full.append((mod, k))
            elif k is None:
                partial.append(mod)
    for stat, mods in single.items():
        ks = split_rolls(mods, stats[stat] - base[stat])
        if ks is None:
            partial.extend(mods)
        else:
            full.extend((mod, k) for mod, k in zip(mods, ks) if k)
    return full, partial


def short(mod_id):
    return mod_id.replace("RandomJuiceMod", "")


# (leagues per map, Threads per league) sections always shown, even before any run. Maps always
# hold three leagues; other sizes still get a section of their own if one is ever logged.
PLANNED_SPLITS = [(3, 3), (3, 6), (3, 8)]

# The current goal: every pair of leagues has shared at least one 6/6/6 map. Each map covers three
# pairs, so the 45 pairs take at least 15 maps. 3/3/3 pair coverage finished on 2026-11-15.
GOAL_SPLIT = 6


@functools.lru_cache(maxsize=None)
def _cover_plan(missing, tries):
    rng = random.Random(0)
    triples = list(itertools.combinations(LEAGUES, 3))
    gain = lambda t, gaps: sum(p in gaps for p in itertools.combinations(t, 2))
    best = None
    for _ in range(tries):
        gaps, picks = set(missing), []
        while gaps:
            top = max(gain(t, gaps) for t in triples)
            pick = rng.choice([t for t in triples if gain(t, gaps) == top])
            picks.append((pick, top))
            gaps -= set(itertools.combinations(pick, 2))
        if best is None or len(picks) < len(best):
            best = picks
    return sorted(best or [])


def cover_plan(missing, tries=1500):
    """A short list of triples covering every missing pair: randomised greedy, best of `tries`.

    Seeded, so the same log always gives the same suggestion; cached, since the console report
    and permutations.md both ask for it.
    """
    return _cover_plan(tuple(missing), tries)


def goal_pairs(rows):
    """Pairs covered by maps at the goal split, and the pairs still missing."""
    covered = Counter()
    for _, mx, _, _ in rows:
        if len(mx) == 3 and set(mx.values()) == {GOAL_SPLIT}:
            for pair in itertools.combinations(sorted(mx), 2):
                covered[pair] += 1
    missing = [p for p in itertools.combinations(LEAGUES, 2) if not covered[p]]
    return covered, missing


def write_permutations(rows, path):
    """The running list: per even split, every league combination marked done (with dates) or left.

    A map counts toward a split when it ran exactly that many leagues at the same count each, so a
    Legion 3 + Ritual 3 map is the pair at 3/3 and nothing else. Combinations are unordered.
    """
    done = defaultdict(lambda: defaultdict(list))  # (size, count) -> combination -> dates
    other = []
    for m, mx, _, _ in rows:
        counts = set(mx.values())
        if mx and len(counts) == 1:
            done[(len(mx), counts.pop())][tuple(sorted(mx))].append(m["time"][:10])
        elif mx:
            other.append((m["time"][:10], " / ".join("%s %d" % (lg, n) for lg, n in sorted(mx.items()))))

    title = lambda lg: lg.capitalize()
    kind = {1: "Single league", 2: "Pairs", 3: "Triples"}
    lines = [
        "# Thread permutations",
        "",
        "Generated by `analyze.py` from `maplog.jsonl` on every run; don't edit by hand.",
        "A combination counts as done at a split when a logged map ran exactly those leagues at that count each.",
        "",
    ]

    split3 = "/".join([str(GOAL_SPLIT)] * 3)
    covered, missing = goal_pairs(rows)
    lines.append("## Goal: every pair in a %s map: %d of 45 covered" % (split3, 45 - len(missing)))
    lines.append("")
    if missing:
        plan = cover_plan(missing)
        lines.append("Fastest way to finish, %d maps. +N is how many still-missing pairs that map covers;" % len(plan))
        lines.append("below +3, it repeats a pair already covered, which can't be avoided at the end.")
        lines.append("")
        for triple, gained in plan:
            lines.append("- [ ] %s  (+%d)" % (" / ".join(map(title, triple)), gained))
        lines.append("")
        lines.append("The plan is recomputed every run, so playing off-plan is fine.")
        lines.append("")
        lines.append("Pairs still missing (%d):" % len(missing))
        lines.append("")
        for first, group in itertools.groupby(missing, key=lambda p: p[0]):
            lines.append("- %s with: %s" % (title(first), ", ".join(title(p[1]) for p in group)))
        lines.append("")
    else:
        lines.append("Done. Next: fill in the remaining %s triples below." % split3)
        lines.append("")
    for size, split in sorted(set(PLANNED_SPLITS) | set(done)):
        combos = list(itertools.combinations(LEAGUES, size))
        ran = done[(size, split)]
        label = "/".join([str(split)] * size)
        lines.append("## %s %s: %d of %d done" % (kind.get(size, "%d leagues" % size), label, len(ran), len(combos)))
        lines.append("")
        if ran:
            lines.append("Done:")
            lines.append("")
            for combo in combos:
                if combo in ran:
                    dates = ran[combo]
                    runs = "" if len(dates) == 1 else " (x%d)" % len(dates)
                    lines.append("- [x] %s, %s%s" % (" / ".join(map(title, combo)), dates[-1], runs))
            lines.append("")
        left = [c for c in combos if c not in ran]
        if left:
            lines.append("Left (%d):" % len(left))
            lines.append("")
            if size == 1:
                lines.append("- " + ", ".join(title(c[0]) for c in left))
            else:
                for first, group in itertools.groupby(left, key=lambda c: c[0]):
                    lines.append("- %s with: %s" % (title(first), ", ".join(" / ".join(map(title, c[1:])) for c in group)))
            lines.append("")
    if other:
        lines.append("## Other splits")
        lines.append("")
        for date, split in other:
            lines.append("- %s, %s" % (split, date))
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default=os.path.join(CONFIG, "maplog.jsonl"))
    ap.add_argument("--juice", default=os.path.join(CONFIG, "juice-mods.json"))
    ap.add_argument("--suggest", type=int, default=5, help="how many gap-filling triples to suggest")
    ap.add_argument("--since", help="only records at or after this time, e.g. 2026-11-18T17:15")
    ap.add_argument("--until", help="only records before this time")
    args = ap.parse_args()

    maps = load_maps(args.log, args.since, args.until)
    with open(args.juice, encoding="utf-8") as f:
        juice = json.load(f)["mods"]
    juice_by_league = defaultdict(list)
    for mod in juice:
        juice_by_league[mod["league"].lower()].append(mod["id"])

    rows = []
    for m in maps:
        mx = mix(m["stats"])
        full, partial = juice_hits(m["stats"], juice, base_for(mx))
        rows.append((m, mx, full, partial))

    print("== maps: %d" % len(rows))
    for m, mx, full, partial in rows:
        split = " / ".join("%s %d" % (lg, n) for lg, n in sorted(mx.items()))
        tree = m["stats"].get("map_active_atlas_passive_tree_index")
        print("  %s  %-20s lvl %s  %s  tree %s  [%s]" % (m["time"], m["areaName"][:20], m.get("areaLevel"), m["areaHash"], tree, split or "no threads"))
        for mod, k in sorted(full, key=lambda j: j[0]["id"]):
            print("      juice %s  %s" % ("x%d" % k if k > 1 else "  ", short(mod["id"])))
        for mod in sorted(partial, key=lambda j: j["id"]):
            print("      partial  %s" % short(mod["id"]))

    print("\n== stat set by that league's own Thread count (damage / tankiness / rarity permyriad)")
    by_count = defaultdict(Counter)
    for m, mx, _, _ in rows:
        for lg, n in mx.items():
            values = tuple(m["stats"].get(t.format(lg)) for t in SET_STATS.values())
            by_count[(n, len(mx))][values] += 1
    for (n, leagues), seen in sorted(by_count.items()):
        for values, k in seen.items():
            print("  %2d threads, %d-league mix: %s  (x%d)" % (n, leagues, " / ".join(map(str, values)), k))

    print("\n== Thread-only stats per league and Thread count")
    print("  Stats never seen in a map without that league, after removing what matched juice mods")
    print("  explain. 'always' = in every such map; 'sometimes' = in at least half. Map affixes that")
    print("  keep landing on one league's maps and that league's own atlas passives show up here too,")
    print("  so check the tree index on the maps listed above.")
    residual = []
    for m, mx, full, _ in rows:
        base = base_for(mx)
        claimed = {s["id"] for mod, _ in full for s in mod["stats"]} - set(base)
        residual.append({k: v for k, v in m["stats"].items() if k not in claimed})
    skip = {t.format(lg) for t in SET_STATS.values() for lg in LEAGUES} | {"map_%s_scarab_count" % lg for lg in LEAGUES}
    for lg in LEAGUES:
        outside = set().union(*[set(m["stats"]) for m, mx, _, _ in rows if lg not in mx])
        for n in sorted({mx[lg] for _, mx, _, _ in rows if lg in mx}):
            own = [res for res, (_, mx, _, _) in zip(residual, rows) if mx.get(lg) == n]
            stats = defaultdict(list)
            for res in own:
                for k, v in res.items():
                    if k not in outside and k not in skip:
                        stats[k].append(v)
            note = "  (one map: its affixes show as 'always' too)" if len(own) == 1 else ""
            print("  %-10s %d threads, %d maps%s" % (lg, n, len(own), note))
            for k, vals in sorted(stats.items(), key=lambda p: (len(p[1]) < len(own), p[0])):
                if len(vals) < min(len(own), max(2, len(own) / 2)):
                    continue  # one-off map affixes that happened to land on this league's maps
                tag = "always   " if len(vals) == len(own) else "sometimes"
                print("      %s %-60s %s  (%d/%d)" % (tag, k, "/".join(map(str, sorted(set(vals)))), len(vals), len(own)))

    print("\n== juice frequency per league (maps rolled in / maps the league was in; xN = total rolls)")
    for lg in LEAGUES:
        present = [(m, full) for m, mx, full, _ in rows if lg in mx]
        if not present:
            continue
        maps_in, total = Counter(), Counter()
        for _, full in present:
            for mod, k in full:
                maps_in[mod["id"]] += 1
                total[mod["id"]] += k
        per_map = [sum(k for mod, k in full if mod["league"].lower() == lg) for _, full in present]
        print("  %-10s in %d maps, %s juice rolls per map" % (lg, len(present), "/".join(map(str, per_map))))
        for mod_id in juice_by_league[lg]:
            extra = "  x%d" % total[mod_id] if total[mod_id] > maps_in[mod_id] else ""
            print("      %d/%d  %s%s" % (maps_in[mod_id], len(present), short(mod_id), extra))

    print("\n== pair coverage")
    pairs = Counter()
    for _, mx, _, _ in rows:
        for pair in itertools.combinations(sorted(mx), 2):
            pairs[pair] += 1
    all_pairs = list(itertools.combinations(LEAGUES, 2))
    missing = [p for p in all_pairs if pairs[p] == 0]
    print("  covered %d/%d pairs" % (len(all_pairs) - len(missing), len(all_pairs)))
    for pair, k in sorted(pairs.items()):
        print("      x%d  %s + %s" % (k, pair[0], pair[1]))

    _, goal_missing = goal_pairs(rows)
    if goal_missing:
        plan = cover_plan(goal_missing)
        print("  goal (every pair in a %s map): %d missing; finishing plan, %d maps:" % ("/".join([str(GOAL_SPLIT)] * 3), len(goal_missing), len(plan)))
        for triple, gained in plan[: args.suggest]:
            print("      %s  (+%d new pairs)" % (" / ".join(triple), gained))
        if len(plan) > args.suggest:
            print("      ... %d more in permutations.md" % (len(plan) - args.suggest))

    print("\n== pair-only stats (seen only when both leagues share a map)")
    print("  A stat qualifies when every map with it holds both leagues, and maps holding either")
    print("  league without the other exist and lack it. Few maps make this noisy; re-check as data grows.")
    found = False
    stat_maps = defaultdict(list)
    for m, mx, _, _ in rows:
        for stat in m["stats"]:
            stat_maps[stat].append(set(mx))
    for stat, mixes in sorted(stat_maps.items()):
        if len(mixes) < 2 or len(mixes) == len(rows):
            continue
        common = set.intersection(*mixes)
        for a, b in itertools.combinations(sorted(common), 2):
            only_a = [mx for _, mx, _, _ in rows if a in mx and b not in mx]
            only_b = [mx for _, mx, _, _ in rows if b in mx and a not in mx]
            if only_a and only_b:
                found = True
                print("  %-70s %s + %s  (in %d maps)" % (stat, a, b, len(mixes)))
    if not found:
        print("  none yet")

    perm_path = os.path.join(os.path.dirname(os.path.abspath(args.log)), "permutations.md")
    write_permutations(rows, perm_path)
    print("\n== permutations list written to %s" % perm_path)


if __name__ == "__main__":
    main()
