# 8/8/8 maps (2026-11-16)

## Setup

Fourteen maps in three sets, all Dunes, on atlas tree index 1 with the same atlas passive as the
[6/6/6 run](results-666.md):

| Set | Maps | Map types |
|---|---|---|
| Bestiary / Incursion / Ultimatum | 4 | Tier 16 (area level 83), two with map affixes and two without |
| Betrayal / Expedition / Incursion | 5 | Two tier 16 (one with affixes, one without), one tier 11 (area level 78), and two special maps at level 83 with citadel and influence stats |
| Abyss / Blight / Legion | 5 | Tier 16 (area level 83), four without affixes and one with |

None of these combinations was run at 3 or 6 Threads, so there's no like-for-like twin. The
comparisons below use the league averages from those runs.

## Maps

| Time | Leagues | Map | Juice mods | Juice rolls | Per league |
|---|---|---|---|---|---|
| 00:59 | Bestiary / Incursion / Ultimatum | T16, no affixes | 9 | 10 | 4 / 2 / 3 |
| 01:00 | Bestiary / Incursion / Ultimatum | T16 | 8 | 8 | 2 / 3 / 3 |
| 01:00 | Bestiary / Incursion / Ultimatum | T16 | 10 | 11 | 4 / 3 / 4 |
| 01:01 | Bestiary / Incursion / Ultimatum | T16, no affixes | 10 | 10 | 4 / 3 / 3 |
| 01:03 | Betrayal / Expedition / Incursion | T16, no affixes | 10 | 12 | 6 / 2 / 4 |
| 01:03 | Betrayal / Expedition / Incursion | T16 | 10 | 10 | 5 / 3 / 2 |
| 01:05 | Betrayal / Expedition / Incursion | T11 | 9 | 10 | 5 / 2 / 3 |
| 01:06 | Betrayal / Expedition / Incursion | special: citadel, influence type 3 | 10 | 11 | 4 / 4 / 3 |
| 01:06 | Betrayal / Expedition / Incursion | special: 3 citadels, influence type 5 | 9 | 9 | 3 / 3 / 3 |
| 01:10 | Abyss / Blight / Legion | T16, no affixes | 10 | 12 | 5 / 5 / 2 |
| 01:11 | Abyss / Blight / Legion | T16, no affixes | 10 | 10 | 1 / 5 / 4 |
| 01:11 | Abyss / Blight / Legion | T16, no affixes | 10 | 10 | 1 / 5 / 4 |
| 01:12 | Abyss / Blight / Legion | T16, no affixes | 11 | 11 | 2 / 5 / 4 |
| 01:13 | Abyss / Blight / Legion | T16 | 9 | 9 | 3 / 3 / 3 |

Legion's counts leave out AdditionalLegion, which can't be detected at 8 (see below).

## What held

- **The stat set at 8 is 40 / 700 / 12500** in all 42 league slots, the same as the single
  8-Abyss map from the [level test](levels.md).
- **What each league's Threads give on their own didn't change** from 3 and 6:
  - Betrayal sets its job index.
  - Blight gets +1 blight and 20% longer paths, and Abyss its spawn stat.
  - Expedition, Incursion and Ultimatum only switch their content on.
- **Legion's extra spawns read 3, 4, 3, 4 and 3 at 8.** As at 6, this isn't a fixed amount, so
  `THREAD_BASE` marks it as varying. Before that, the analyzer counted it as 3–4 rolls of
  AdditionalLegion per map.
- **Area level, not map affixes, sets the hidden monster life bonus.** It was +109% at area
  level 83 and +61% at 78, with or without affixes.
- **The +5% rarity and +8% pack size on maps without affixes come from the atlas tree.** They
  match the affix-free 6/6/6 maps.
- **The special maps' citadel and influence stats come from the map.** They didn't change the
  Thread stats or the juice.

## Juice keeps growing

