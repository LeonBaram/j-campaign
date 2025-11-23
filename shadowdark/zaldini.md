# Zaldini the Mind Goblin

**Ancestry:** Goblin; **Background:** Wanted; **Alignment:** Chaotic; **Deity:** Shune the Vile\
**Languages:** Common, Goblin, Orcish, Thanian, Diabolic, Draconic\
**Class:** Wizard; **Title:** Channeler; **Level:** 3; **XP:** 13 / 30

LUCK TOKEN: 1

| **str**        | **dex**         | **con** | **int**         | **wis** | **cha** |
| -------------- | --------------- | ------- | --------------- | ------- | ------- |
| '8'`:STR` / -1 | 15 / '+2'`:dex` | 11 / +0 | 19 / '+4'`:int` | 9 / -1  | 12 / +1 |

**Keen Senses:** Can't be surprised\
**HP:** 8 / 8; **AC:** 12; **Attacks:** dagger, '2'`:=dex` (N), 1d4\
**Talents:** '+1' `:talent` to spellcasting checks\
**Spellcasting:** '+5' `:+=int+talent`

## Spells

| **Tier** | **Name**       | **Duration** | **Range** | **Description**                                                                              |
| -------- | -------------- | ------------ | --------- | -------------------------------------------------------------------------------------------- |
| 1        | Magic Missile  | Instant      | Far       | ADV to cast, 1d4 dmg to 1 creature within Far range.                                         |
| 1        | ~Detect Magic~ | Focus        | Near      | sense magic within Near range, hold for 2+ rounds for more info.(blocked by full barriers)   |
| 1        | Sleep          | Instant      | Near      | LV 0-2 creatures in a Near-sized cube sleep until shaken/hurt.                               |
| 1        | Burning Hands  | Instant      | Close     | creatures within Close range around me take 1d6 damage. unattended flammable objects ignite. |
| 2        | Fixed Object   | 5 rounds     | Close     | touch an object \<= 5lb. it is completely unmovable for the duration (up to 5000lb of force) |

(Note: Close=5ft, Near=30ft, Far=line of sight)

### Wands

**Detect Thoughts** (tier 2, Focus): choose 1 creature in Near range. Each round learn its immediate thoughts.\
On each of its turns it makes a WIS check vs my last spellcasting check. when it succeeds the spell ends,\
and it knows you were reading its mind.

### Spell Roll Outcomes

| outcome | spellcasting check                       | focus check                   |
| ------- | ---------------------------------------- | ----------------------------- |
| nat 20  | x2 one numerical effect                  | keep focusing                 |
| success | cast spell normally                      | keep focusing                 |
| fail    | spell fails, gone for today              | spell is done. can recast     |
| nat 1   | spell fails, gone for today. roll mishap | spell is done. gone for today |

## Gear

free carry:

- backpack
- **money:** 23.6gp

slots (max '10'`:=max(STR,10)`):

1. pole
2. pokeball potion: Domini angel
3. mirror
4. pokeball potion: Djinni
5. magic wand of Detect Thoughts
6. rations (3)
7. broken jade hair comb (60gp)
8. jade and gold scarab pin (20gp)
9. Staff of the Cobra
10. torch

## Allies

- 3 famous bard allies (TBD??)
- snake wizard ally ("Gorgoroth")

## Magic Items

#### Staff Of The Cobra

_A curved scepter tipped with a ruby-eyed, flaring cobra head._

**Bonus**. +1 staff.

**Benefit**. All snakes regard you with a friendly attitude unless you do something to upset them. Once per day, you can throw the staff to the ground. It becomes a giant snake for 5 rounds that obeys your mental commands. If the giant snake goes to 0 HP, it reverts into a staff.

**Curse**. You have disadvantage on attacks and casting hostile spells targeting snakes.

## Utility Functions

```lua calcmd
-- take the max of 2 numbers
function max(x, y)
    if x >= y then
        return x
    else
        return y
    end
end

-- print "RESET" if any of the given reset conditions are true
function reset(...)
    for _, condition in ipairs(table.pack(...)) do
        if condition then
            return "RESET"
        end
    end
    return ""
end
```
