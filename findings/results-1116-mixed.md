# Mixed maps, last before the patch (2026-11-16 afternoon)

19 maps logged after the solo 10-Legion run and before the 2026-11-18 Thread patch. They weren't
a planned run: different map bases, uneven Thread splits, one Bestiary atlas tree, and 12 maps
with no Threads at all. They're the last pre-patch data.

## Maps with Threads

| Time | Map | Tree | Leagues | Juice rolls | Per league |
|---|---|---|---|---|---|
| 14:32 | City Square, T12 (level 79), affixes | 2 | Bestiary 8 / Betrayal 6 / Blight 6 | 7 | 5 / 1 / 1 |
| 14:36 | City Square, T12, no affixes | 2 | Bestiary 5 / Blight 6 / Legion 6 | 7 | 2 / 2 / 3 |
| 14:46 | City Square, T12, no affixes | 2 | Bestiary 6 / Betrayal 6 / Breach 6 | 7 | 1 / 2 / 4 |
| 14:56 | City Square, T12, no affixes | 2 | Bestiary 6 / Betrayal 6 / Breach 6 | 10 | 3 / 5 / 2 |
| 16:21 | Maze, T16 (level 83), no affixes | 1 | Legion 2 | 3 | 3 |
| 16:24 | Temple, T16, no affixes | 1 | Legion 2 | 1 | 1 |
| 16:33 | Maze of the Minotaur, T16, affixes | 1 | Betrayal 6 / Breach 3 / Incursion 3 | 8 | 5 / 2 / 1 |

Breach's counts include AdditionalUnstableBreaches, which may partly be Breach's own Thread
content (see [results-888.md](results-888.md#breach-hive-or-unstable-breaches)). Legion's counts
leave out AdditionalLegion, which can't be detected at 2 or 6 Threads.

**Atlas tree 2 is a Bestiary tree.** It puts 14 Bestiary stats on the map that no other tree
does, among them `map_additional_red_beast_chance_%`, `map_rare_beasts_more_common` and
`map_yellow_beasts_replaced_by_red_beasts_chance_%`, plus `map_mod_effect_+%_per_mod`. Red beast
counts on these maps (31, 6, 4, 6) may include the tree's share, so the Bestiary juice counts
on tree 2 aren't comparable with tree 1.

## What held

- **Each league's stat set follows its own Thread count** in uneven splits too: 5 gave
  15 / 120 / 5200, 6 gave 20 / 210 / 7000, 8 gave 40 / 700 / 12500, and Legion 2 gave
  0 / 25 / 1500, all as in the [level test](levels.md).
- **Breach's branch held.** All three Breach maps had unstable breaches (3, 1 and 2) and no hive,
  and the unstable-breach-only GuaranteedBoss rolled on both City Square Breach maps.
- **Legion's extra spawns at 2 Threads read 2 and 1.** `THREAD_BASE` now marks 2 as varying,
  like 6, 8 and 10. Before that, the analyzer counted them as AdditionalLegion rolls.

## The "only at 8" mods rolled lower

| Mod | Seen before only at | Rolled here at |
|---|---|---|
| Legion SmallCrystals | 6 and up (0/5 at 3) | **2**, on both Legion 2 maps, tree 1 |
| Betrayal Fracture | 8 | 6, tree 2 |
| Betrayal Sculpture | 8 | 6, tree 2 |
| Blight FreeTowers | 8 | 6, tree 2 |
| Legion InvertedLegion | 8 | 6, tree 2 |

The four at 6 were on the Bestiary tree, which doesn't touch Betrayal, Blight or Legion. The
SmallCrystals result is on tree 1. So the mods we listed as "first seen at 6" or "first seen at 8"
aren't locked to a Thread count. They're rare, and the earlier runs had about 5 maps per league
per Thread count, too few to catch them below 8. Whether they get more common at higher counts
is still open.

The patch notes back this up: they say Abyssal Consorts "can no longer appear when only spending
one Abyssal Thread", which means that before the patch a juice mod could roll at any count.

## Maps without Threads

| Maps | Atlas tree | Thread stats |
|---|---|---|
| Dunes, Theatre of Lies, Fortress | 1 | none |
| Pit of the Chimera (2), Lair of the Hydra | 1 | none |
| Rewritten and Augmented Distant Memory (Maven invitations) | none | none |
| Whakawairua Tuahu, Mao Kun, Acton's Nightmare, Maelstrom of Chaos (unique maps) | none | none |

The unique maps and Maven invitations carry no atlas tree index and no Thread stats at all, so
neither the atlas tree nor Threads apply there. The log doesn't record whether Threads were
slotted for the other maps, so their missing Thread stats say nothing either way.
