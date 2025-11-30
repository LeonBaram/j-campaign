# Elbar Rockseeker

INSPIRATION: YES

Paladin (_Oath of Vengeance_); level '3'`:lvl`\
Guild Artisan; 'Lawful Good'`:alignment`\
69-year-old male Dwarf (_Mountain Dwarf_)

## Conditions:

- darkvision 60ft
- immune to disease
- resistance against poison damage
- advantage on saving throws against poison

proficiency bonus: '+2'`:+prof`

## Stats

| stat  | score      | mod         | save              |
| ----- | ---------- | ----------- | ----------------- |
| STR   | '19'`:STR` | '+4'`:+str` | '+4'`:+=str`      |
| DEX   | '12'`:DEX` | '+1'`:+dex` | '+1'`:+=dex`      |
| CON   | '18'`:CON` | '+4'`:+con` | '+4'`:+=con`      |
| INT   | '5' `:INT` | '-3'`:int`  | '-3'`:=int`       |
| WIS\* | '14'`:WIS` | '+2'`:+wis` | '+4'`:+=wis+prof` |
| CHA\* | '17'`:CHA` | '+3'`:+cha` | '+5'`:+=cha+prof` |

\*proficient save

## Skills

| skill        | bonus             |
| ------------ | ----------------- |
| athletics    | '+6'`:+=str+prof` |
| insight      | '+4'`:+=wis+prof` |
| persuasion   | '+5'`:+=cha+prof` |
| intimidation | '+5'`:+=cha+prof` |

**passive perception**: 12

## Combat

''`:=reset(longrest)`\
**hp**: 13 / 31\
**hit dice**: 3d10 / '3d10'`:=fmt(lvl,'d10')`

**armor class**: '18'`:=16+2`\
**initiatve**: '+1'`:+=dex`\
**speed**: 25

**attacks:**

- **talon (+1 longsword):** '+7'`:+=str+prof+1` to hit, damage: 1d8'+7'`:+=str+1+2` slashing (versatile)
- **warhammer:** '+6'`:+=str+prof` to hit, damage: 1d8'+6'`:+=str+2` bludgeoning (versatile)
- **handaxe:** '+6'`:+=str+prof` to hit, damage: 1d6'+6'`:+=str+2` slashing (thrown)

''`:=reset(longrest)`\
**divine sense:** 4 / '4'`:=cha+1`\
**lay on hands:** 5 / 15\
**channel divinity:** 1 / 1

## Spells

''`:=reset(longrest)`

| lvl1 spell slots |
| ---------------- |
| 3 / 3            |

**spell attack**: '+5'`:+=cha+prof`\
**spell save dc**: '13'`:=8+cha+prof`\
**total prepared spells:** '4'`:=cha+(lvl//2)`

**prepared spells:**

- lvl1:
    - cure wounds
    - bless
    - command
    - compelled duel
    - bane (always prepared)
    - hunter's mark (always prepared)

## Other Proficiencies

- smith's/mason's tools
- light/medium/heavy armor
- shields
- simple/martial weapons

## Languages

- common
- dwarven
- giant

**money:** 74gp / 4sp / 0cp

**deposited in bank:** 180gp / sp / cp

**max weight (lb):** '285'`:=STR*15`\
**current weight (lb):** '138'`:=total_weight()`

## Inventory

```lua calcmd
inventory = [[
    55lb    chain mail armor
    1lb     holy symbol - amulet
    5lb     backpack
    7lb     bedroll
    10lb    50ft rope
    4lb     traveler's clothes
    2lb     warhammer
    3lb     +1 longsword ("Talon"). once belonged to Aldith Tresendar, a.k.a the Black Hawk.
    6lb     shield
    1lb     tinderbox
16x 2lb     1-day rations
    5lb     waterskin
    2lb     handaxe
    3lb     net
            redbrand cloak
            diamond (5k gp)
]]
```

## Features

**divine sense**

> as an action, until end of next turn, you know the location of any celestial/fiend/undead within 60 feet that is not behind total cover. for any being you sense, you know their type but not their identity. within the same radius you also detect any place/object that has been consecrated/desecrated, as with the spell Hallow.
> [link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s0-0~sub_vengeance_phb=b1)