| | 3/3/3 | 6/6/6 | 8/8/8 |
|---|---|---|---|
| Juice rolls per map | 5.8 | 7.6 | 10.2 |
| Area level | 83 | mostly 77–78 | 83, one map at 78 |

Average juice rolls per map, by league:

| League | 3 Threads | 6 Threads | 8 Threads |
|---|---|---|---|
| Blight | 2.2 | 3.0 | 4.6 |
| Betrayal | 2.0 | 1.8 | 4.6 |
| Bestiary | 2.8 | 2.6 | 3.5 |
| Legion | 1.6 | 1.8 | 3.4 |
| Ultimatum | 1.0 | 2.6 | 3.25 |
| Incursion | 2.4 | 3.2 | 2.9 |
| Expedition | 1.2 | 2.4 | 2.8 |
| Abyss | 2.2 | 2.8 | 2.4 |

- **Six of these eight leagues rolled clearly more juice at 8.** Blight, Betrayal and Legion
  roughly doubled.
- **Abyss and Incursion appear to level off.** Abyss went 5 / 1 / 1 / 2 / 3 at 8. Both leagues
  have few juice mods, and Abyss had seen all of its mods by 6. Abyss is probably undercounted:
  three of its five mods (Mortars, ElitePairs, Consort) are on/off, so a repeat roll can't show.
- **Map tier doesn't drive juice.** The tier-11 map rolled 10, the same as the tier-16 maps in
  its set, and the special maps rolled 11 and 9. This settles the doubt from the 6/6/6 run, where
  Thread count and area level changed together: Thread count is what matters.
- **Ultimatum** has climbed at every step: exactly one juice mod at 3, then 2.6, then 3–4 at 8.
  Hearts rolled in all four maps and SoulCore in three.

## Juice mods first seen at 8

| Mod | Maps at 8 | What it does |
|---|---|---|
| Betrayal Fracture | 3/5 | Veiled items drop with fractured veiled mods |
| Betrayal Sculpture | 3/5 | A corpse sculpture spawns |
| Legion InvertedLegion | 3/5 | 50% chance of an inverted legion |
| Legion MonstersRankHigher | 2/5 | 50% chance for legion monsters to rank up |
| Blight FreeTowers | 3/5 | Towers cost nothing (tower cost -100%) |
| Blight Pantheon | 1/5 | The blight core is replaced by a pantheon god |
| Ritual Nameless | 2/5 | The ritual type is Nameless (in the two-league maps) |
| Breach WombgiftRareDrops | 1/5 | Breach rares can drop an extra wombgift (in the two-league maps) |

