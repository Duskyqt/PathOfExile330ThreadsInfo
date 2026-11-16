# Solo 10-Thread Legion (2026-11-16)

## Setup

- **Maps:** 5, Legion only, at 10 Threads. 10 Threads needs the atlas passive that allows one
  league above the cap of 8.
- **Map base:** Dunes, tier 16 (area level 83), all with map affixes (item rarity +57% to +60%).
- **Atlas tree:** index 1, with the same passives as the 6/6/6 and 8/8/8 runs. With one Thread
  type slotted, the map-mod bonus from `map_mod_effect_+%_per_different_thread_type` is +5%.

## Maps

| Time | Extra spawns | Legion juice rolls | Juice mods |
|---|---|---|---|
| 01:33 | 4 | 2 | EternalConflict, SmallCrystals |
| 01:33 | 5 | 2 | MonstersRankHigher, SmallCrystals |
| 01:33 | 4 | 3 | AllChestsAreWarHoards, BothLegionsHaveGenerals, EternalConflict |
| 01:34 | 4 | 0 | none |
| 01:34 | 4 | 3 | BothLegionsHaveGenerals, MonstersRankHigher, SmallCrystals |

The juice counts leave out AdditionalLegion, which can't be told apart from Legion's own extra
spawns at 10 Threads (see below).

## What held

- **The stat set at 10 is 50 / 1400 / 16000,** the same as the earlier 10-Legion and 10-Abyss
  maps.
- **The 10-Thread passive's three stats were on every map:** `map_maximum_one_thread_slot` 1,
  `map_x_additional_free_threads_bypassing_maximum` 2 and `map_threads_convert_to_gold_chance_%`
  75.
- **Hidden monster life was +109%,** matching area level 83 as before.
- No stats appeared that only these maps had, apart from ordinary map affixes (elemental
  weakness, monsters can't be leeched from).

## Legion's extra spawns at 10

`map_legion_league_extra_spawns` read 4, 5, 4, 4 and 4. An earlier solo 10-Legion map read 4. The
5 may be 4 plus one AdditionalLegion roll, but with the amount varying at 6 and 8 that can't be
confirmed. `THREAD_BASE` marks 10 as varying, like 6 and 8. Before that, the analyzer counted 4 to 5
AdditionalLegion rolls per map.

| Legion Threads | Extra spawns seen |
|---|---|
| 3 | 2 (3 with AdditionalLegion) |
| 6 | 1, 2, 3, 4, 4, and 4 on a solo map |
| 8 | 3, 4, 3, 4, 3 |
| 10 | 4, 5, 4, 4, 4, and 4 on an earlier solo map |

## Juice drops at 10

| | Legion Threads | Legion juice rolls per map | Juice rolls for the whole map |
|---|---|---|---|
| Solo Legion | 10 | 2.0 | 2.0 |
| Legion in a three-league map | 8 | 3.4 | 10.2 |
| Legion in a three-league map | 6 | 1.8 | 7.6 |
| Legion in a three-league map | 3 | 1.6 | 5.8 |

- **Legion rolled less juice at 10 than at 8:** 2.0 against 3.4, with one map rolling none. Every
  map at 10 had 3 rolls or fewer, and the five Legion maps at 8 had 2 to 4.
- **InvertedLegion didn't roll at 10,** after 3 of 5 maps at 8. SmallCrystals fell from 5 of 5 to
  3 of 5. MonstersRankHigher held at 2 of 5.
- **No new juice mods.** InstantBreakout is still the only Legion juice mod never seen.
- The one 10-Abyss map from the [level test](levels.md) rolled 5 Abyss juice, so 10 Threads
  doesn't clearly cap juice per league. That's one map against five.

## What this means for choosing a setup

| Setup | League rarity | Tankiness | Juice rolls per map |
|---|---|---|---|
| Solo 10 | +160% for one league | +1400% | about 2 |
| 8/8/8 | +125% each for three leagues | +700% each | about 10 |

In this small test, Legion's own juice was lower at 10 Threads than at 8 (2.0 per map against
3.4), for slightly more rarity and twice the tankiness. The whole map also rolls about a fifth of
the juice of an 8/8/8 map, but most of that gap is the two empty slots. Five maps on each side,
all Legion, and neither count includes AdditionalLegion.
