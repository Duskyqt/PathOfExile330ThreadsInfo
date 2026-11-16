# Research notes

The raw findings behind the [write-up](../README.md): what Path of Exile 3.30's Threads do to a
map. Threads replaced scarabs in 3.30, and their effects are hidden from the in-game UI. We read
them from game memory while running maps with known Thread setups.

## Findings

| File | Contents |
|---|---|
| [threads.md](threads.md) | What Threads are in the game data, the caps, and the stat set for every level from 1 to 10 |
| [levels.md](levels.md) | The level 1–10 test, and which level gives the most rarity for the least tankiness |
| [juice-mods.md](juice-mods.md) | The 70 hidden "juice" modifiers: how to detect them, how often each rolled, and evidence that one can roll more than once |
| [results-333.md](results-333.md) | The 3/3/3 run: 17 maps covering all 45 league pairs, and what each league's Threads give on their own |
| [results-666.md](results-666.md) | The 6/6/6 run: the same 17 combinations at 6 Threads, mostly at area level 77–78. More juice and new juice mods; the extra league content comes through juice |
| [results-888.md](results-888.md) | Fourteen 8/8/8 maps in three league combinations plus five two-league Breach / Ritual 8/8 maps. Juice keeps rising, eight juice mods first seen at 8, juice is per league, and Breach's hive-or-unstable-breaches branch |
| [results-solo10.md](results-solo10.md) | Five solo 10-Thread Legion maps. About 2 juice per map, less than Legion gets at 8, for twice the tankiness |
| [plan-666.md](plan-666.md) | The plan for the 6/6/6 run, as written before it |

Short version:
- **The stat set.** Each slotted league adds monster damage, monster tankiness and league item
  rarity. The values depend only on that league's own Thread count.
- **Juice mods.** On top of that, each map rolls up to 12 juice mods, picked by the server. More
  Threads mean more juice: 5.8 rolls per map at 3/3/3, 7.6 at 6/6/6 and 10.2 at 8/8/8. Ten mods
  were first seen at 6 and eight more at 8, though with about 5 maps per league per Thread count
  that may be rarity rather than a hard unlock. Juice is decided per league, so a two-league map gets
  about a third less. Map tier doesn't change the juice count. In a small solo 10-Legion test,
  Legion rolled less juice at 10 Threads than at 8 (2.0 per map against 3.4).
- **Mixing.** Which leagues share a map has shown no effect in two full pair-coverage runs.
- **Area level** doesn't change the Thread stats. It sets the hidden monster life bonus instead.

## Data

- [`data/maplog.jsonl`](../data/maplog.jsonl): every logged map, one line per version of the map's stats.
  - Keyed by area hash.
  - A new version is logged when the stats change mid-map, for example from altars or monoliths.
  - Snapshot from 2026-11-16, after the 6/6/6 run, 14 maps at 8/8/8, 5 at Breach / Ritual 8/8
    and 5 solo 10-Legion maps.
- [`data/juice-mods.json`](../data/juice-mods.json): the 70 `RandomJuiceMod*` rows from Mods.dat, with their stats and
  roll ranges.

## Analyzer

```
python -I analyze.py
python -I analyze.py --log path\to\maplog.jsonl
```

Run it from the repo root. With no arguments it reads the snapshot in `data/`. Pass `--log` to read a different
map log. Python 3.8 or later, standard library only.

It prints:
- each map's area level, Thread setup, atlas tree and juice mods, with repeat rolls shown as `xN`;
- the stat set by Thread count;
- the stats each league's Threads give on their own, by count;
- how often each juice mod rolled, per league;
- which league pairs have been covered;
- stats that only appear when two particular leagues share a map.

It also writes `permutations.md` next to the log: the running list of which league
combinations have been done at each split and which are left.

When a league's Threads add to a stat a juice mod also uses (Legion's extra spawns, for example),
put that amount in `THREAD_BASE` at the top of [`analyze.py`](../analyze.py). Otherwise those juice rolls get
miscounted.