**lay on hands**

> total healing pool of 5\*lvl hp. as an action, can touch a creature and give them hp from the pool. can spend 5hp to heal 1 disease/poison. no effect on undead/constructs. [link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s0-1~sub_vengeance_phb=b1)

**divine smite**

> when you hit with an attack, can spend 1 level-n spell slot to deal (1+n)d8 bonus radiant damage [link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s1-0~sub_vengeance_phb=b1)

**fighting style**

> \+2 to damage rolls when wielding exactly 1 weapon in 1 hand [link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s1-1~sub_vengeance_phb=b1)

**spellcasting**

[link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s1-2~sub_vengeance_phb=b1)

**divine health**

> immune to disease [link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s2-0~sub_vengeance_phb=b1)

**channel divinity: abjure enemy**

> as an action, one creature within 60ft makes a WIS save. unaffected if immune to frighten. disadvantage if fiend/undead. on a fail, frightened for 1 minute or until damage. while frightened, speed is 0 regardless of bonuses. on a success, speed is halved for 1 minute or until damage.
> [link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s2-1~sub_vengeance_phb=b1)

**channel divinity: vow of enmity**

> as a bonus action, gain advantage on attacks against one creature within 10ft for 1 minute or until 0hp or unconscious.
> [link](https://2014.5e.tools/classes.html#paladin_phb,state:feature=s2-1~sub_vengeance_phb=b1)

**stonecunning**

> expertise in History checks about the origin of stonework [link](<https://2014.5e.tools/races.html#dwarf%20(mountain)_phb>)

**guild membership**

> As an established and respected member of a guild, you can rely on certain benefits that membership provides. Your fellow guild members will provide you with lodging and food if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a central place to meet other members of your profession, which can be a good place to meet potential patrons, allies, or hirelings.
> Guilds often wield tremendous political power. If you are accused of a crime, your guild will support you if a good case can be made for your innocence or the crime is justifiable. You can also gain access to powerful political figures through the guild, if you are a member in good standing. Such connections might require the donation of money or magic items to the guild's coffers.
> You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues to remain in the guild's good graces.
> [link](https://2014.5e.tools/backgrounds.html#guild%20artisan_phb)

## Characteristics

**Personality Traits**

- loves a good drink
- loves a good scrap (for fun, with the homies)
- bit of a gruff / stoic demeanor, but actually pretty generous and considerate with his friends

**Ideal**

- Generosity. My talents were given to me so that I could use them to benefit the world. (Good)

**Bonds**

- loves his sister Hilda, but they frequently bicker
- may have met uncle Gundren at 1-2 social family gatherings??
- R\&R A\&A is his and Hilda's baby
- absolutely hates criminals and evildoers (almost 0 nuance)

**Flaws**

- sometimes a _little_ racist in that way where you can tell he had a traditional Dwarven upbringing, but isn't actually trying to be mean or racially supremacist (basically the racism that comes from a place of ignorance, rather than the KKK shit)
- somewhat judgy of others' cultures
- almost always speaks his mind, except when in "business savvy" mode

## Notes

- monthly guild payment is 10gp instead of default due to adamantine shipment

## Utility/Helper Functions

```lua calcmd
-- stringifies and concatenates all the arguments
function fmt(...)
    out=''
    for _, arg in ipairs(table.pack(...)) do
        s = tostring(arg)
        if s == nil then
            s = ''
        end
        out=out..s
    end
    return out
end

-- calculate current total inventory weight based on item weights / quantities
function total_weight()
    local total = 0
    for submatch in string.gmatch(inventory, '([%d.]+)lb') do
        local w = tonumber(submatch)
        if w ~= nil then
            total = total + w
        end
    end
    for submatch in string.gmatch(inventory, '(%d+x%s+[%d.]+lb)') do
        local _, _, quantity, weight = string.find(submatch, '(%d+)x%s+([%d.]+)lb')
        local q, w = tonumber(quantity), tonumber(weight)
        if q == nil then
            q = 1
        end
        if w ~= nil then
            total = total + (q * w)
        end
    end
    return total
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
