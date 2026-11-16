# 3/3/3 run (2026-11-15)

## Setup

- **Maps:** 17, all tier 16, all 3 leagues × 3 Threads.
- **Coverage:** together they cover all 45 league pairs at least once.
- **Atlas tree:**
  - The Legion maps used a tree with Legion passives (tree index 3).
  - Every other map used a tree with no league content, only shrines, Searing Exarch and map-mod
    juicing (tree index 1).
  - **Exception:** the 6th map (Abyss/Betrayal/Breach) still logged tree index 3, so the tree
    switch happened one map later than intended. Tree 3 only adds Legion stats, so that map is
    still fine for non-Legion conclusions.
- **Scarabs:** none. They no longer exist.

## Maps

| Time | Leagues | Tree | Juice mods | Juice rolls |
|---|---|---|---|---|
| 17:12 | Abyss / Bestiary / Legion | 3 | 6 | 6 |
| 17:22 | Breach / Incursion / Legion | 3 | 6 | 6 |
| 17:26 | Blight / Legion / Ritual | 3 | 5 | 5 |
| 17:38 | Betrayal / Expedition / Legion | 3 | 6 | 6 |
| 18:08 | Abyss / Legion / Ultimatum | 3 | 2 | 2 |
| 18:40 | Abyss / Betrayal / Breach | 3 | 4 | 8 |
| 18:51 | Abyss / Blight / Incursion | 1 | 6 | 6 |
| 19:11 | Abyss / Expedition / Ritual | 1 | 5 | 7 |
| 19:31 | Bestiary / Betrayal / Blight | 1 | 8 | 8 |
| 19:39 | Bestiary / Blight / Ultimatum | 1 | 4 | 5 |
| 19:49 | Bestiary / Breach / Ritual | 1 | 5 | 9 |
| 19:57 | Bestiary / Expedition / Incursion | 1 | 5 | 5 |
| 20:03 | Betrayal / Incursion / Ritual | 1 | 7 | 7 |
| 20:10 | Betrayal / Incursion / Ultimatum | 1 | 4 | 4 |
| 20:19 | Blight / Breach / Expedition | 1 | 6 | 6 |
| 20:39 | Blight / Expedition / Ultimatum | 1 | 6 | 6 |
| 20:48 | Breach / Ritual / Ultimatum | 1 | 3 | 3 |

- **Juice mods:** how many different juice mods matched.
- **Juice rolls:** those mods' rolls added up, counting repeats (see
  [juice-mods.md](juice-mods.md)).

## What we found

1. **Mixing doesn't change the Thread stat set.** Every league in every map got the same
   5 / 40 / 2500.
2. **No stat depended on which pair of leagues shared the map.** We traced every stat on every
   map to one of these sources:
   - a juice mod;
   - the Thread stat set;
   - a stat that marks the league as present;
   - a map affix: boss possessed, Bloodlines, elemental equilibrium, the random monster and
     player mods;
   - an Eldritch altar;
   - the atlas tree.

   The exceptions are the over-range values in the stacking table in
   [juice-mods.md](juice-mods.md). That's still only one map per pair, so a weak pair effect
   could have been missed.
3. **What 3 Threads of a league give on their own.** These held across every map:

   | League | Stats |
   |---|---|
   | All | `map_<league>_scarab_count` 3, plus the Thread stat set |
   | Abyss | `map_spawn_abysses` 1 (the Thread type's base stat) |
   | Bestiary | `map_bestiary_league` 2 |
   | Betrayal | `map_betrayal_league` 1, `betrayal_job_index` 13 or 14 |
   | Blight | `map_num_extra_blights_` 1, `blight_path_piece_length_modifier_%` 20 |
   | Breach | Either `map_contains_breach_hive` 1 (3 maps) or `map_contains_additional_unstable_breaches` 2–3 (2 maps). Never both, never neither. |
   | Expedition | `map_expedition_league` 1 |
   | Incursion | `map_incursion_league` 1 |
   | Legion | `map_legion_league_extra_spawns` 2. It reads 3 when the Additional Legion juice mod rolls. |
   | Ritual | `map_area_contains_rituals` 1 |
   | Ultimatum | `map_area_contains_ultimatum` 1 |

   - Blight's path-length stat isn't granted by any Mods.dat row.
   - The breach hive is only granted by the old `ScarabBreachesNew1` row, which nothing can roll
     now. Both look like Thread effects the server applies directly.
   - Breach's either/or could be its Thread effect choosing one of two outcomes. Or the unstable
     breaches are repeat rolls of the AdditionalUnstableBreaches juice mod (1 per roll).
     **Update:** hives and unstable breaches are mutually exclusive in the game, and all 18 Breach
     maps through 8 Threads had exactly one of the two. See
     [results-888.md](results-888.md#breach-hive-or-unstable-breaches).
4. **Juice per map varies widely,** from 2 to 9 rolls (5.8 on average), but each league's count
   stays small (0 to 4). Ultimatum rolled exactly one in each of its 5 maps.
