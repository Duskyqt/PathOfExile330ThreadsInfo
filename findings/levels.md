# Thread levels 1–10 (2026-11-15)

## Setup

Five maps, all Dunes at tier 16, on the atlas tree with no league content (tree index 1). The
three-league maps tested a different level on each league, which works because the Thread stat
set depends only on that league's own count (shown by the 3/3/3 run).

| Map | Split | Levels tested |
|---|---|---|
| A | Abyss 1 / Breach 4 / Ritual 2 | 1, 2, 4 |
| B | Abyss 5 / Breach 7 / Ritual 6 | 5, 6 (in a mix), 7 |
| C | Abyss 8 / Breach 3 / Ritual 1 | 8, plus 3 and 1 repeated as checks |
| D | Abyss 9, one league | 9 (needs the 10-Thread passive) |
| E | Abyss 10, one league, no Abyss passives | 10 |

## Results

The full table is in [threads.md](threads.md#the-thread-stat-set).

- **The repeat checks all matched:**
  - 1 Thread gave no stat set on both Abyss and Ritual.
  - 3 Breach gave 5 / 40 / 2500, the same as the 3/3/3 run.
  - 6 Ritual in a mix matched the earlier solo 6 Legion.
  - 10 Abyss without Abyss passives matched the earlier 10 Legion with Legion passives.
- **The values depend only on that league's own count:** not on which league, not on the other
  leagues in the map, and not on the atlas passives.
- **Juice may grow with Thread count.** One map per level isn't enough to say:
  - Abyss Mortars never rolled in 17 maps at 3 Threads, but rolled at Abyss 1, 5, 8 and 10.
  - Abyss Consort rolled for the first time at 10.
  - Breach at 7 read as 6 juice mods (AdditionalUnstableBreaches x4, GenesisSaplingTree,
    GuaranteedBoss). The x4 is uncertain: the unstable breaches may come partly from the Threads
    (see [results-888.md](results-888.md#breach-hive-or-unstable-breaches)).

## Choosing a level

This compares only the league item rarity stat against monster tankiness. It leaves out juice
mods and league content. The rarity stat affects only monsters from that league.

| Threads | Rarity | Tankiness | Rarity ÷ tankiness | Next Thread adds |
|---|---|---|---|---|
| 2 | +15% | +25% | 0.60 | +10 rarity for +15 tankiness |
| **3** | **+25%** | **+40%** | **0.63** | +13 for +30 |
| 4 | +38% | +70% | 0.54 | +14 for +50 |
| 5 | +52% | +120% | 0.43 | +18 for +90 |
| 6 | +70% | +210% | 0.33 | +23 for +170 |
| 7 | +93% | +380% | 0.24 | +32 for +320 |
| 8 | +125% | +700% | 0.18 | +20 for +350 (needs the passive) |
| 9 | +145% | +1050% | 0.14 | +15 for +350 |
| 10 | +160% | +1400% | 0.11 | — |

- **3 has the best ratio,** and 4 is the last cheap step. From 5 on, each extra Thread adds 5 to
  23 times more tankiness than rarity.
- **If kill speed is what limits you,** loot per minute goes roughly with
  (1 + rarity) ÷ (1 + tankiness). That number falls at every level, from 0.92 at 2 Threads to
  0.28 at 8.
- **If you overkill,** tankiness costs nothing until monsters start surviving a hit. Then take the
  highest level you still one-shot through.
- **Spreading Threads beats stacking them.** 3/3/3 gives three leagues +25% each at +40%
  tankiness. Solo 9 gives one league +145% at +1050%. Juice says the same: five
  [solo 10-Legion maps](results-solo10.md) rolled about 2 juice each, against about 10 for an
  8/8/8 map, and Legion's own juice was lower at 10 (2.0) than at 8 (3.4).
- **More Threads bring more juice, but not more league content.** The
  [6/6/6 run](results-666.md) rolled 7.6 juice per map against 5.8 at 3/3/3 over the same 17
  combinations, and ten juice mods first appeared at 6. What each league's Threads give on their
  own stayed the same from 3 to 6. Legion's extra spawns varied between 1 and 4 at 6. So 6 may pay
  better than rarity alone suggests. Fourteen [8/8/8 maps](results-888.md) rolled 10.2 juice per
  map, and eight juice mods only appeared at 8.
- **Slot three leagues, not two.** Juice is decided per league: two-league 8/8 maps rolled 6.6
  juice, the same per league as three-league maps. A third league adds its juice and its rarity,
  at the cost of one more group of tankier monsters. A tier-11 map rolled as much juice as the tier
  16s, so the gain comes from the Threads, not the map tier.

## Area level

The Thread stat set is the same at area level 77, 78 and 83. Area level sets
`map_hidden_monster_life_+%_final` instead: +109% at 83, +61% at 78, +55% at 77. That's the map's
own scaling, applied on top of the Threads' tankiness.
