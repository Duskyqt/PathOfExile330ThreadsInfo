# After the 2026-11-18 patch

# The data is being put out quickly just to illustrate the modifier differences, the rest of the data is incomplete.

The patch changed the Thread stat set, gave each league an extra stat of its own at 3, 6 and 8
Threads, guaranteed a minimum number of juice mods, and added six juice mods. These are the first
five maps after it, which between them cover every Thread count from 1 to 10.

## Setup

All five maps were Waste Pool, tier 16 (area level 83), on atlas tree index 1. The atlas passive
from the earlier runs (`map_mod_effect_+%_per_different_thread_type`) isn't on any of them.

| Time  | Leagues                                 | Total Threads |
| ----- | --------------------------------------- | ------------- |
| 18:17 | Ritual 3 / Blight 6 / Incursion 8       | 17            |
| 18:26 | Expedition 1 / Betrayal 2 / Incursion 4 | 7             |
| 18:27 | Expedition 5 / Bestiary 7               | 12            |
| 18:29 | Expedition 9                            | 9             |
| 18:29 | Expedition 10                           | 10            |

The game now also writes `map_total_thread_count`. The solo 9 and 10 maps carry the 10-Thread
passive's stats (`map_maximum_one_thread_slot`, `map_x_additional_free_threads_bypassing_maximum`
2, `map_threads_convert_to_gold_chance_%` 75).

Read these with `--since 2026-11-18` and the re-exported juice list:

```
python -I analyze.py --log path\to\maplog.jsonl --juice path\to\juice-mods.json --since 2026-11-18
```

## The new stat set

Each count comes from one league slot on one map. Before the patch these values never varied
between maps, so one reading each is probably enough.

| Threads | Damage | Tankiness | Rarity (permyriad) | Tankiness before | Rarity before |
| ------- | ------ | --------- | ------------------ | ---------------- | ------------- |
| 1       | —      | —         | —                  | —                | —             |
| 2       | +0%    | +23%      | 1200               | +25%             | 1500          |
| 3       | +5%    | +51%      | 2544               | +40%             | 2500          |
| 4       | +10%   | +86%      | 4049               | +70%             | 3800          |
| 5       | +15%   | +129%     | 5735               | +120%            | 5200          |
| 6       | +20%   | +182%     | 7623               | +210%            | 7000          |
| 7       | +25%   | +247%     | 9738               | +380%            | 9300          |
| 8       | +30%   | +327%     | 12107              | +700%            | 12500         |
| 9       | +35%   | +425%     | 14760              | +1050%           | 14500         |
| 10      | +40%   | +546%     | 17731              | +1400%           | 16000         |

- **Tankiness** is now a smooth curve, far lower from 6 Threads up. From 3 to 5 Threads it's
  higher than before, which the patch notes don't mention.
- **Rarity** is lower at 2 and 8 Threads, although the notes say "slightly higher at all Thread
  counts". It's higher everywhere else, most at 10.
- **Damage** now rises by exactly 5 per Thread, so from 7 up it's lower than before.
- **1 Thread** still gives no stat set.

### What this does to choosing a level

| Threads | Rarity ÷ tankiness | (1 + rarity) ÷ (1 + tankiness) | Before the patch |
| ------- | ------------------ | ------------------------------ | ---------------- |
| 2       | 0.52               | 0.91                           | 0.92             |
| 3       | 0.50               | 0.83                           | 0.89             |
| 4       | 0.47               | 0.76                           | 0.81             |
| 5       | 0.44               | 0.69                           | 0.69             |
| 6       | 0.42               | 0.62                           | 0.55             |
| 7       | 0.39               | 0.57                           | 0.40             |
| 8       | 0.37               | 0.52                           | 0.28             |
| 9       | 0.35               | 0.47                           | 0.21             |
| 10      | 0.32               | 0.43                           | 0.17             |

