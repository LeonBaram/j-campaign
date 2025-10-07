# {{name}}
**class/level**: {{class}} {{level}}  
**race**: {{race}}  
**background**: {{background}}  
**age**: {{age}}  
**gender**: {{gender}}  
**alignment**: {{alignment}}

**inspiration**: {{inspiration}}

**conditions:**
{{conditions}}

**proficiency bonus**: +{{prof}}

## stats
|stat|score|save|mod|
|---|---|---|---|
|STR|{{strength}}|{{str_save}}|{{str}}|
|DEX|{{dexterity}}|{{dex_save}}|{{dex}}|
|CON|{{constitution}}|{{con_save}}|{{con}}|
|INT|{{intelligence}}|{{int_save}}|{{int}}|
|WIS|{{wisdom}}|{{wis_save}}*|{{wis}}|
|CHA|{{charisma}}|{{cha_save}}*|{{cha}}|

\*proficient save

## combat

**hp**: {{hp}}
**temp hp**: {{temp_hp}}

**hit dice**: {{hit_dice}}

{{#death_saves}}
**death saves**: {{successes}} successes; {{failures}} failures
{{/death_saves}}

**armor class**: {{armor_class}}
  
**initiatve**: {{initiative}}

**speed**: {{speed}}

**attacks:**
{{#attacks}}
- **{{name}}:** {{atk}} to hit, damage: {{dmg}}
{{/attacks}}

**divine sense:** {{divine_sense}}  
**lay on hands:** {{lay_on_hands}}  
**channel divinity:** {{channel_divinity}}

## skills
{{#skills}}
- athletics: {{athletics}}
- insight: {{insight}}
- persuasion: {{persuasion}}
- intimidation: {{intimidation}}
{{/skills}}

**passive perception**: {{passive_perception}}

**total prepared spells:** {{prepared_total}}

## spell slots
|lvl|slots|
|---|---|
{{#spell_slots}}
|1|{{lvl1}}|
{{/spell_slots}}

**spell attack**: {{spells.attack}}
**spell save dc**: {{spells.save_dc}}

### spells prepared
#### lvl1
{{#spells.lvl1}}
- {{{.}}}
{{/spells.lvl1}}

## other proficiencies  
{{{other_proficiencies}}}

## languages
{{{languages}}}

{{#money}}
**money:** {{gp}}gp / {{sp}}sp / {{cp}}cp
{{/money}}

{{#bank_account}}
**deposited in bank:** {{gp}}gp / {{sp}}sp / {{cp}}cp
{{/bank_account}}

**total weight:** {{inv_total_weight}}

**max weight**: {{inv_max_weight}}

## inventory
{{#inventory}}
- {{{.}}}
{{/inventory}}

## features  
{{#features}}
### {{name}}
{{{summary}}} [link]({{link}})
{{/features}}

## Characteristics

### Personality Traits
{{{personality_traits}}}

### Ideal
{{{ideals}}}

### Bonds
{{{bonds}}}

### Flaws
{{{flaws}}}

#### Notes
{{{notes}}}
