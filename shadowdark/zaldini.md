# Zaldini the Mind Goblin

**Ancestry:** Goblin; **Background:** Wanted; **Alignment:** Chaotic; **Deity:** Shune the Vile\
**Languages:** Common, Goblin, Orcish, Thanian, Diabolic, Draconic\
**Class:** Wizard; **Title:** Channeler; **Level:** 3; **XP:** 13 / 30

| **str**        | **dex**         | **con** | **int**         | **wis** | **cha** |
| -------------- | --------------- | ------- | --------------- | ------- | ------- |
| '8'`:STR` / -1 | 15 / '+2'`:dex` | 11 / +0 | 19 / '+4'`:int` | 9 / -1  | 12 / +1 |

**Keen Senses:** Can't be surprised\
**HP:** 8 / 8; **AC:** 12; **Attacks:** dagger, '2'`:=dex` (N), 1d4\
**Talents:** '+1' `:talent` to spellcasting checks\
**Spellcasting:** '+5' `:+=int+talent`

## Spells

| **Tier** | **Name**      | **Duration** | **Range** | **Description**                                                                              |
| -------- | ------------- | ------------ | --------- | -------------------------------------------------------------------------------------------- |
| 1        | Magic Missile | Instant      | Far       | ADV to cast, 1d4 dmg to 1 creature within Far range.                                         |
| 1        | Detect Magic  | Focus        | Near      | sense magic within Near range, hold for 2+ rounds for more info.(blocked by full barriers)   |
| 1        | Sleep         | Instant      | Near      | LV 0-2 creatures in a Near-sized cube sleep until shaken/hurt.                               |
| 1        | Burning Hands | Instant      | Close     | creatures within Close range around me take 1d6 damage. unattended flammable objects ignite. |
| 2        | Fixed Object  | 5 rounds     | Close     | touch an object \<= 5lb. it is completely unmovable for the duration (up to 5000lb of force) |

(Note: Close=5ft, Near=30ft, Far=line of sight)

## Gear

free carry:

- backpack
- **money:** 23.5gp

slots (max '10'`:=max(STR,10)`):

1. pole
2. .
3. rope, 60' / 60'
4. mirror
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

```lua calcmd
function max(x, y)
    if x >= y then
        return x
    else
        return y
    end
end
```