None of these eight rolled in any map at 3 or 6 Threads. **Legion SmallCrystals** points the same
way: 0 of 5 Legion maps at 3, 2 of 5 at 6, and 5 of 5 at 8. Together with the ten mods first seen
at 6 (in [juice-mods.md](juice-mods.md#first-seen-at-6-threads-10)), some mods look either
locked behind a Thread count or much more common above it. With about 5 maps per league per
Thread count, a rare mod can easily miss every map, so this can't tell the two apart.

**Update:** later maps settled it. SmallCrystals rolled at 2 Legion Threads, and Fracture,
Sculpture, FreeTowers and InvertedLegion at 6, so these mods are rare, not locked to 8. See
[results-1116-mixed.md](results-1116-mixed.md#the-only-at-8-mods-rolled-lower).

Mods that had been rare turned up again too: Red Beast Invasion (22 red beasts = one Invasion
plus one ExtraRedBeasts), Ultimatum DoubleDown, and Expedition RunicRares (2 maps).

## Repeat rolls

- Research chest clusters read 33, two rolls, in three of the five Betrayal maps. Before this it
  had happened once. Extra abysses read 3 in one map.
- **Betrayal MonsterMod rolled twice in one map:** `map_betrayal_members_x_additional_mods` read
  4, and one roll is exactly 2. Until now every repeat was a mod that adds more of some content
  (abysses, red beasts, chest clusters). This one adds monster modifiers, so
  any juice mod with a counted stat may be able to repeat.

## Two leagues: Breach / Ritual at 8/8

Five maps with only two leagues slotted, to see whether fewer leagues changes anything. Four were
tier 15 (area level 82, hidden monster life +98%) and one tier 16 (level 83, +109%). Two had map
affixes.

| Time | Map | Juice rolls | Breach | Ritual |
|---|---|---|---|---|
| 01:17 | T15, no affixes | 6 | 2 | 4 |
| 01:17 | T15, no affixes | 6 | 4 | 2 |
| 01:17 | T15 | 5 | 1 | 4 |
| 01:18 | T16 | 9 | 4 | 5 |
| 01:19 | T15, no affixes | 7 | 4 | 3 |

| | 3 leagues at 8 (14 maps) | 2 leagues at 8 (5 maps) |
|---|---|---|
| Juice rolls per map | 10.2 | 6.6 |
| Juice rolls per league | 3.4 | 3.3 |
| Stat set per league | 40 / 700 / 12500 | 40 / 700 / 12500 |
| Atlas map-mod bonus | +15% (5% × 3 Thread types) | +10% (5% × 2) |

- **Juice is decided league by league.** Leaving a slot empty doesn't give the other leagues more
  juice, so a two-league map gets about a third less juice than a three-league one.
- **The only other change is the atlas passive,** which scales with the number of Thread types.
- **The cost is lower too.** Each league's tankiness applies only to its own monsters, so one
  fewer league means one fewer group of tankier monsters.
- Ritual averaged 3.6 juice rolls at 8, double its 1.8 at 6. Breach averaged 3.0.

## Breach: hive or unstable breaches

Hives and unstable breaches are mutually exclusive in the game. Every Breach map so far has
exactly one of `map_contains_breach_hive` and `map_contains_additional_unstable_breaches`:

| Breach Threads | Maps with a hive | Maps with unstable breaches (count) |
|---|---|---|
| 3 | 4 | 2 (2, 3) |
| 4 and 7 | 0 | 2 (3, 4) |
| 6 | 3 | 2 (3, 3) |
| 8 | 5 | 0 |

- No Mods.dat row can put a hive on a map any more (only the old `ScarabBreachesNew1` did), so
  the hive comes from the Threads. The unstable breaches are the other branch.
- **The Breach juice mods follow the branch.** GuaranteedFortress (the hive is always a sky
  fortress) and EstablishedSpreadCoffers (hives contain coffers) only rolled on hive maps.
  GuaranteedBoss (an unstable breach spawns a boss) only rolled on unstable-breach maps.
- **At 8 all five maps had the hive.** At the roughly 60% hive rate seen at 3 and 6, five in a
  row happens about 1 time in 13, so it may be chance.
- **Breach's juice counts below 8 are uncertain.** The analyzer counts each unstable breach as a
  roll of AdditionalUnstableBreaches (+1), which is where its x2 to x4 repeats came from. If the
  count comes partly or wholly from the Threads, those repeats aren't real. The 8-Thread figures
  aren't affected, since no unstable breaches appeared.

## Analyzer fixes from this data

- **Negative stat values.** FreeTowers sets tower cost to -100%, and `analyze.py` used to read any
  value at or below 0 as "didn't roll", so FreeTowers could never be detected. Only 0 counts as
  not rolled now.
- **Legion at 8** is marked as varying in `THREAD_BASE`, as at 6. AdditionalLegion (+1) can't be
  detected at 6 or 8 Threads.

## Still never seen

Bestiary BlackMorrigan and ExtraHarvestBeasts, Blight GigaLane, Incursion
ReplacePacksWithArchitects and ContainsTempests, Expedition SpecialRemnants and Legion
InstantBreakout: 7 of 70. Every league has now been run at 8, so these mods are either very rare
or don't come from Threads.
