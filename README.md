# What Threads Actually Do to Your Maps

_Path of Exile 3.30 · after the 2026-11-18 Thread patch_

> **Disclaimer:** this data only covers the modifiers that Threads apply to a map. In-game
> interactions between objects, such as the "Blighted Strongbox", don't show up in it, because
> they aren't as easily quantified.

## Patch update (2026-11-18): the new Thread curve

> **This is a preliminary update.** Its only job is to get the new percentage changes between
> Thread levels out quickly. It rests on the first five maps after the patch, one reading per
> Thread count. Juice and everything else will follow once we've run more maps.

**The patch replaced the whole stat set with a smooth curve.** Each extra Thread now multiplies
monster tankiness by **×1.23** and the rarity bonus by **×1.12**, at every step from 2 to 10.
Damage goes up by a flat 5 points per Thread. Before the patch, the tankiness steps grew from
×1.12 to ×1.67, which is what made 7 and 8 Threads so brutal.

| Going from                 | 2→3   | 3→4   | 4→5   | 5→6   | 6→7   | 7→8   | 8→9\* | 9→10\* |
| -------------------------- | :---: | :---: | :---: | :---: | :---: | :---: | :----: | :-----: |
| Tankiness (points)         | +28   | +35   | +43   | +53   | +65   | +80   | +98    | +121    |
| Monsters this much tankier | ×1.23 | ×1.23 | ×1.23 | ×1.23 | ×1.23 | ×1.23 | ×1.23  | ×1.23   |
| Damage (points)            | +5    | +5    | +5    | +5    | +5    | +5    | +5     | +5      |
| Rarity (points)            | +13   | +15   | +17   | +19   | +21   | +24   | +27    | +30     |

\* _9 and 10 Threads still need the atlas passive that lifts the cap, and only work with a
single league mechanic slotted._

Here's how each Thread count compares with before the patch:

| Threads | Tankiness | Before | Damage | Before | Rarity | Before |
| :-----: | :-------: | :----: | :----: | :----: | :----: | :----: |
|    2    |   +23%    |  +25%  |  +0%   |  +0%   |  +12%  |  +15%  |
|    3    |   +51%    |  +40%  |  +5%   |  +5%   |  +25%  |  +25%  |
|    4    |   +86%    |  +70%  |  +10%  |  +10%  |  +40%  |  +38%  |
|    5    |   +129%   | +120%  |  +15%  |  +15%  |  +57%  |  +52%  |
|    6    |   +182%   | +210%  |  +20%  |  +20%  |  +76%  |  +70%  |
|    7    |   +247%   | +380%  |  +25%  |  +28%  |  +97%  |  +93%  |
|    8    |   +327%   | +700%  |  +30%  |  +40%  | +121%  | +125%  |
|    9    |   +425%   | +1050% |  +35%  |  +45%  | +148%  | +145%  |
|   10    |   +546%   | +1400% |  +40%  |  +50%  | +177%  | +160%  |

What changed:

- **High Thread counts got much cheaper.** At 8 Threads, monsters are now 4.3× as tanky instead
  of 8×. At 10 they're 6.5× instead of 15×.
- **Low counts got a little worse.** At 3 to 5 Threads, tankiness went _up_ (3 Threads went from
  +40% to +51%), and rarity barely moved. The patch notes don't mention this.
- **Rarity is lower at 2 and 8 Threads,** even though the patch notes say it's "slightly higher
  at all Thread counts". Everywhere else it's a bit higher, most of all at 10.
- **Damage is lower from 7 Threads up,** because it now climbs a flat 5 points per Thread.
- **1 Thread still gives no stats.**

**Also in the patch** (one map each, so treat these as early sightings):

- Each league mechanic gets an extra stat of its own at 3, 6 and 8 Threads, such as more
  Incursion pack size or more red beasts. The tiers apply in between: 4 and 5 Threads get the
  3-Thread bonus, 7 gets the 6-Thread one, and 9 and 10 get the 8-Thread one.
- Every map now gets a guaranteed minimum number of juice mods, rising with the Thread count.
  All five maps met it, and six of the ten league slots rolled exactly the minimum.
- Six new juice mods were added, including more Ritual favours, extra rare bodyguards for
  Betrayal and Incursion, and duplicated final-wave Breach rares.

The full readings are in [findings/results-patch-1118.md](findings/results-patch-1118.md).
