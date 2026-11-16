# 6/6/6 run (2026-11-16)

## Setup

- **Maps:** the same 17 league combinations as the [3/3/3 run](results-333.md), each league at
  6 Threads. Together they cover all 45 league pairs again, so every map has a 3/3/3 twin.
- **Map base:** Dunes, but **mostly not tier 16**, on purpose, to see whether map level matters:
  - 1 map at area level 83 (Abyss / Betrayal / Breach), with normal map affixes;
  - 16 maps at area level 77–78. 15 of them had almost no map affixes (item rarity +5%, pack
    size +8%), and one (Breach / Incursion / Legion) had some (+40% rarity).
- **Atlas tree:** index 1 throughout, the tree with no league content. One new atlas passive was
  allocated before this run. It adds two stats to every map:
  - `map_mod_effect_+%_per_different_thread_type` = 5
  - `map_num_thread_types` = 3

  So these two are an atlas passive, not a Thread effect. Juice values stayed inside their
  single-roll ranges (research chest clusters read 14 and 16), so the 15% doesn't appear to
  scale juice mods.

## Maps

| Time | Area level | Leagues | Juice mods | Juice rolls | At 3/3/3 |
|---|---|---|---|---|---|
| 00:18 | 83 | Abyss / Betrayal / Breach | 7 | 9 | 8 |
| 00:23 | 77 | Abyss / Blight / Incursion | 9 | 9 | 6 |
| 00:28 | 78 | Abyss / Expedition / Ritual | 4 | 6 | 7 |
| 00:28 | 78 | Bestiary / Betrayal / Blight | 4 | 5 | 8 |
| 00:29 | 78 | Bestiary / Blight / Ultimatum | 6 | 6 | 5 |
| 00:29 | 78 | Bestiary / Breach / Ritual | 8 | 9 | 9 |
| 00:30 | 78 | Bestiary / Expedition / Incursion | 6 | 6 | 5 |
| 00:31 | 78 | Betrayal / Incursion / Ritual | 6 | 6 | 7 |
| 00:31 | 78 | Betrayal / Incursion / Ultimatum | 3 | 3 | 4 |
| 00:32 | 78 | Blight / Breach / Expedition | 11 | 11 | 6 |
| 00:33 | 78 | Blight / Expedition / Ultimatum | 10 | 10 | 6 |
| 00:34 | 77 | Breach / Ritual / Ultimatum | 4 | 6 | 3 |
| 00:36 | 78 | Abyss / Bestiary / Legion | 5 | 6 | 6 |
| 00:40 | 78 | Abyss / Legion / Ultimatum | 10 | 11 | 2 |
| 00:41 | 78 | Betrayal / Expedition / Legion | 9 | 9 | 6 |
| 00:42 | 78 | Blight / Legion / Ritual | 6 | 6 | 5 |
| 00:44 | 78 | Breach / Incursion / Legion | 11 | 11 | 6 |

## What held

- **The stat set at 6 is 20 / 210 / 7000** for every league in every map, at area level 77, 78
  and 83 alike. It doesn't depend on area level either.
- **What a league's Threads give on their own doesn't grow from 3 to 6,** except Legion's extra
  spawns (below). Blight still gets 1 extra blight and 20% longer paths, Breach
  a hive in about 60% of maps, and the rest only switch their content on.
- **No pair effects.** Every stat the analyzer flags as pair-only is a juice mod stat, a map
  affix, or map generation noise (terrain failures). Each combination now has exactly two maps,
  so anything that landed on both copies of a triple looks like a pair effect.

## What's new

### Juice grows with Thread count

| | 3/3/3 | 6/6/6 |
|---|---|---|
| Juice rolls per map | 5.8 | 7.6 |
| Different juice mods per map | 5.2 | 7.0 |
| Maps with more juice than their twin | | 10 of 17 (4 fewer, 3 equal) |

Average juice rolls per map, by league:

| League | 3 Threads | 6 Threads |
|---|---|---|
| Ultimatum | 1.0 | 2.6 |
| Expedition | 1.2 | 2.4 |
| Breach | 2.0 | 3.2 |
| Blight | 2.2 | 3.0 |
| Incursion | 2.4 | 3.2 |
| Abyss | 2.2 | 2.8 |
| Legion | 1.6 | 1.8 (AdditionalLegion can't be detected at 6, see below) |
| Bestiary | 2.8 | 2.6 |
| Betrayal | 2.0 | 1.8 |
| Ritual | 2.0 | 1.8 |

- **Ultimatum** rolled exactly one juice mod in all 5 maps at 3, and up to 5 at 6.
- **Abyss Mortars** rolled in 0 of 5 Abyss maps at 3 and in 5 of 5 at 6. It also rolled at Abyss
  1, 5, 8 and 10 in the [level test](levels.md), but not at 9.
- **Ten mods rolled at 6 that never rolled at 3:**
  - Ultimatum: CatalystOnly, Trialmaster, DoubleDown, Oversouls
  - Breach: GuaranteedFortress (3 maps), RareMonstersBreachMonsterMods
  - Legion: SmallCrystals (2 maps)
  - Expedition: RunicRares
  - Bestiary: RedBeastInvasion
  - Abyss: Consort (first seen at Abyss 10)
- **Repeat rolls kept showing up:** ExtraAbysses x2 and x3 and ExtraRedBeasts x2 three times.
  AdditionalUnstableBreaches also read x3 twice, but that's uncertain: the unstable breaches may
  come partly from the Threads (see
  [results-888.md](results-888.md#breach-hive-or-unstable-breaches)).

**Caveat: area level changed along with Thread count.** All 3/3/3 maps were level 83 and 16 of
the 17 6/6/6 maps were level 77–78. If higher-level maps rolled more juice, the 6/6/6 maps
should have rolled less, yet they rolled more, so Thread count is the likely cause. The one
6/6/6 map at level 83 rolled 9 against its twin's 8, which can't settle it alone. A few 6/6/6
maps at tier 16 repeating 3/3/3 combinations would.

### Juice doesn't need map affixes or a high map level

15 maps with almost no affixes, at level 77–78, rolled juice as usual. Juice values stayed
inside their normal ranges.

### Area level drives the hidden monster life stat

`map_hidden_monster_life_+%_final` is +109% at area level 83, +61% at 78 and +55% at 77,
whatever the Threads. So it's the map level's scaling, separate from the Threads' tankiness.

### Legion's extra spawns at 6 vary

`map_legion_league_extra_spawns` read 2, 3, 1, 4 and 4 across the five Legion maps at 6, with
no AdditionalLegion detected. At 3 it was always 2, or 3 when AdditionalLegion rolled. A solo
6-Legion map earlier read 4. One map read 1, below the 3-Thread value, so at 6 this isn't a
fixed amount. `THREAD_BASE` now marks it as varying, which means AdditionalLegion (+1) can't be
told apart at 6 Threads.

### Red Beast Invasion rolled

Abyss / Bestiary / Legion read 28 red beasts. That's one RedBeastInvasion (18–20) plus two
ExtraRedBeasts rolls (2–4 each). `analyze.py` now fits mods that share a stat together, taking
the fewest rolls that add up to the value.