The third column is roughly loot per minute when kill speed limits you (see
[levels.md](levels.md#choosing-a-level)). Both still fall with every Thread, but far more
gently: 8 Threads is now worth about twice what it was, and 3 to 4 are slightly worse.

## Each league's new stat

| League and Threads  | What appeared                                                               | Patch notes           |
| ------------------- | --------------------------------------------------------------------------- | --------------------- |
| Expedition 1        | nothing                                                                     | nothing below 3       |
| Betrayal 2          | nothing                                                                     | nothing below 3       |
| Ritual 3            | `map_ritual_rarity_quantity_revive_penalty_+%` 20, no favours stat          | 20% increased favours |
| Incursion 4         | `map_incursion_pack_size_+%` 20, `map_incursion_number_of_rare_packs_+%` 15 | 20% pack size at 3    |
| Expedition 5        | `map_expedition_extra_relic_suffix_chance_%` 20                             | 15% at 3              |
| Blight 6            | `map_blight_lanes_spawn_at_least_magic_monsters_surpass_chance_%` 80        | 80% at 6              |
| Bestiary 7          | `map_additional_red_beasts` 6                                               | 3 at 6                |
| Incursion 8         | `map_incursion_pack_size_+%` 40, `map_incursion_number_of_rare_packs_+%` 30 | 40% at 8              |
| Expedition 9 and 10 | `map_expedition_extra_relic_suffix_chance_%` 50                             | 50% at 8              |

- **The tiers apply in between.** Incursion 4 got the 3-Thread value and Expedition 9 and 10 the
  8-Thread value, so a league gets the 3 tier from 3 to 5, the 6 tier at 6–7 and the 8 tier from 8
  up.
- **Incursion's rare packs** aren't in the per-count list. They're probably the separate "rare
  monsters in Incursions scale with Threads" change.
- **Expedition 5 read 20%, not 15%.** Either the notes are off, or 5 Threads gets something between
  the tiers.
- **Ritual's favours stat is missing.** The new RitualFavours juice mod uses
  `map_ritual_reward_count_+%`, and that stat isn't on the map. The 20 that is there names the
  revive penalty. So either the favours bonus reaches the map some other way, or it isn't live.
- **Bestiary's red beasts collide with juice.** ExtraRedBeasts (2–4) and Red Beast Invasion use the
  same stat. 6 at 7 Threads is 3 from the Threads plus one ExtraRedBeasts roll. `analyze.py` now
  subtracts the Bestiary amounts from the notes (2 / 3 / 4 by tier) on post-patch maps.
- **Legion will collide too:** its extra encounters likely land on
  `map_legion_league_extra_spawns`, which AdditionalLegion uses. Until a post-patch Legion map is
  read, `analyze.py` skips AdditionalLegion on post-patch maps.

## Juice

| League and Threads | Juice mods                                                  | Guaranteed minimum |
| ------------------ | ----------------------------------------------------------- | ------------------ |
| Expedition 1       | 1 (ReviveObelisk)                                           | 1                  |
| Betrayal 2         | 3 (MonsterMod, RareBodyguards, Sculpture)                   | 1                  |
| Ritual 3           | 1 (TributeBoss)                                             | 1                  |
| Incursion 4        | 3 (FleshMerchant, GoldPiles, Tempests)                      | 2                  |
| Expedition 5       | 2 (LogbookChest, RunicLieutenants)                          | 2                  |
| Blight 6           | 2 (ExileLane, Supercharge)                                  | 2                  |
| Bestiary 7         | 4 (EinharBloodAura, HaveWisps, ExtraRedBeasts, AzmeriHulks) | 2                  |
| Incursion 8        | 3 (CursedTreasure, VaalVessels, GoldenDoors)                | 3                  |
| Expedition 9       | 3 (ReviveObelisk, RunicLieutenants, Scale)                  | 3                  |
| Expedition 10      | 3 (ReviveObelisk, RunicLieutenants, Scale)                  | 3                  |

- **Every league met its minimum,** and six of ten rolled exactly the minimum.
- **Two mods we'd never seen rolled:** BetrayalRareBodyguards (new in the patch) at 2 Threads, and
  IncursionContainsTempests at 4. Tempests was one of the seven mods never seen before the patch;
  the notes call it new, but it was already in Mods.dat.
- One map per count can't say whether juice per league changed beyond the minimums.

## The re-exported juice list

`Mods.dat` now has 76 `RandomJuiceMod*` rows. The 70 old ones kept their stats and ranges, and the
Ultimatum upside mod is still there although it can no longer roll. The six new ones:

| Mod                        | Stat                                                               | What it does                                                        |
| -------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------- |
| RitualFavours              | `map_ritual_reward_count_+%` 150                                   | Ritual altars offer 150% more favours                               |
| BetrayalRareBodyguards     | `map_betrayal_initial_targets_have_x_additional_rare_bodyguards` 2 | First Betrayal targets get 2 extra rare bodyguards                  |
| IncursionRareBodyguards    | `map_incursion_architect_rare_bodyguard_per_previous_incursion` 1  | Architects get 1 extra rare per Incursion already completed         |
| BestiaryAdditionalModifier | `map_bestiary_beasts_X_additional_modifiers` 1                     | Red beasts get 1 extra Bestiary modifier                            |
| BreachDuplicateRares       | `map_breach_duplicate_final_rare_monsters` 1                       | Final-wave Breach rares are duplicated                              |
| BreachMagicMods            | `map_breach_magic_monsters_num_additional_modifiers` 1             | Magic Breach monsters get 1 extra modifier (not in the patch notes) |

`data/juice-mods.json` in this repo stays the pre-patch export, so the pre-patch numbers keep
reading the same.

## Next

- A post-patch Legion map, to measure its extra encounters and re-enable AdditionalLegion.
- A Ritual map at 6 or 8, to see whether a favours stat appears.
- Expedition at 3 or 4, to see whether its 3 tier is 15% or 20%.
- More maps per count, to see how much juice rolls above the new minimums.
