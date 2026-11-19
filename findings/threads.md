# Threads

## In the game data

- Threads are items, `Metadata/Items/Threads/Thread<League>`. There are 10 types: Abyss,
  Bestiary, Betrayal, Blight, Breach, Expedition, Incursion, Legion, Ritual and Ultimatum.
- They're slotted on the Atlas screen, in the Left, Centre and Right slots of
  `AtlasThreadsLayout`, not in the map device.
- They sit in player inventory id 165.
- The items carry no mods.
- **Scarabs are gone from the game in 3.30; Threads replaced them.** The `Scarab*` rows are
  still in Mods.dat, but nothing can put them on a map. The map stat `map_<league>_scarab_count`
  now holds that league's Thread count.
- `AtlasThreadTypes.dat` gives each type at most one base stat. Abyss has
  `map_spawn_abysses = 1` and Breach has none.
- All 100 rows of `AtlasThreadTiers.dat` have empty effect arrays on the client. **The server
  works out what Threads do and writes the result straight into the map's stats.** Nothing in
  Mods.dat accounts for it.

## Caps

- At most 8 Threads per league and at most 3 leagues at once, so 24 is the most a map can have
  (8/8/8).
- An atlas passive allows 10 Threads, but only when a single league is slotted. With 10 in, it
  puts three stats on the map. They come from the passive, not from Threads, even though their
  names mention Threads:

  | Stat | Value |
  |---|---|
  | `map_maximum_one_thread_slot` | 1 |
  | `map_x_additional_free_threads_bypassing_maximum` | 2 |
  | `map_threads_convert_to_gold_chance_%` | 75 |
- `map_total_thread_count` holds the total across all leagues.

## The Thread stat set

For each league that has Threads slotted, the map gets three stats that only Threads produce.
They're Stats.dat rows 23344–23374, and no Mods.dat row grants them:

```
map_<league>_monster_damage_+%
map_<league>_monster_difficulty_tankiness_+%
map_<league>_monster_from_league_item_rarity_+%_permyriad
```

The values depend only on how many Threads that league has. They don't depend on which league
it is, which other leagues share the map, or the atlas passives.

**The 2026-11-18 patch changed every value below.** The new table is in
[results-patch-1118.md](results-patch-1118.md#the-new-stat-set). What follows is the pre-patch
curve, measured 2026-11-15:

| Threads of the league | Damage | Tankiness | Rarity (permyriad) | Source |
|---|---|---|---|---|
| 1 | — | — | — | none of the three stats appear (Abyss and Ritual, 1 map each) |
| 2 | +0% | +25% | 1500 | Ritual; the damage stat is present with value 0 |
| 3 | +5% | +40% | 2500 | 52 slots across 18 maps, all 10 leagues |
| 4 | +10% | +70% | 3800 | Breach |
| 5 | +15% | +120% | 5200 | Abyss |
| 6 | +20% | +210% | 7000 | 52 slots across 18 maps (the 6/6/6 run and Ritual in a mix), and earlier solo Legion |
| 7 | +28% | +380% | 9300 | Breach |
| 8 | +40% | +700% | 12500 | Abyss, 42 slots across fourteen 8/8/8 maps, and 10 across five Breach / Ritual 8/8 maps |
| 9 | +45% | +1050% | 14500 | solo Abyss, with the 10-Thread passive |
| 10 | +50% | +1400% | 16000 | solo Abyss without Abyss passives, earlier solo Legion with Legion passives, and five solo Legion maps |

- **Up to 8 Threads,** the cost rises faster than the reward:
  - damage goes up by 5 per Thread to 6, then by 8 and 12;
  - tankiness roughly doubles from 4 to 8 with each Thread;
  - rarity rises more slowly.
- **Above the cap (9 and 10)** each step is smaller:
  - damage +5, tankiness +350 and rarity +2000 or +1500 per Thread;
  - 8 is where tankiness jumps the most.
- **1 Thread** puts only the presence stats on the map (`map_<league>_scarab_count` 1 plus the
  league's spawn stat), with no stat set.
- `map_hidden_monster_damage_+%_final` 15 appears in every logged map, including maps without
  Threads, so it isn't a Thread stat.
- `map_hidden_monster_life_+%_final` follows the area level, not the Threads: +109% at 83, +98%
  at 82, +61% at 78, +55% at 77. The stat set is the same at every level.
- **Breach's Threads give a hive or unstable breaches,** never both (the two are mutually
  exclusive in the game). The hive came up in about 60% of maps at 3 and 6, and in all 5 at 8.

This stat set is the reliable way to tell which leagues have Threads in a map. `analyze.py`
reads it. `map_<league>_league_extra_spawns` is a weaker sign:
it doesn't prove Threads, because juice mods can add to it too. Its Thread share is 2 at 3 Legion
Threads but varies from 1 to 4 at 6, from 3 to 4 at 8 and from 4 to 5 at 10.

## Other hidden mods

- Mods.dat domain 44 holds 7 hidden mods for individual Legion monoliths (`LegionMonolith*`).
