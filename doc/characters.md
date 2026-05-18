# GBDB Characters json format

## More info

### Recommend weapon's 
Recommended list of weapona good for the character and explain why is it good.

Quality of weapon (stars) and where is from (wish, anvil, explore) is stored in weapon's DB

```
"recommended_weapons": [
 {
  "id": str,
  "why": str, 
  "rating":
 },
]
```
### artefacts - set

What sets are the best what jiu is good and why.

 - set id: is id of full set for this character. isn't made for out of json use!
 - id: id of artefact
 - id2: is here if artefact cobo use 2+2 pice instead of 4 pice. is empty if it si 4 pice set.

```
"recommended_sets": [
 {
  "set_id" str,
  "id": str, 
  "id2": str, 
  "why": str, 
  "rating": int,
 },
]
```

### artefacts - stats

This is for good main or sub stats.

In goblet, sans and cirlet are ids of good min stats (cr, atk, er).

Substats: are for witch substats are good. can be apply on all 5 artefacts.
```
"stats": {
 "goblet": [],
 "sands": [],
 "circlet": [],

 "substats": [],
},
 ```

## Json Show case

```
{
 "id": str, // id of character
 "name": str, // Name of character
 "limited" boolean, // Is character limited. Limited = True, standard = False
 "element": str, // Element of character: Pyro, Geo, Electro
 "weapon_type": str, // Weapon character type: Sword, Bow, Catalyst
 "rarity": int, // Rarity of character. 4 or 5 star
 "region": str, // Monstad, Fontaine, Inazima
 
 "recommended_weapons": [ // list of recommend weapons
  {
   "id": str, // Id of recommend weapon id
   "why": str, // Why is this weapon good
   "rating": int // Rating of weapon 1-10
  }
 ],

 "artefacts" : {
  "recommended_sets": [
    {
     "set_id" str, // id of set for this char.
     "id": str, // id of set
     "id2": str, // id of 2. set if it is 2+2 instead of 4 piece. Can be null!
     "why": str, // Why is set or sets good?
     "rating“: int, // Rating of set or sets 1-10
  }
 ],
  "stats": {
   "goblet": [], // List of good main stats for goblet 
   "sands": [], // List of good main stats for sans
   "circlet": [], // List of good main stats for circlet
   "substats": [], // List of best substats 
  }
 },

 "talents": [
  {
   "pos": int, // 1=atk, 2=skil, 3=burst, 4=pasive
   "recommend_level": int, // only for 1-3
   "name": str, // name of talent
   "description": str, // description of talent
   "razor": str, // description of talent in lazor language
   "cooldown" int, // cooldown of talent
   "animation_time": int, // how long take to get back to game
  }
 ],
 
 "base_stats": {
  "scale": str, // From witch stat is character scale
  "atk": int, // atack
  "hp": int, // hit poins
  "def": int, // defence
  "cr": int, // crit rate
  "cd": int, // crit dgm
  "er": int, // energy recharge
  "burst_cost" int // How mouch cost burst
 },

 "materials": {
  "common_drop_id": str, // id of lv up materials | character + talent
  "boss_material_id": str, // if of world boss drop | character
  "boss_talent_id": str // id of weekly boss material drop | talents
  "book_id": str, // book id to upgrade talents | talents
  "local_spectality_id": str // a world material | character
 },
 
 "constellation": [ // List of cons and thier quality
  {
   "level": int, // con lv. 1-6
   "name": str, // con name
   "description": str, // con description
   "value": int, // How mouch is con woth pull. 0-10
   "why": str // Why is con good or bad
  }
 ],
 
 "playstyles": [ // List of possible play styles
  {
   "playstyle_id" str, // id for play style
   "type": str, // main DPS, healer, sub-DPS
   "set_id": str, // recommend set off artefacts 
  }
 ],

 "teams": [
  {
   "name": str, // Name of team combo
   "playstyle_id": str, // Support build don't play as min dps
   "slot_2": list, // List off ids of character to slot 2
   "slot_3": list, // List off ids of character to slot 3
   "slot_4": list, // List off ids of character to slot 4
   "rating": int, // Rating how good is a team
   "why": str, // Why is a team good
   "dmg": int, // What is a theoretical dmg
   "showcase": str, // Link on YouTube video with showcase of team.
  }
 ],
}
```
