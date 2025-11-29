from KCFSyntax import *
_damagedEntity = "@n[nbt={HurtTime:10s},tag=!self]"

_player = "@s[type=player]"
_debugger = "@a[tag=debug]"

level: int # For pylance
started: int

# Difficulty
# 1 = Easy
# 2 = Normal
# 3 = Hard
difficulty: int
waiting: int

# Prevents cheating
gameiter: int

"""
Weapon data:

Status: Chance of applying status
DMG: Base DMG of weapon

Fire: Whether this weapon can apply fire. 0 = NO, 1 = WITH STATUS, 2 = ALWAYS
Ice, Water, Electric, Nature: ^^^

CR: base Crit Rate
CD: base Crit DMG

ATKSPD: Attack Speed
"""

def lt_normal():
    self.looptimes = level / 5 + 1

    if difficulty == 3:
        self.looptimes *= 2

    for i in range(self.looptimes):
        run('summon experience_orb ~ ~ ~ {Value:5}')
        run('summon item ~ ~ ~ {Item:{id:"minecraft:sunflower",count:1,components:{"minecraft:item_name":"Coin"}}}')
        # 50% of 1 experience
        randint(self.temp, 0, 1)
        if self.temp == 0:
            run('summon experience_orb ~ ~ ~ {Value:1}')
        randint(self.temp, 1, 100)
        if level < 50:
            if 'score @s temp matches 1..20' and level < 10: 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:leather_horse_armor",count:1,components:{"minecraft:item_name":"Bronze Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 21..25': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:iron_horse_armor",count:1,components:{"minecraft:item_name":"Silver Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 27': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:golden_horse_armor",count:1,components:{"minecraft:item_name":"Gold Relic", "minecraft:custom_data":{GetRelic:1}}}}')
        else:
            if 'score @s temp matches 1..3' and level < 70: 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:golden_horse_armor",count:1,components:{"minecraft:item_name":"Gold Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 4': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:item_name":"Diamond Relic", "minecraft:custom_data":{GetRelic:1}}}}')
        # FLOWERS
        randint(self.temp, 1, 1000)
        if level < 50:
            if 'score @s temp matches 1..100' and level < 20: 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:white_tulip",count:1,components:{"minecraft:item_name":"White Flower", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 101..130': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:orange_tulip",count:1,components:{"minecraft:item_name":"Orange Flower", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 131..136': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:red_tulip",count:1,components:{"minecraft:item_name":"Red Flower", "minecraft:custom_data":{GetRelic:1}}}}')
        else:
            if 'score @s temp matches 1..50' and level < 70: 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:orange_tulip",count:1,components:{"minecraft:item_name":"Orange Flower", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 51..60': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:red_tulip",count:1,components:{"minecraft:item_name":"Red Flower", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 61..66':
                run('summon item ~ ~ ~ {Item:{id:"minecraft:pink_tulip",count:1,components:{"minecraft:item_name":"Purple Flower", "minecraft:custom_data":{GetRelic:1}}}}')
    # MODS
        randint(self.temp, 1, 100)
        if level < 50:
            if 'score @s temp matches 1..5': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:blade_pottery_sherd",count:1,components:{"minecraft:item_name":"Common Mod", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 6..8': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:flow_pottery_sherd",count:1,components:{"minecraft:item_name":"Uncommon Mod", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 9': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:prize_pottery_sherd",count:1,components:{"minecraft:item_name":"Rare Mod", "minecraft:custom_data":{GetRelic:1}}}}')
    if level >= 50:
        randint(self.temp, 1, 100)
        if 'score @s temp matches 1..5': 
            run('summon item ~ ~ ~ {Item:{id:"minecraft:blade_pottery_sherd",count:1,components:{"minecraft:item_name":"Common Mod", "minecraft:custom_data":{GetRelic:1}}}}')
        elif 'score @s temp matches 6..10': 
            run('summon item ~ ~ ~ {Item:{id:"minecraft:flow_pottery_sherd",count:1,components:{"minecraft:item_name":"Uncommon Mod", "minecraft:custom_data":{GetRelic:1}}}}')
        elif 'score @s temp matches 11..15': 
            run('summon item ~ ~ ~ {Item:{id:"minecraft:prize_pottery_sherd",count:1,components:{"minecraft:item_name":"Rare Mod", "minecraft:custom_data":{GetRelic:1}}}}')

def lt_elite():
    self.looptimes = level / 5 + 1
    if difficulty == 3:
        self.looptimes *= 2

    for i in range(self.looptimes):
        run('summon item ~ ~ ~ {Item:{id:"minecraft:sunflower",count:5,components:{"minecraft:item_name":"Coin"}}}')
        run('summon experience_orb ~ ~ ~ {Value:16}')

        if level < 10:
            run('summon item ~ ~ ~ {Item:{id:"minecraft:leather_horse_armor",count:1,components:{"minecraft:item_name":"Bronze Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            run('summon item ~ ~ ~ {Item:{id:"minecraft:white_tulip",count:1,components:{"minecraft:item_name":"White Flower", "minecraft:custom_data":{GetRelic:1}}}}')
        elif level < 50:
            run('summon item ~ ~ ~ {Item:{id:"minecraft:iron_horse_armor",count:1,components:{"minecraft:item_name":"Silver Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            run('summon item ~ ~ ~ {Item:{id:"minecraft:orange_tulip",count:1,components:{"minecraft:item_name":"Orange Flower", "minecraft:custom_data":{GetRelic:1}}}}')

        randint(self.temp, 1, 100)
        if level < 50:
            if 'score @s temp matches 1..50' and level < 25: 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:iron_horse_armor",count:1,components:{"minecraft:item_name":"Silver Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 51..71': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:golden_horse_armor",count:1,components:{"minecraft:item_name":"Gold Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 72..77': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:item_name":"Diamond Relic", "minecraft:custom_data":{GetRelic:1}}}}')

        else:

            if 'score @s temp matches 1..10' and level < 70: 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:golden_horse_armor",count:1,components:{"minecraft:item_name":"Gold Relic", "minecraft:custom_data":{GetRelic:1}}}}')
            elif 'score @s temp matches 11..21': 
                run('summon item ~ ~ ~ {Item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:item_name":"Diamond Relic", "minecraft:custom_data":{GetRelic:1}}}}')

        randint(self.temp, 1, 100)
        if 'score @s temp matches 1..8' and level < 70: 
            run('summon item ~ ~ ~ {Item:{id:"minecraft:red_tulip",count:1,components:{"minecraft:item_name":"Red Flower", "minecraft:custom_data":{GetRelic:1}}}}')
        elif 'score @s temp matches 9..11': 
            run('summon item ~ ~ ~ {Item:{id:"minecraft:pink_tulip",count:1,components:{"minecraft:item_name":"Purple Flower", "minecraft:custom_data":{GetRelic:1}}}}')
            
    if level >= 50:
        run('summon item ~ ~ ~ {Item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:item_name":"Diamond Relic", "minecraft:custom_data":{GetRelic:1}}}}')

    # Mods
    randint(self.temp, 1, 10)
    if 'score @s temp matches 1..6': 
        run('summon item ~ ~ ~ {Item:{id:"minecraft:blade_pottery_sherd",count:1,components:{"minecraft:item_name":"Common Mod", "minecraft:custom_data":{GetRelic:1}}}}')
    elif 'score @s temp matches 7..9': 
        run('summon item ~ ~ ~ {Item:{id:"minecraft:flow_pottery_sherd",count:1,components:{"minecraft:item_name":"Uncommon Mod", "minecraft:custom_data":{GetRelic:1}}}}')
    elif 'score @s temp matches 10': 
        run('summon item ~ ~ ~ {Item:{id:"minecraft:prize_pottery_sherd",count:1,components:{"minecraft:item_name":"Rare Mod", "minecraft:custom_data":{GetRelic:1}}}}')

def lt_boss():
    self.looptimes = level / 5 + 1

    for i in range(self.looptimes):
        run('summon item ~ ~ ~ {Item:{id:"minecraft:sunflower",count:10,components:{"minecraft:item_name":"Coin"}}}')
        run('summon experience_orb ~ ~ ~ {Value:30}')

    # Based on floor
    if level >= 50:
        run('summon item ~ ~ ~ {Item:{id:"minecraft:diamond_horse_armor",count:3,components:{"minecraft:item_name":"Diamond Relic", "minecraft:custom_data":{GetRelic:1}}}}')
        run('summon item ~ ~ ~ {Item:{id:"minecraft:prize_pottery_sherd",count:3,components:{"minecraft:item_name":"Rare Mod", "minecraft:custom_data":{GetRelic:1}}}}')
    elif level >= 29:
        run('summon item ~ ~ ~ {Item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:item_name":"Diamond Relic", "minecraft:custom_data":{GetRelic:1}}}}')
        run('summon item ~ ~ ~ {Item:{id:"minecraft:prize_pottery_sherd",count:1,components:{"minecraft:item_name":"Rare Mod", "minecraft:custom_data":{GetRelic:1}}}}')
    else:
        run('summon item ~ ~ ~ {Item:{id:"minecraft:golden_horse_armor",count:1,components:{"minecraft:item_name":"Gold Relic", "minecraft:custom_data":{GetRelic:1}}}}')
        run('summon item ~ ~ ~ {Item:{id:"minecraft:prize_pottery_sherd",count:1,components:{"minecraft:item_name":"Rare Mod", "minecraft:custom_data":{GetRelic:1}}}}')
        run('summon item ~ ~ ~ {Item:{id:"minecraft:flow_pottery_sherd",count:2,components:{"minecraft:item_name":"Uncommon Mod", "minecraft:custom_data":{GetRelic:1}}}}')





def dokill():
    if entity(_player):
        run('damage @s 2 out_of_world')
        self.health = self.max_health
        self.shields = self.max_shields
        self.invincible = 100
        removeStatuses()
    elif entity('@s[tag=!notmob,tag=mob]'):
        if not self.died == 1:
            # Drop items
            if entity('@s[tag=boss]'):
                lt_boss()
            elif entity('@s[tag=elite]'):
                lt_elite()
            else:
                lt_normal()
            self.died = 1 # In case it doesn't die for some reason, we don't want it to keep spamming items     
        kill(self)   
    elif entity('@s[tag=!notmob]'):
        # Kill self
        kill(self)

def load():
    # CONFIG # 

    # Limit text displays
    # When dealing large small numbers, many DMG numbers can clutter and reduce lag
    # This helps prevent both client and server lag on large hits
    # Default: 200. 200 is a good starting value as text displays do not get ticked by functions
    # You'll rarely ever see 200 anyway! Even something like 50 is fine enough.
    # Setting this to a large negative number (due to bugs sometimes) essentially disables damage numbers
    TEXT_DISPLAY_LIMIT = 200 # Set to 100 to further improve lag

    
    # END OF CONFIG #



    # Refresh text display just in case
    textdisplays = 0

    var('atk', 'custom:damage_dealt')
    var('dmgtaken', 'custom:damage_resisted')
    var('lvl', 'level')

    # KCash support!
    var('kcash')

    var('xpos')
    var('ypos')
    var('zpos')

    run('gamerule naturalRegeneration false')
    run('gamerule doMobSpawning false')
    run('gamerule mobGriefing false')
    run('gamerule commandModificationBlockLimit 1000000')

    run('team add mob "Mob team"')

    sec()
    sec3()
    tick10()

    trigger('stats')
    trigger('start')
    trigger('buy')
    if block('8 -61 8', cobblestone) and block('12 -61 20', stone) and block('3 -61 5', stone):
        spawnArena()

    compileweapons()

    difficulty = 2

    run('bossbar add timer "Timer"')
    run('bossbar set timer max 1800')
    run('bossbar set timer color yellow')

    '@a[gamemode=creative]'.invincible += 20
    '@a[gamemode=spectator]'.invincible += 20

def triggers__start():
    if self.start == 1:
        difficulty = 2
    elif self.start == 2:
        difficulty = 1
    elif self.start == 3:
        difficulty = 3
    start()

def spawnArena():
    fill('-9 -62 -9', '25 3 25', quartz_block, hollow)
    run('fill -8 -61 -8 24 -61 24 minecraft:grass_block')
    run('fill 24 -60 24 10 -60 10 grass_block')
    run('fill 9 -60 24 9 -60 13 minecraft:grass_block')
    run('fill 8 -60 19 8 -60 24 minecraft:grass_block')
    run('fill 10 -60 11 13 -60 11 air')
    run('fill 10 -60 10 16 -60 10 air')
    run('fill 26 7 26 -10 3 -10 minecraft:quartz_block hollow')
    run('fill -9 7 -9 25 7 25 air')

    # Now add some grass!
    # for i in range(16):
    #     summon(pig, '~ ~ ~', {'Tags': '[arenagrass]'})
    
    # run('spreadplayers 8 8 8 16 under -32 false @e[type=pig,tag=arenagrass]')

    # execute('at @e[type=pig,tag=arenagrass]', (
    #     run('setblock ~ ~-2 ~ dispenser[facing=up,triggered=false]{Items:[{Slot:0b,id:"minecraft:bone_meal",count:1}]} replace'),
    #     run('setblock ~ ~-3 ~ redstone_block')
    # ))

    def sacleanup():
        execute('at @e[type=pig, tag=arenagrass]', fill('~ ~-2 ~', '~ ~-3 ~', air))
        run('fill -8 3 24 24 3 -8 barrier')
        # tp('@e[type=pig, tag=arenagrass]', '0 -100 0')
        # kill('@e[type=pig, tag=arenagrass]')
        kill('@e[type=item]')
        run('fill 24 -62 24 -8 -62 -8 bedrock')
        createmsg()

    def createmsg():
        kill('@e[tag=joinmsg]')
        run('summon text_display 8.5 5.0 25.9 {Tags:[notmob,important,joinmsg],Rotation:[-180F,0F],transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[5f,5f,5f]},text:[{"color":"#FFF700","text":"C"},{"color":"#FDF800","text":"l"},{"color":"#FCF801","text":"i"},{"color":"#FAF901","text":"c"},{"color":"#F9FA02","text":"k "},{"color":"#F7FB02","text":"t"},{"color":"#F6FB03","text":"o "},{"color":"#F4FC03","text":"J"},{"color":"#F3FD04","text":"o"},{"color":"#F1FE04","text":"i"},{"color":"#EEFF05","text":"n"}],background:16711680}')
        run('summon interaction 8.5 4.75 29.5 {width:9f,height:2f,response:1b,Tags:[joinInteraction,joinmsg,important,notmob]}')
        run('summon text_display 8 4 20 {Tags:[notmob,important,joinmsg],billboard:"vertical",text:[{"bold":true,"color":"yellow","text":"Welcome to KCSurvival"},{"bold":false,"color":"aqua","text":"\\nKCSurvival is a floor based gamemode with a RPG touch to the survival experience."},{"color":"green","text":"\\n\\nCan you beat all 50 floors?"},{"bold":false,"color":"yellow","text":"\\n\\nType /trigger start to play\\nType /trigger start set # for difficulty\\n1 = easy, 2 = normal, 3 = hard"}],background:268435456}')

    schedule('5t', sacleanup)

def sec3():
    schedule('3s', sec3)
    
    execute('as @a', tickmodifiers)

def triggers__stats():
    run('tellraw @s ["",{"text":"Player Stats:","color":"aqua"},{"text":"\\n"},{"text":"Base Defense: ","color":"light_purple"},{"score":{"name":"@s","objective":"defense"},"color":"green"},{"text":" | Bonus DMG: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"lvl"},"color":"green"},{"text":"0%","color":"green"},{"text":"\\n"},{"text":"Player Bonus Stats:","color":"aqua"},{"text":"\\n"},{"text":"Base DMG: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.dmgbonus"},"color":"green"},{"text":"%","color":"green"},{"text":" | Elemental Mastery: ","color":"light_purple"},{"score":{"name":"@s","objective":"em"},"color":"green"},{"text":"\\n"},{"text":"Status Chance: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.status"},"color":"green"},{"text":"%","color":"green"},{"text":" | Multihit: ","color":"light_purple"},{"score":{"name":"@s","objective":"multihit"},"color":"green"},{"text":"%","color":"green"},{"text":"\\n"},{"text":"Critical Chance: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.cr"},"color":"green"},{"text":"%","color":"green"},{"text":" | Critical Damage: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.cd"},"color":"green"},{"text":"%","color":"green"},{"text":"\\n"},{"text":"Attack Speed: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.atkspd"},"color":"green"},{"text":"%","color":"green"},{"text":"\\n"},{"text":"Bonus Elemental DMG:","color":"aqua"},{"text":"\\n"},{"text":"Fire: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.fire"},"color":"green"},{"text":"%","color":"green"},{"text":" | Ice: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.ice"},"color":"green"},{"text":"%","color":"green"},{"text":" | Water: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.water"},"color":"green"},{"text":"%","color":"green"},{"text":"\\nElectric: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.electric"},"color":"green"},{"text":"%","color":"green"},{"text":" | Nature: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.nature"},"color":"green"},{"text":"%","color":"green"}]')

def addweapont(ID, Cost, Item, Name, Description, DMG, CR, CD, ATKSPD, Status, Fire, Ice, Water, Electric, Nature, Root):
    run(f'data modify storage kcs:weapons {ID}.itemdata set value \'{{"id": "{Item}", "count": 1, "components":{{blocks_attacks:{{block_delay_seconds:0.05,damage_reductions:[{{base:1,factor:0.25,type:["mob_attack","arrow","magic","mob_projectile","explosion"]}}],item_damage:{{threshold:0,base:2,factor:0.1}},block_sound:"entity.player.attack.strong"}},max_damage:500,custom_name:[{{"text":"{Name}","italic":false}}],lore:[[{{"text":"{Description}","italic":false,"color":"gray"}}],"",[{{"text":"Base DMG: {DMG}","italic":false,"color":"gray"}}],[{{"text":"Base Status: {Status}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Chance: {CR}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Damage: {CD}%","italic":false,"color":"gray"}}],[{{"text":"Base Attack Speed: {ATKSPD}/s","italic":false,"color":"gray"}}]],custom_data:{{Root: "{Root}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: {Fire}, Ice: {Ice}, Water: {Water}, Electric: {Electric}, Nature: {Nature}}},attribute_modifiers:[{{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{{type:"hidden"}},operation:add_value}},{{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{{type:"hidden"}},operation:add_value}},{{type:attack_speed,amount:{ATKSPD},slot:mainhand,id:"weapon_atkspdmod",operation:add_value}}]}}}}\'')
    run(f'data modify storage kcs:weapons {ID}.shopdata set value {{"Cost": {Cost}, "Name": "{Name}", "ItemData": \'{{"action":"show_item", "id": "{Item}", "count": 1, "components":{{blocks_attacks:{{block_delay_seconds:0.05,damage_reductions:[{{base:1,factor:0.25,type:["mob_attack","arrow","magic","mob_projectile","explosion"]}}],item_damage:{{threshold:0,base:2,factor:0.1}},block_sound:"entity.player.attack.strong"}},max_damage:500,custom_name:[{{"text":"{Name}","italic":false}}],lore:[[{{"text":"{Description}","italic":false,"color":"gray"}}],"",[{{"text":"Base DMG: {DMG}","italic":false,"color":"gray"}}],[{{"text":"Base Status: {Status}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Chance: {CR}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Damage: {CD}%","italic":false,"color":"gray"}}],[{{"text":"Base Attack Speed: {ATKSPD}/s","italic":false,"color":"gray"}}]],custom_data:{{Root: "{Root}",DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: {Fire}, Ice: {Ice}, Water: {Water}, Electric: {Electric}, Nature: {Nature}}},attribute_modifiers:[{{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{{type:"hidden"}},operation:add_value}},{{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{{type:"hidden"}},operation:add_value}},{{type:attack_speed,amount:{ATKSPD},slot:mainhand,id:"weapon_atkspdmod",operation:add_value}}]}}}}\'}}')
def addshortweapon(ID, Cost, Item, Name, Description, DMG, CR, CD, ATKSPD, Status, Fire, Ice, Water, Electric, Nature, Root):
    run(f'data modify storage kcs:weapons {ID}.itemdata set value \'{{"id": "{Item}", "count": 1, "components":{{custom_name:[{{"text":"{Name}","italic":false}}],lore:[[{{"text":"{Description}","italic":false,"color":"gray"}}],"",[{{"text":"Base DMG: {DMG}","italic":false,"color":"gray"}}],[{{"text":"Base Status: {Status}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Chance: {CR}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Damage: {CD}%","italic":false,"color":"gray"}}],[{{"text":"Base Attack Speed: {ATKSPD}/s","italic":false,"color":"gray"}}]],custom_data:{{Root: "{Root}",DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: {Fire}, Ice: {Ice}, Water: {Water}, Electric: {Electric}, Nature: {Nature}}},attribute_modifiers:[{{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{{type:"hidden"}},operation:add_value}},{{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{{type:"hidden"}},operation:add_value}},{{id:"weapon_short",type:"entity_interaction_range",amount:-0.5,operation:"add_multiplied_total",slot:"mainhand"}},{{type:attack_speed,amount:{ATKSPD},slot:mainhand,id:"weapon_atkspdmod",operation:add_value}}]}}}}\'')
    run(f'data modify storage kcs:weapons {ID}.shopdata set value {{"Cost": {Cost}, "Name": "{Name}", "ItemData": \'{{"action":"show_item", "id": "{Item}", "count": 1, "components":{{custom_name:[{{"text":"{Name}","italic":false}}],lore:[[{{"text":"{Description}","italic":false,"color":"gray"}}],"",[{{"text":"Base DMG: {DMG}","italic":false,"color":"gray"}}],[{{"text":"Base Status: {Status}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Chance: {CR}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Damage: {CD}%","italic":false,"color":"gray"}}],[{{"text":"Base Attack Speed: {ATKSPD}/s","italic":false,"color":"gray"}}]],custom_data:{{Root: "{Root}",DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: {Fire}, Ice: {Ice}, Water: {Water}, Electric: {Electric}, Nature: {Nature}}},attribute_modifiers:[{{id:"weapon_short",type:"entity_interaction_range",amount:-0.5,operation:"add_multiplied_total",slot:"mainhand"}},{{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{{type:"hidden"}},operation:add_value}},{{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{{type:"hidden"}},operation:add_value}},{{type:attack_speed,amount:{ATKSPD},slot:mainhand,id:"weapon_atkspdmod",operation:add_value}}]}}}}\'}}')

def addweapon(ID: str):
    run(f'data modify storage kcf:functionargs Root set value "{ID}"')
    run('function kcf:addweapont with storage kcf:functionargs')

def giveweapon(ID: str):
    """Gives a weapon to the player based on the KCS Weapon ID"""
    run(f'data modify storage kcf:functionargs itemdata set from storage kcs:weapons {ID}.itemdata')
    def giveweapont(itemdata: str):
        run(f'summon item ~ ~ ~ {{Tags: [notmob], PickupDelay:0, Item: {itemdata}}}')
    run('execute at @s run function kcf:giveweapont with storage kcf:functionargs')

def addstandardweapon(ID, NormalCost, Cost, Item, Name, Description, DMG, CR, CD, ATKSPD, Status):
    run(f'''function kcf:addweapont {{ID: "{ID}", Cost: {NormalCost}, Item: "{Item}", Name: "{Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 0, Electric: 0, Nature: 0, Root: "{ID}"}}''')
    run(f'''function kcf:addweapont {{ID: "{ID}_fire", Cost: {Cost}, Item: "{Item}", Name: "Flaming {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 1, Ice: 0, Water: 0, Electric: 0, Nature: 0, Root: "{ID}"}}''')
    run(f'''function kcf:addweapont {{ID: "{ID}_ice", Cost: {Cost}, Item: "{Item}", Name: "Iced {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 1, Water: 0, Electric: 0, Nature: 0, Root: "{ID}"}}''')
    run(f'''function kcf:addweapont {{ID: "{ID}_water", Cost: {Cost}, Item: "{Item}", Name: "Hydrous {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 1, Electric: 0, Nature: 0, Root: "{ID}"}}''')
    run(f'''function kcf:addweapont {{ID: "{ID}_electric", Cost: {Cost}, Item: "{Item}", Name: "Shocking {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 0, Electric: 1, Nature: 0, Root: "{ID}"}}''')
    run(f'''function kcf:addweapont {{ID: "{ID}_nature", Cost: {Cost}, Item: "{Item}", Name: "Nurturing {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 0, Electric: 0, Nature: 1, Root: "{ID}"}}''')
def addstandardshortweapon(ID, NormalCost, Cost, Item, Name, Description, DMG, CR, CD, ATKSPD, Status):
    run(f'''function kcf:addshortweapon {{ID: "{ID}", Cost: {NormalCost}, Item: "{Item}", Name: "{Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 0, Electric: 0, Nature: 0}}''')
    run(f'''function kcf:addshortweapon {{ID: "{ID}_fire", Cost: {Cost}, Item: "{Item}", Name: "Flaming {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 1, Ice: 0, Water: 0, Electric: 0, Nature: 0}}''')
    run(f'''function kcf:addshortweapon {{ID: "{ID}_ice", Cost: {Cost}, Item: "{Item}", Name: "Iced {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 1, Water: 0, Electric: 0, Nature: 0}}''')
    run(f'''function kcf:addshortweapon {{ID: "{ID}_water", Cost: {Cost}, Item: "{Item}", Name: "Hydrous {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 1, Electric: 0, Nature: 0}}''')
    run(f'''function kcf:addshortweapon {{ID: "{ID}_electric", Cost: {Cost}, Item: "{Item}", Name: "Shocking {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 0, Electric: 1, Nature: 0}}''')
    run(f'''function kcf:addshortweapon {{ID: "{ID}_nature", Cost: {Cost}, Item: "{Item}", Name: "Nurturing {Name}", Description: "{Description}", DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: 0, Ice: 0, Water: 0, Electric: 0, Nature: 1}}''')

def compileweapons():
    """
    I am using Minecraft to "compile" our weapons f orfuture use.
    This basically sets up all the strings so I can both give and show this weapon in chat, etc
    """
    addweapon({
        'ID': '"ts_fire"',
        'Cost': 0,
        'Item': '"iron_sword"',
        'Name': '"Fire Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30, "CR": 25, "CD": 50,
        "Status": 75, "ATKSPD": 1.6,
        "Fire": 1, "Ice": 0, "Water": 0, "Electric": 0, "Nature": 0
    })
    addweapon({
        'ID': '"ts_ice"',
        'Cost': 0,
        'Item': '"iron_sword"',
        'Name': '"Ice Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30, "CR": 25, "CD": 50,
        "Status": 75, "ATKSPD": 1.6,
        "Fire": 0, "Ice": 1, "Water": 0, "Electric": 0, "Nature": 0
    })
    addweapon({
        'ID': '"ts_water"',
        'Cost': 0,
        'Item': '"iron_sword"',
        'Name': '"Water Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30, "CR": 25, "CD": 50,
        "Status": 75, "ATKSPD": 1.6,
        "Fire": 0, "Ice": 0, "Water": 1, "Electric": 0, "Nature": 0
    })
    addweapon({
        'ID': '"ts_electric"',
        'Cost': 0,
        'Item': '"iron_sword"',
        'Name': '"Electric Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30, "CR": 25, "CD": 50,
        "Status": 75, "ATKSPD": 1.6,
        "Fire": 0, "Ice": 0, "Water": 0, "Electric": 1, "Nature": 0
    })
    addweapon({
        'ID': '"ts_nature"',
        'Cost': 0,
        'Item': '"iron_sword"',
        'Name': '"Nature Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30, "CR": 25, "CD": 50,
        "Status": 75, "ATKSPD": 1.6,
        "Fire": 0, "Ice": 0, "Water": 0, "Electric": 0, "Nature": 1
    })
    addstandardweapon({
        'ID': '"diamondsword"', 'Cost': 200, 'NormalCost': 180,
        'Item': '"diamond_sword"', 'Name': '"Diamond Sword"',
        "Description": '"The diamond sword focused heavily on its Critical abilities, enhancing mid-game combat."',
        "DMG": 200, "CR": 35, "CD": 120,
        "Status": 20, "ATKSPD": 1.6
    })
    addstandardweapon({
        'ID': '"ironsword"', 'Cost': 100, 'NormalCost': 80,
        'Item': '"iron_sword"', 'Name': '"Iron Sword"',
        "Description": '"The standard sword wielded by many major swordsman with its decent DMG, status chance, and its critical abilities"',
        "DMG": 185, "CR": 25, "CD": 75,
        "Status": 35, "ATKSPD": 1.6
    })
    addstandardweapon({
        'ID': '"coppersword"', 'Cost': 75, 'NormalCost': 20,
        'Item': '"copper_sword"', 'Name': '"Copper Sword"',
        "Description": '"A standard sword that is very conductive but lacks the standard damage output. The recommended elemental applier for beginners."',
        "DMG": 30, "CR": 15, "CD": 50,
        "Status": 75, "ATKSPD": 1.6
    })
    addstandardweapon({
        'ID': '"goldensword"', 'Cost': 150, 'NormalCost': 135,
        'Item': '"golden_sword"', 'Name': '"Golden Sword"',
        "Description": '"The heavy golden sword focused heavily on its damage and status chance, but lacked Critical abilities."',
        "DMG": 400, "CR": 10, "CD": 75,
        "Status": 80, "ATKSPD": 1
    })
    addstandardweapon({
        'ID': '"stonesword"', 'Cost': 50, 'NormalCost': 45,
        'Item': '"stone_sword"', 'Name': '"Stone Sword"',
        "Description": '"This starting sword deals decent damage but lacks the required stats for powerful builds."',
        "DMG": 150, "CR": 5, "CD": 50,
        "Status": 5, "ATKSPD": 1.6
    })
    addstandardshortweapon({
        'ID': '"irondagger"', 'Cost': 50, 'NormalCost': 45,
        'Item': '"iron_sword"', 'Name': '"Iron Dagger"',
        "Description": '"A smaller version of the standard sword, this weapon is deadly both in speed and critical damage. Has 50% less range."',
        "DMG": 100, "CR": 15, "CD": 100,
        "Status": 12, "ATKSPD": 3
    })
    addstandardshortweapon({
        'ID': '"diamonddagger"', 'Cost': 200, 'NormalCost': 185,
        'Item': '"diamond_sword"', 'Name': '"Diamond Dagger"',
        "Description": '"A smaller version of the standard sword, this weapon is deadly both in speed and critical damage. Has 50% less range."',
        "DMG": 120, "CR": 15, "CD": 200,
        "Status": 10, "ATKSPD": 3.2
    })
    addweapon({
        'ID': '"thorshammer"', 'Cost': 200,
        'Item': '"mace"', 'Name': '"Thor\'s Hammer"',
        "Description": '"Based on the popular Mace, this old-fashioned weapon comes pre-installed with an Electric status charge (not guaranteed)."',
        "DMG": 600, "CR": 35, "CD": 200,
        "Status": 50, "ATKSPD": 0.4,
        "Fire": 0, "Ice": 0, "Water": 0, "Electric": 1, "Nature": 0
    })
    addweapon({
        'ID': '"frostysword"', 'Cost': 200,
        'Item': '"diamond_sword"', 'Name': '"Frosty Sword"',
        "Description": '"It\'s so cold! Must be freezing for the entity hit! Has a guaranteed Ice status."',
        "DMG": 100, "CR": 25, "CD": 100,
        "Status": 5, "ATKSPD": 1.6,
        "Fire": 0, "Ice": 2, "Water": 0, "Electric": 0, "Nature": 0
    })



def displayreactionm(Name: str, Color: str, x: float, y: float, z: float):
    run(f'execute at @s positioned ~{x} ~{y} ~{z} run summon text_display ^ ^ ^ {{Tags:[notmob,dmgtext],teleport_duration:0,start_interpolation:-1,interpolation_duration:0,transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}, billboard:"center",see_through:1b,text:{{"color":"{Color}","text":"{Name}","bold":true}},background:268435456,glow_color_override:1b,Glowing:1b, shadow: 1b}}')

def displayreaction(Name: str, Color: str):
    if textdisplays >= TEXT_DISPLAY_LIMIT: return

    run(f'data modify storage kcf:functionargs Name set value "{Name}"')
    run(f'data modify storage kcf:functionargs Color set value "{Color}"')
    run('''
execute store result storage kcf:functionargs x float 0.1 run random value -6..6
execute store result storage kcf:functionargs y float 0.1 run random value 10..16
execute store result storage kcf:functionargs z float 0.1 run random value -6..6

function kcf:displayreactionm with storage kcf:functionargs
    ''')
    run('data modify storage kcf:functionargs Color set value "white"')

    textdisplays += 1

def displaydmg(Symbol: str, takedmg: int, Color: str):
    if 'entity @s[tag=notmob]': return
    if textdisplays >= TEXT_DISPLAY_LIMIT: return
    # Note that Symbol, takedmg, and color are already set.
    
    # run(f'tellraw @a "SYMBOL:{Symbol}, TAKEDMG: {takedmg}, COLOR:{Color}"')

    run('''
execute store result storage kcf:functionargs x float 0.1 run random value -6..6
execute store result storage kcf:functionargs y float 0.1 run random value 10..16
execute store result storage kcf:functionargs z float 0.1 run random value -6..6
    ''')
    
    if self.takedmg >= 1000:
        if self.takedmg >= 1000000:
            # Weird formula because scale by 0.1 causes floating-point errors
            self.dec = self.takedmg / 100000 % 10
            self.whole = self.takedmg / 1000000
            run('data modify storage kcf:functionargs compactLetter set value "M"')
        else:
            self.dec = self.takedmg / 100 % 10
            self.whole = self.takedmg / 1000
            run('data modify storage kcf:functionargs compactLetter set value "K"')

        run('execute store result storage kcf:functionargs dec int 1 run scoreboard players get @s dec')
        run('execute store result storage kcf:functionargs whole int 1 run scoreboard players get @s whole')
        run('function kcf:displaydmgmd with storage kcf:functionargs')

    else:
        run('function kcf:displaydmgm with storage kcf:functionargs')
    
    textdisplays += 1
    

def displaydmgM(Symbol: str, takedmg: int, Color: str, x: float, y: float, z: float):
    run(f'execute at @s positioned ~{x} ~{y} ~{z} run summon text_display ^ ^ ^ {{Tags:[notmob,notDone,dmgtext],teleport_duration:0,start_interpolation:-1,interpolation_duration:0,transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}, billboard:"center",see_through:1b,text:{{"color":"{Color}","text":"{Symbol} {takedmg}","bold":false}},background:268435456,glow_color_override:1b,Glowing:1b, shadow: 1b}}')
def displaydmgMD(Symbol: str, dec: int, whole: int, Color: str, x: float, y: float, z: float, compactLetter: str):
    run(f'execute at @s positioned ~{x} ~{y} ~{z} run summon text_display ^ ^ ^ {{Tags:[notmob,notDone,dmgtext],teleport_duration:0,start_interpolation:-1,interpolation_duration:0,transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}, billboard:"center",see_through:1b,text:{{"color":"{Color}","text":"{Symbol} {whole}.{dec}{compactLetter}","bold":false}},background:268435456,glow_color_override:1b,Glowing:1b, shadow: 1b}}')


def elementEffects():
    if self.fire > 0 and not entity('@s[tag=fire]'):
        # Blaze: immune
        self.takedmg = 2 * self.takeem * self.fireS

        # Zombie: 7x effectiveness
        if entity('@s[type=zombie]'):
            self.takedmg *= 7

        doReactionDMG()
    if self.ice > 0 and not entity('@s[tag=ice]'):
        if self.iceS == 1: effect(self, slowness, 1, 0, True)
        elif self.iceS == 2: effect(self, slowness, 1, 1, True)
        elif self.iceS == 3: effect(self, slowness, 1, 2, True)
        elif self.iceS == 4: effect(self, slowness, 1, 3, True)
        elif self.iceS == 5: effect(self, slowness, 1, 4, True)
        elif self.iceS == 6: effect(self, slowness, 1, 5, True)
        elif self.iceS >= 7: effect(self, slowness, 1, 6, True)

        # Husk: Deal frostburn
        if entity('@s[type=husk]'):
            self.takedmg = 5 * self.takeem * self.iceS
            doReactionDMG()

    if self.nature > 0 and not entity('@s[tag=nature]'):
        self.takedmg = self.takeem * self.natureS
        doHPDMG()

    # Reactions
    if self.electrified > 0:
        self.takedmg = 30 * self.takeem
        # 2x shields effectiveness
        if self.shields > 0:
            self.takedmg *= 2
            
            # Iron Golem: 20x shields effectiveness
            if entity('@s[type=iron_golem]'):
                self.takedmg *= 20

        elif entity('@s[type=iron_golem]'):
            self.takedmg *= 5

        doElectricDMG()

        self.electrified -= 1

    if self.viral > 0:
        self.takedmg = 15 * self.takeem
        doReactionDMG()

        if entity(_player):
            "@a[distance=1.1..3]".takedmg = self.takedmg / 2
            execute("as @a[distance=1.1..3]", doReactionDMG)
        else:
            "@e[type=!player,distance=1.1..3]".takedmg = self.takedmg / 2
            execute("as @e[type=!player, distance=1.1..3]", doReactionDMG)

        self.viral -= 1

def elementEffects10t():    
    # Element statuses
    execute('as @e[tag=fire]', (set(self.fireS, 2), set(self.fire, 20)))
    execute('as @e[tag=ice]', (set(self.iceS, 2), set(self.ice, 20)))
    execute('as @e[tag=water]', (set(self.waterS, 2), set(self.water, 20)))
    execute('as @e[tag=electric]', (set(self.electricS, 2), set(self.electric, 20)))
    execute('as @e[tag=nature]', (set(self.natureS, 2), set(self.nature, 20)))

    # Burning
    if entity(_player): store(self.temp, getdata(self, 'Fire'))
    if self.burning > 0 or (entity(_player) and self.temp > 0):
        self.takedmg = 5 * self.takeem

        # Shield = 2x less
        if self.shields > 0:
            self.takedmg /= 2

        doFireDMG() # DO FIRE DMG, not reaction DMG
        run('particle minecraft:flame ~ ~0.6 ~ 0.2 0.3 0.2 0 5 normal @a')

        self.burning -= 1


def tick10():
    schedule('10t', tick10)
    execute('as @e[tag=!notmob] at @s', elementEffects10t)

def endermanEffects():
    # Enderman Magnetic effect
    execute('as @a[distance=..2.5]', set(self.takedmg, 5))
    execute('as @a[distance=..2.5]', mult(self.takedmg, self.takeem))
    execute('as @a[distance=..2.5]', set(self.iceS, 1))
    execute('as @a[distance=..2.5]', doElectricDMG)

def entityMods():
    def pillagerMods():
        if entity('@s[tag=firePillager]'):
            run('item replace entity @s weapon.offhand with tipped_arrow[potion_contents={custom_color:16351261,custom_effects:[{id:unluck,duration:20,amplifier:1}]},custom_name=[{"text":"Fire Arrow","italic":false}],lore=[[{"text":"When players are hit:","italic":false,"color":"gray"}],[{"text":"Deal EM Fire DMG","italic":false,"color":"gray"}]]] 3')
        elif entity('@s[tag=icePillager]'):
            run('item replace entity @s weapon.offhand with tipped_arrow[potion_contents={custom_color:65535,custom_effects:[{id:unluck,duration:20,amplifier:2}]},custom_name=[{"text":"Ice Arrow","italic":false}],lore=[[{"text":"When players are hit:","italic":false,"color":"gray"}],[{"text":"Deal EM Ice DMG","italic":false,"color":"gray"}]]] 3')
        elif entity('@s[tag=waterPillager]'):
            run('item replace entity @s weapon.offhand with tipped_arrow[potion_contents={custom_color:255,custom_effects:[{id:unluck,duration:20,amplifier:3}]},custom_name=[{"text":"Water Arrow","italic":false}],lore=[[{"text":"When players are hit:","italic":false,"color":"gray"}],[{"text":"Deal EM Water DMG","italic":false,"color":"gray"}]]] 3')
        elif entity('@s[tag=electricPillager]'):
            run('item replace entity @s weapon.offhand with tipped_arrow[potion_contents={custom_color:16701501,custom_effects:[{id:unluck,duration:20,amplifier:4}]},custom_name=[{"text":"Electric Arrow","italic":false}],lore=[[{"text":"When players are hit:","italic":false,"color":"gray"}],[{"text":"Deal EM Electric DMG","italic":false,"color":"gray"}]]] 3')
        elif entity('@s[tag=naturePillager]'):
            run('item replace entity @s weapon.offhand with tipped_arrow[potion_contents={custom_color:8439583,custom_effects:[{id:unluck,duration:20,amplifier:5}]},custom_name=[{"text":"Nature Arrow","italic":false}],lore=[[{"text":"When players are hit:","italic":false,"color":"gray"}],[{"text":"Deal EM Nature DMG","italic":false,"color":"gray"}]]] 3')

    if entity('@s[type=pillager]'):
        pillagerMods()

def showtimer(timeleft: int):
    run(f'bossbar set timer value {timeleft}')
    run('bossbar set timer name [{"text": "Time left: ", "color":"yellow"},{"score":{"name": "#global", "objective": "timeleftS"}, "color":"green"},{"text":"s","color":"green"}]')

def sec():
    schedule('1s', sec)

    execute('as @e at @s', elementEffects)
    execute('as @e', entityMods)

    kill('@e[type=arrow,nbt={inGround:1b}]')

    # Enderman ice status
    execute('as @e[type=enderman] at @s', endermanEffects)

    def dpscalc():
        # DPS = (Previous + Current) / 2, unless previous is 0 where it uses CURRENT instead.
        if self.dps == 0:
            self.dps = self.dmgdealt
        else:
            self.dps = (self.dps + self.dmgdealt) / 2
        self.dmgdealt = 0

    def healthregen():
        self.health += self.stat.hpregen * self.max_health / 500
        if self.health > self.max_health:
            self.health = self.max_health

    execute('as @a', dpscalc)
    execute('as @a', healthregen)

    # Bossbar 
    timeleft -= 1
    showtimer(timeleft)

    def arenaticks():
        # Player determination
        arenaNumOfPlayers=0
        execute('as @a[distance=..24,gamemode=adventure]', add(arenaNumOfPlayers, 1))
        if started == 1 and arenaNumOfPlayers == 0:
            print(f"#red,b#All players in the arena have died. Game stopped.\n#r,red#You have made it to Floor {level}!")
            stop()

        # Arena mob determination
        numOfMobs = 0
        execute('as @e[distance=..24, type=!player,tag=mob]', add(numOfMobs, 1))
        if started == 1 and waiting == 0:
            if numOfMobs == 0:
                shopphase()

    execute('positioned 8 -60 8', arenaticks)

    execute('positioned 8 4 8', run('item replace entity @a[distance=..30] hotbar.0 with minecraft:spyglass'))

    execute('as @e[type=enderman] at @s', endermanEffects)


def rollFire():
    store(self.rolltemp, getdata(self, 'SelectedItem.components."minecraft:custom_data".Fire'))    
    
    self.rolltemp2 = 0
    if self.rolltemp == 1:
        randint(self.rolltemp, 1, 10000)     
        if self.status >= self.rolltemp:
            self.rolltemp2 = 1
    elif self.rolltemp == 2:
        return 1

    if self.rolltemp2 == 1:
        return 1

    return 0

def rollIce():
    store(self.rolltemp, getdata(self, 'SelectedItem.components."minecraft:custom_data".Ice'))
    
    self.rolltemp2 = 0
    if self.rolltemp == 1:
        randint(self.rolltemp, 1, 10000)        
        if self.status >= self.rolltemp:
            self.rolltemp2 = 1
    elif self.rolltemp == 2:
        return 1

    if self.rolltemp2 == 1:
        return 1

    return 0
def rollWater():
    store(self.rolltemp, getdata(self, 'SelectedItem.components."minecraft:custom_data".Water'))
    
    self.rolltemp2 = 0
    if self.rolltemp == 1:
        randint(self.rolltemp, 1, 10000)        
        if self.status >= self.rolltemp:
            self.rolltemp2 = 1
    elif self.rolltemp == 2:
        return 1

    if self.rolltemp2 == 1:
        return 1

    return 0
def rollElectric():
    store(self.rolltemp, getdata(self, 'SelectedItem.components."minecraft:custom_data".Electric'))
    
    self.rolltemp2 = 0
    if self.rolltemp == 1:
        randint(self.rolltemp, 1, 10000)        
        if self.status >= self.rolltemp:
            self.rolltemp2 = 1
    elif self.rolltemp == 2:
        return 1

    if self.rolltemp2 == 1:
        return 1

    return 0
def rollNature():
    store(self.rolltemp, getdata(self, 'SelectedItem.components."minecraft:custom_data".Nature'))
    
    self.rolltemp2 = 0
    if self.rolltemp == 1:
        randint(self.rolltemp, 1, 10000)        
        if self.status >= self.rolltemp:
            self.rolltemp2 = 1
    elif self.rolltemp == 2:
        return 1

    if self.rolltemp2 == 1:
        return 1

    return 0


def calcCriticals():
    store(self.cr, getdata(self, 'SelectedItem.components."minecraft:custom_data".CR'))

    # Get stat
    self.tempcr = self.stat.cr
    # Ice bonus
    self.tempcr += (2 * _damagedEntity.iceS * self.em)    

    if entity('@s[nbt={Inventory:[{Slot:11b, components:{"minecraft:custom_data":{ModID: "Blessing of the Sea"}}}]}]'):
        self.tempcr += (50 * _damagedEntity.waterS)

    # Calc based on stats
    self.cr *= (100 + self.tempcr)

    # CRIT hit bonus: +25% final
    if self.atk == 3:
        self.cr += 2500

    # Steel Blade
    self.cr += self.cscounter

    # Start CRIT alghorithm
    # Do a /100, and thats how much bonus 100% there is
    self.crittimes = self.cr
    self.crittimes /= 10000
    # Now get remaining CR and test if it worked
    self.cr %= 10000
    randint(self.rolltemp, 1, 10000)    
    tellraw(_debugger, f"#yellow#CRIT RATE: {self.cr} > {self.rolltemp} (Currently have {self.crittimes} crittimes)")
    if self.cr > self.rolltemp:
        self.crittimes += 1

    if self.crittimes > 0:
        if entity('@s[nbt={Inventory:[{Slot:13b, components:{"minecraft:custom_data":{ModID: "Biotic Hits"}}}]}]'):
            randint(self.temp, 0, 9)
            if self.temp < 3: execute('as @n[nbt={HurtTime:10s},tag=!self]', doViral)

        # Get CD
        store(self.cd, getdata(self, 'SelectedItem.components."minecraft:custom_data".CD')) # e.g. 50%
        # CD = WCD + WCD * CD

        self.tempcd = self.stat.cd

        # Frozen bonus
        if _damagedEntity.frozen > 0:
            self.tempcd += 4 * self.em * _damagedEntity.iceS

        # Nature revenge
        if entity('@s[nbt={Inventory:[{Slot:12b, components:{"minecraft:custom_data":{ModID: "Nature\'s Revenge"}}}]}]') and _damagedEntity.nature > 0:
            _damagedEntity.takedmg = 15
            execute('as @n[tag=!self,nbt={HurtTime:10s}]', doNatureDMG)
            # Also grant bonus CD
            self.bonuscd = 15 * _damagedEntity.natureS
            if self.bonuscd > 120:
                self.bonuscd = 120
            self.tempcd += self.bonuscd

        self.cd *= self.crittimes * (100 + self.tempcd) / 100 
        self.cd += 100
        tellraw(_debugger, f"#yellow#CRIT DMG Multiplier: {self.cd}x")
        # Assume, CD = 50%, statCD = 100%
        # 50% += 50% * 100% / 100
        # 50% += 50%
        # 100%, expected result

        # Multiply DMG 
        self.dmg *= self.cd
        self.dmg /= 100

        # Color based on crittimes
        if self.crittimes == 1:
            run('data modify storage kcf:functionargs Color set value "yellow"')
        elif self.crittimes == 2:
            run('data modify storage kcf:functionargs Color set value "gold"')
        else:
            run('data modify storage kcf:functionargs Color set value "red"')

        # Halve Critical Steel counter - even if it is 0, it will still be 0
        self.cscounter /= 2

    else:
        run('data modify storage kcf:functionargs Color set value "white"')
        if entity('@s[nbt={Inventory:[{Slot:11b, components:{"minecraft:custom_data":{ModID: "Steel Blade"}}}]}]'):
            self.cscounter += 2000
# DMG

def doDMG():
    execute('at @s', doFinalDMG)
    # doFinalDMG()
    run('data modify storage kcf:functionargs Color set value "white"')

def defcalc():
    self.tempdefense = self.defense

    # Fire reduction
    self.tempdefense -= self.takeem * self.fireS * 3

    # Corrosive reduction
    if self.corrosion > 0:
        self.tempdefense *= 100 - (45 + self.takeem)
        self.tempdefense /= 100

    # Acidified reduction
    if self.acidified > 0:
        self.tempdefense -= 35 * self.takeem

    # Minimum -100
    if self.tempdefense < -100:
        self.tempdefense = -100

    # Reduction
    self.reduc = 50000 / (self.tempdefense + 500)

    # Can't be 0
    if self.reduc < 1:
        self.reduc = 1

    self.takedmg *= self.reduc
    self.takedmg /= 100

def setshieldcd():
    if entity(_player):        
        self.shieldCD = 40
        self.shieldCD -= self.stat.shieldcd
        if difficulty == 3:
            self.shieldCD += 10
    else:
        self.shieldCD = 50

def calcda():
    # DMG Attenuation
    if self.da.a > 0:
        if self.da.x > self.da.a:
            self.da.reduc = 100 * self.da.a / self.da.x
            self.da.x += (self.takedmg * self.da.reduc / 100)

            if self.da.reduc <= 0:
                self.takedmg = 1
            else:
                self.takedmg *= self.da.reduc
                self.takedmg /= 100
        else:
            self.da.x += self.takedmg
            if self.da.x > self.da.a:
                self.da.reduc = 100 * self.da.a / self.da.x
                self.da.x += (self.takedmg * self.da.reduc / 100)

                if self.da.reduc <= 0:
                    self.takedmg = 1
                else:
                    self.takedmg *= self.da.reduc
                    self.takedmg /= 100

def doFinalDMG():
    setshieldcd()
    
    if entity(_player) and entity("@s[gamemode=creative]"):
        return
    
    # Dodge Chance
    if entity(_player) and not self.invincible > 0:
        randint(self.temp, 1, 100)
        if self.dodge >= self.temp:
            self.invincible += 1
        
    if self.invincible > 0:
        run('data modify storage kcf:functionargs Color set value "dark_gray"')
        run('data modify storage kcf:functionargs takedmg set value 0')
        run('function kcf:displaydmg with storage kcf:functionargs')   

    else:
        # Do SHIELD DMG
        if self.shields > 0:
            run('data modify storage kcf:functionargs Color set value "aqua"')

            # DA
            calcda()

            # Magnetized: 2x dmg
            if self.magnetized > 0:
                self.takedmg *= (10 + 2 * self.takeem)
                self.takedmg /= 10

            # Acidified: 2x Overshields dmg
            if not self.acidified > 0 and self.shields > self.max_shields:
                self.takedmg /= 2


            self.sgduration = 20 * self.shields / self.max_shields
            self.shields -= self.takedmg

            if entity(_player) and entity('@s[nbt={Inventory:[{Slot:15b, components:{"minecraft:custom_data":{ModID: "Electrical Shields"}}}]}]'):
                "@e[type=!player,distance=..2.5,tag=!notmob]".takedmg = 50
                execute('as @e[type=!player,distance=..2.5,tag=!notmob]', doElectricDMG)

            if self.shields <= 0:   # Spider: Instant Die
                if entity('@s[type=spider]'):
                    self.takedmg = self.health
                    doVoidDMG()
                else:
                    if entity(_player):
                        times(self, 2, 10, 5)
                        title(self, f"#aqua#<<                    >>")
                        subtitle(self, "")
                        # Set Invcilibabiltiy
                        # However, max 1s
                        if self.sgduration > 20:
                            self.sgduration = 20

                        if entity('@s[nbt={Inventory:[{Slot:14b, components:{"minecraft:custom_data":{ModID: "Catalyzing Shields"}}}]}]'):
                            self.invincible = 12
                        else:
                            self.invincible = self.sgduration
                                                    
                    self.invincible += 1
                    self.shields = 0

        # DO HEALTH DMG
        else:
            # Evoker: +1000% health DMG
            if entity('@s[type=evoker]'):
                self.takedmg *= 10

            # Reduce defense from EM
            defcalc()

            # DMG Attenuation
            calcda()

            # Viral: Increased health DMG
            if self.viral > 0:
                self.takedmg *= (15 + self.takeem)
                self.takedmg /= 10



            self.health -= self.takedmg
        
            if entity(_player):
                times(self, 2, 5, 5)
                title(self, f"#red#<<                    >>")
                subtitle(self, "") 

        if self.health <= 0:
            dokill()

        if self.takedmg > 0:
            # displaydmg(Symbol, Color, self.takedmg)
            run('execute store result storage kcf:functionargs takedmg int 1 run scoreboard players get @s takedmg')
            run('function kcf:displaydmg with storage kcf:functionargs')   

        if not entity(_player):
            "@a[distance=..7]".dmgdealt += self.takedmg

        tellraw(_debugger, f"Final DMG: {self.takedmg}")
        run('damage @s 0.01')
        showhp()



def doVoidDMG():
    setshieldcd()
    if self.invincible > 0:
        run('data modify storage kcf:functionargs Color set value "dark_gray"')
        run('data modify storage kcf:functionargs takedmg set value 0')
        run('function kcf:displaydmg with storage kcf:functionargs')   
    else:
        # Iron Golem: 90% reduction
        if entity('@s[type=iron_golem]'):
            self.takedmg /= 10
        
        self.health -= self.takedmg

        if self.health <= 0:
            dokill()

        tellraw(_debugger, f"Final DMG: {self.takedmg}")
        if not entity(_player):
            "@a[distance=..10]".dmgdealt += self.takedmg


        run('data modify storage kcf:functionargs Symbol set value "🔮"')
        run('data modify storage kcf:functionargs Color set value "black"')
        if self.takedmg > 0:
            run('execute store result storage kcf:functionargs takedmg int 1 run scoreboard players get @s takedmg')
            run('function kcf:displaydmg with storage kcf:functionargs')

        showhp()



def doHPDMG():
    setshieldcd()

    # Dodge Chance
    if entity(_player):
        randint(self.temp, 1, 100)
        if self.dodge >= self.temp:
            self.invincible += 1

    if self.invincible > 0:
        run('data modify storage kcf:functionargs Color set value "dark_gray"')
        run('data modify storage kcf:functionargs takedmg set value 0')
        run('function kcf:displaydmg with storage kcf:functionargs')   

    else:
        # Spider: 3x more HP DMG
        if entity('@s[type=spider]'):
            self.takedmg *= 3

        ## DEFENSE
        defcalc()

        # DA
        calcda()

        self.health -= self.takedmg

        if self.health <= 0:
            dokill()

        tellraw(_debugger, f"Final DMG: {self.takedmg}")
        if not entity(_player):
            "@a[distance=..10]".dmgdealt += self.takedmg
            
        run('data modify storage kcf:functionargs Symbol set value "♥"')
        run('data modify storage kcf:functionargs Color set value "white"')
        if self.takedmg > 0:
            run('execute store result storage kcf:functionargs takedmg int 1 run scoreboard players get @s takedmg')
            run('function kcf:displaydmg with storage kcf:functionargs')

        showhp()

def showhp():
    if 'entity @s[tag=notmob]': return

    # Calc Health % and Shield %
    self.healthpct = 100 * self.health / self.max_health
    if self.healthpct < 0:
        self.healthpct = 0
    self.shieldpct = 100 * self.shields / self.max_shields


    # Health color changes based on defense
    # <50 (Low): Red
    # <100       
    healthcolor = "#ff0000"

    # If it is not set,
    if not self.tempdefense >= -250:
        defcalc()

    if self.tempdefense >= 1:
        healthcolor = "red"
    if self.tempdefense >= 500:
        healthcolor = "#ff6600"
    if self.tempdefense >= 1000:
        healthcolor = "#ff9900"
    if self.tempdefense >= 2000:
        healthcolor = "#ffcc00"

    displayname(self.level, self.healthpct, self.shieldpct, healthcolor)

def ondeath():
    if started == 1 and self.floor != 0:
        gamemode(self, spectator)

def doReactionDMG():
    # Blaze: 50% reduction
    if entity('@s[type=blaze]'):
        self.takedmg /= 2
    # Gigantic: 2x effectiveness
    if entity('@s[tag=gigantic]'):
        self.takedmg *= 2

    tellraw(_debugger, f"#green#Final REACTION Calc DMG: {self.takedmg}")

    run('data modify storage kcf:functionargs Symbol set value "🧪"')
    doDMG()

def doPhysDMG():

    # Skeleton: 2x effectiveness
    if entity('@s[type=skeleton]'):
        self.takedmg *= 2
    # Gigantic: 50% reduction
    if entity('@s[tag=gigantic]'):
        self.takedmg /= 2
    # Iron Golem: 90% reduction
    if entity('@s[type=iron_golem]'):
        self.takedmg /= 10
    if entity(_player):
        execute('at @s if entity @e[distance=..6,tag=gigantic]', multiply(self.takedmg, 2.5))
        execute('at @s if entity @e[distance=..12,tag=titan]', multiply(self.takedmg, 6))

    tellraw(_debugger, f"#green#Final PHYS Calc DMG: {self.takedmg}")

    run('data modify storage kcf:functionargs Symbol set value "🗡"')
    doDMG()

def doFireDMG():
    self.fire = 60
    self.fireS += 1

    if self.fireS > 10: self.fireS = 10

    # DMG bonuses
    self.takedmg *= (100 + self.take.fire)
    self.takedmg /= 100

    tellraw(_debugger, f"#green#FIRE Calc DMG: {self.takedmg}")

    # Skeleton/Husk: 50% reduction
    if entity('@s[type=skeleton]') or entity('@s[type=husk]'):
        self.takedmg /= 2
    # Fire enemies: 80% reduction
    if entity('@s[tag=fire]'):
        self.takedmg /= 5
    # Stray: 200% more
    if entity('@s[type=stray]'):
        self.takedmg *= 3
    run('data modify storage kcf:functionargs Symbol set value "🔥"')
    doDMG()

def waterburst():
    if entity('@s[type=!player]'):        
        "@e[type=!player,distance=..3]".takeem = self.takeem
        execute('as @e[type=!player,distance=..3]', waterburstdmg)
    else:
        execute('as @a[distance=..3]', waterburstdmg)

    run('particle dolphin ~ ~ ~ 1.5 1.5 1.5 10 100')
def doIceDMG():
    self.ice = 60
    self.iceS += 1

    # DMG bonuses
    self.takedmg *= (100 + self.take.ice)
    self.takedmg /= 100

    tellraw(_debugger, f"#green#ICE Calc DMG: {self.takedmg}")

    # Max 7 stacks
    if self.iceS > 7: self.iceS = 7

    # Enderman/Stray: 80% less
    if entity('@s[tag=ice]'):
        self.takedmg /= 5
    # Husk: 2x effectiveness
    if entity('@s[type=husk]'):
        self.takedmg *= 2

    run('data modify storage kcf:functionargs Symbol set value "❆"')
    doDMG()

def waterburstdmg():
    self.takedmg = 50 * self.takeem
    doWaterDMG()
    run('damage @s 1')

def doWaterDMG():
    self.water = 60
    self.waterS += 1

    # DMG bonuses
    self.takedmg *= (100 + self.take.water)
    self.takedmg /= 100

    tellraw(_debugger, f"#green#WATER Calc DMG: {self.takedmg}")


    # Enderman/Blaze: 200% more
    if entity('@s[type=enderman]') or entity('@s[type=blaze]'):
        self.takedmg *= 3
    # Zombie: 50% reduction
    if entity('@s[type=zombie]'):
        self.takedmg /= 2

    run('data modify storage kcf:functionargs Symbol set value "🌊"')
    doDMG()


    if self.waterS > 4:
        self.waterS = 0
        self.takedmg = 50 * self.takeem
        doWaterDMG()
        run('damage @s 1')
        run('particle dolphin ~ ~ ~ 1.5 1.5 1.5 10 100')


def doElectricDMG():
    self.electric = 60
    self.electricS += 1

    # DMG bonuses
    self.takedmg *= (100 + self.take.electric)
    self.takedmg /= 100

    tellraw(_debugger, f"#green#ELECTRIC Calc DMG: {self.takedmg}")

    # Max 5 stacks
    if self.electricS > 5: 
        self.electricS = 5
        self.electric = 80
    
    run('data modify storage kcf:functionargs Symbol set value "⚡"')
    doDMG()


def doNatureDMG():
    self.nature = 60
    self.natureS += 1
    
    # DMG bonuses
    self.takedmg *= (100 + self.take.nature)
    self.takedmg /= 100

    tellraw(_debugger, f"#green#NATURE Calc DMG: {self.takedmg}")


    run('data modify storage kcf:functionargs Symbol set value "🦠"')
    doDMG()


def doPlayerWeaponDamage():
    # Calculates player DMG for weapon
    # Net DMG = (Base DMG) * (Bonus base DMG | 100)
    if not entity('@s[nbt={Inventory:[{Slot:10b, components:{"minecraft:custom_data":{ModID: "Crispy Hits"}}}]}]'):
        store(self.rawdmg, getdata(self, 'SelectedItem.components."minecraft:custom_data".DMG'))
        self.rawdmg *= (100 + self.stat.dmgbonus)
        self.rawdmg /= 100

        # Increase raw DMG based on player level
        # +10% per level 
        self.rawdmg *= (10 + self.lvl)
        self.rawdmg /= 10

    # Get the status
    store(self.status, getdata(self, 'SelectedItem.components."minecraft:custom_data".Status'))
    self.status *= 100 + self.stat.status # Scaled to 100x. so 10000 = 100%

    # Tag self to not take DMG by self
    tag(self, 'self')

    # Multihit calculation.
    self.tempmultihit = self.multihit

    while self.tempmultihit >= 100:
        calcPlayerWeaponDamage()
        self.tempmultihit -= 100
    
    randint(self.temp, 0, 100)
    if self.tempmultihit >= self.temp:
        calcPlayerWeaponDamage()

    removetag(self, 'self')

def calcPlayerWeaponDamage():
    # Crispy Hits
    if entity('@s[nbt={Inventory:[{Slot:10b, components:{"minecraft:custom_data":{ModID: "Crispy Hits"}}}]}]'):
        store(self.rawdmg, getdata(self, 'SelectedItem.components."minecraft:custom_data".DMG'))
        self.rawdmg *= (100 + self.stat.dmgbonus + (30 * _damagedEntity.iceS))
        self.rawdmg /= 100

        # Increase raw DMG based on player level
        # +10% per level 
        self.rawdmg *= (10 + self.lvl)
        self.rawdmg /= 10

    self.dmg = self.rawdmg
    tellraw(_debugger, f"#aqua#\nInitial DMG: {self.dmg}")

    # Elements
    self.gotamt = 0
    store(self.gotfire, rollFire)
    if self.gotfire == 1: 
        self.gotamt += 1
    store(self.gotice, rollIce)
    if self.gotice == 1: 
        self.gotamt += 1
    store(self.gotwater, rollWater)
    if self.gotwater == 1: 
        self.gotamt += 1
    store(self.gotelectric, rollElectric)
    if self.gotelectric == 1: 
        self.gotamt += 1
    store(self.gotnature, rollNature)
    if self.gotnature == 1: 
        self.gotamt += 1

    # Apply criticals
    calcCriticals()

    _damagedEntity.takedmg = self.dmg
    _damagedEntity.takeem = self.em

    _damagedEntity.take.fire = self.stat.fire
    _damagedEntity.take.ice = self.stat.ice
    _damagedEntity.take.water = self.stat.water
    _damagedEntity.take.electric = self.stat.electric
    _damagedEntity.take.nature = self.stat.nature

    _damagedEntity.take.level = self.lvl

    tellraw(_debugger, f"#aqua#Final Weapon Calc DMG: {self.dmg}")

    if self.gotamt >= 1:
        if self.gotfire == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doFireDMG)
        elif self.gotice == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doIceDMG)
        elif self.gotwater == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doWaterDMG)
        elif self.gotelectric == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doElectricDMG)
        elif self.gotnature == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doNatureDMG)

    else:
        execute('as @n[nbt={HurtTime:10s},tag=!self]', doPhysDMG)


def displayname(level: int, healthpct: int, shieldpct: int, healthcolor: int):
    # run(f'data modify entity @s CustomName set value [{{"text":"⭐{level}","color":"yellow"}},{{"color":"gray","text":" | "}},{{"color":"{healthcolor}","text":"♥{healthpct}%"}},{{"color":"gray","text":" | "}},{{"color":"blue","text":"⛊{shieldpct}%"}}]')
    run(f'data merge entity @s {{CustomNameVisible:1b, CustomName: [{{"text":"⭐{level}","color":"yellow"}},{{"color":"gray","text":" | "}},{{"color":"{healthcolor}","text":"♥{healthpct}%"}},{{"color":"gray","text":" | "}},{{"color":"blue","text":"⛊{shieldpct}%"}}]}}')

def applyElectrified():
    self.electrified += 4
    if self.electrified > 12:
        self.electrified = 12

def doViral():
    # VIRAL
    self.viral += 4
    if self.viral > 12: self.viral = 12
    displayreaction({"Name": '"☣ Viral"', "Color": '"#16bf8b"'})

def genericEntityTick():
    # Generic shields and stuff
    if tag('aggroqueue'):
        run('damage @s 0.00001 player_attack by @r')
        removetag(self, 'aggroqueue')
        run('data modify entity @s Slient set value 0b')

    if entity('@s[tag=!done]') and entity('@s[type=!#minecraft:impact_projectiles]'):
        onnewentity()

    if entity('@s[type=bee,nbt={HasStung:1b}]'):
        run('data modify entity @s AngerTime set value 600')
        run('data modify entity @s HasStung set value 0b')

    if self.invincible > 0:
        self.invincible -= 1

    # Damage Attenuation
    if self.da.a > 0 and self.da.x > 0:
        self.da.x *= 0.98

        if self.da.x < 0: self.da.x = 0

    # Regen shield
    if not self.water > 0 and not self.magnetized > 0:
        if self.shields < self.max_shields and self.shieldCD <= 0:
            if entity(_player):
                self.addshields = self.max_shields / 100

                self.addshields *= (100 + self.stat.shieldregen)
                self.addshields /= 100

                self.shields += self.addshields

                if self.shields > self.max_shields:
                    self.shields = self.max_shields
            else:
                self.shields += self.max_shields / 100
                if self.shields > self.max_shields:
                    self.shields = self.max_shields
                showhp()

    if self.shieldCD > 0 and not self.magnetized > 0:
        self.shieldCD -= 1

    # Take DMG
    if 'entity @s[nbt={HurtTime:10s}]' or self.dmgtaken > 0:

        # Get the amount of damage dealt.
        # The amount of DMG dealt should be scaled, which will produce Physical DMG
        # This uses LIENAR scaling: where X is DMG: 50 * X
        # Only activate if DMG taken is above 1

        if not entity(_player):
            # To calc DMG taken, we can use Health.
            # Mobs don't have RES but they have 1024 HP
            store(self.hp, getdata(self, 'Health', 10)) # Scale by 10x to catch decimals
            # BUGFIX: HP is 0 when dead, and this is still ran
            # Of course, this bugfix adds another edge case: damages that one shot will not be shown.
            if self.hp > 0:
                self.dmgtaken = 10240 - self.hp
            else:
                self.dmgtaken = 0

        if self.dmgtaken > 2:                
            self.takedmg = 2 * self.dmgtaken

            if entity(_player):
                # (Base * (Level^2/100 + 1))
                self.takedmg *= level * level + (10 * level) + 100
                self.takedmg /= 100

                # Easy Difficulty
                if difficulty == 1:
                    self.takedmg /= 2
                # Hard Difficulty
                if difficulty == 3:
                    self.takedmg *= 3

            doPhysDMG()
        
        # Heal
        if not entity(_player):
            if self.health > 0:
                run('data modify entity @s Health set value 1024')
        else:
            self.dmgtaken = 0

        # Electric
        if self.electric > 0 and not entity('@s[tag=electric]'):
            self.takedmg = 2 * self.takeem * self.electricS
            if self.shields > 0:
                self.takedmg *= 2
            doReactionDMG()
            # Spread
            if entity(_player):
                "@a[distance=1.1..2.5]".takedmg = self.takedmg
                execute('as @a[distance=1.1..2.5]', doReactionDMG)
            else:
                "@e[type=!player,tag=!notmob,distance=1.1..2.5]".takedmg = self.takedmg
                execute('as @e[type=!player,tag=!notmob,distance=1.1..2.5]', doReactionDMG)
        # Water
        if self.water > 0 and not entity('@s[tag=water]'):
            # IF MOB
            if entity('@s[type=!player]'):
                "@a[distance=..4]".health += self.takeem * self.waterS / 5
                self.health += self.takeem / 5 * 2
            else:
                "@e[type=!player,distance=..4]".health += self.takeem * self.waterS
                self.health += self.takeem / 5

        setshieldcd()
        showhp()

        # Fix duplicate bug
        if not entity(_player):
            self.dmgtaken = 0


    # Reactions, in order

    if self.fireS > 0:
        # First does not need fireS but others do
        if self.iceS > 0:
            # BLAST
            # Deals 75EM to within 3m
            if entity(_player):
                "@a[distance=..3]".takedmg = 75*self.takeem
                execute('as @a[distance=..3]', doReactionDMG)

                "@e[type=!player,distance=..3]".takedmg = 15*self.takeem
                execute('as @e[type=!player,distance=..3]', doReactionDMG)

            else:
                "@e[type=!player,distance=..3]".takedmg = 75*self.takeem
                execute('as @e[type=!player,distance=..3]', doReactionDMG)

                "@a[distance=..3]".takedmg = 15*self.takeem
                execute('as @a[distance=..3]', doReactionDMG)

            displayreaction({"Name": '"💥 Blast"', "Color": '"#ff0099"'})

            # Create explosion sound
            run('playsound minecraft:entity.generic.explode player @a')

            run('particle explosion_emitter ~ ~1.2 ~ 0.2 0.1 0.2 0 1 normal @a')

            # Remove frozen
            self.frozen = 1

            # Remove a stack
            self.iceS -= 1; self.fireS -= 1

        if self.fireS > 0 and self.waterS > 0:
            # VAPORIZE
            self.takedmg = 100*self.takeem

            # 50% less effective against shields
            if self.shields > 0:
                self.takedmg /= 2

            # Reduce burning time
            self.burning -= 6

            doReactionDMG()
            displayreaction({"Name": '"🌫 Vaporize"', "Color": '"#aaaaaa"'})

            run('particle minecraft:smoke ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')

            # Remove a stack
            self.waterS -= 1; self.fireS -= 1

        if self.fireS > 0 and self.electricS > 0:
            # RADIATION
            self.takedmg = 20 *self.takeem

            doVoidDMG()
            displayreaction({"Name": '"☢ Radiation"', "Color": '"#00ee00"'})

            # Remove a stack
            self.electricS -= 1; self.fireS -= 1


    if self.iceS > 0 and self.electricS > 0:
        # MAGENTIZE
        self.magnetized += 80 
        if self.magnetized > 240: self.magnetized = 240

        # DMG
        self.takedmg = 30 * self.takeem * self.electricS
        doReactionDMG()

        displayreaction({"Name": '"🧲 Magnetized"', "Color": '"#dda3ff"'})

        # Remove a stack
        self.iceS -= 1; self.electricS = 0

    if self.waterS > 0:
        if self.iceS > 0:
            # FREEZE
            self.frozen += 60
            if self.frozen > 160: self.frozen = 160
            displayreaction({"Name": '"🧊 Freeze"', "Color": '"aqua"'})

            # Remove a stack. Ice is kept
            self.waterS -= 1

        if self.waterS > 0 and self.electricS > 0:
            # ELECTIRIFED
            if entity(_player):
                execute('as @a[distance=..2.5]', applyElectrified)
            else:
                execute('as @e[type=!player,distance=..2.5]', applyElectrified)

            displayreaction({"Name": '"⚡ Electrified"', "Color": '"#FFFF00"'})

            # Remove a stack
            self.electricS -= 1; self.waterS -= 1

        if self.waterS > 0 and self.natureS > 0:
            # Bloom

            # Get amount of bloom cores
            self.temp = 0
            execute('at @e[type=slime,distance=..4,tag=bloomCore]', add(self.temp, 1))
            if self.temp >= 4:
                execute('as @e[type=slime,distance=..4,sort=random,limit=1,tag=bloomCore] at @s', explodeBloom)

            run('summon slime ~ ~ ~ {CustomNameVisible:1b,NoAI:1b,Health:1024f,Size:0,Tags:["bloomCore","notmob","notdone"],CustomName:"Bloom Core",attributes:[{id:"minecraft:max_health",base:1024}]}')

            execute('at @s as @n[type=slime,tag=bloomCore,tag=notdone]', (
                # Set own stats
                set(self.em, nearest.takeem),
                set(self.stat.nature, nearest.take.nature),
                set(self.level, nearest.take.level),
                removetag(self, 'notdone')
            ))

            displayreaction({"Name": '"🧪 Bloom"', "Color": '"green"'})

            # Remove a stack
            self.waterS -= 1; self.natureS -= 1

    if self.natureS > 0:
        if self.fireS > 0:
            # BURNING
            self.burning += 6 # loses 1 per tick, so 3 / 0.5 = 6
            if self.burning > 16: self.burning = 16
            displayreaction({"Name": '"🔥 Burning"', "Color": '"gold"'})
            # Remove a stack
            self.fireS -= 1; self.natureS -= 1

        if self.natureS > 0 and self.iceS > 0:
            doViral()
            # Remove a stack
            self.iceS -= 1; self.natureS -= 1

        if self.natureS > 0 and self.electricS > 0:
            # Corrosive 
            self.corrosion += 100 

            # DMG
            self.takedmg = 10 * self.takeem * self.natureS
            doHPDMG()

            displayreaction({"Name": '"🍾 Corrosion"', "Color": '"#014c00"'})
            # Remove all stacks
            self.natureS = 0; self.electricS = 0

# Elements
    if self.fire > 0:
        self.fire -= 1

        if self.fire <= 0:            
            self.fireS -= 1
            if self.fireS > 0:
                self.fire = 10
        run('particle minecraft:flame ~ ~0.6 ~ 0.2 0.3 0.2 0 5 normal @a')
    if self.ice > 0:
        self.ice -= 1
        if self.ice <= 0:            
            self.iceS -= 1
            if self.iceS > 0:
                self.ice = 10
        run('particle minecraft:snowflake ~ ~1 ~ 0.2 0.1 0.2 0 5 normal @a')
    if self.water > 0:
        self.water -= 1
        if self.water <= 0:
            self.waterS -= 1
            if self.waterS > 0:
                self.water = 10

        run('particle minecraft:block_crumble{block_state:"water"} ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')
    if self.electric > 0:
        self.electric -= 1
        if self.electric <= 0:             
            self.electricS -= 1
            if self.electricS > 0:
                self.electric = 10

        run('particle minecraft:electric_spark ~ ~1 ~ 0.2 0.1 0.2 0 5 normal @a')
    if self.nature > 0:
        self.nature -= 1
        if self.nature <= 0: 
            self.natureS -= 1
            if self.natureS > 0:
                self.nature = 10

        run('particle minecraft:block_crumble{block_state:"oak_leaves"} ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')


    ## REACTION TICKS

    # Magnetic status
    if self.magnetized > 0:
        self.magnetized -= 1
        if entity(_player) and entity('@s[nbt={Inventory:[{Slot:15b, components:{"minecraft:custom_data":{ModID: "Electrical Shields"}}}]}]'):
            self.magnetized -= 1
        run('particle minecraft:firework ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')

    if self.acidified > 0:
        self.acidified -= 1
        run('particle minecraft:falling_spore_blossom ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')

    if self.electrified > 0:
        run('particle minecraft:enchanted_hit ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')

    if self.viral > 0:
        run('particle minecraft:spore_blossom_air ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')
    
    if self.corrosion > 0:
        self.corrosion -= 1
        run('particle minecraft:warped_spore ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')

    # Frozen
    if self.frozen > 0:
        if entity(_player):
            pass

        else:
            if self.frozen == 1:
                run('data modify entity @s NoAI set value 0b')
            elif entity('@s[tag=!nofreeze]'):
                run('data modify entity @s NoAI set value 1b')

                # When NoAI, entity does not get affected by gravity. 
                # This also makes Freeze for something like PHANTOMS OP
                if block('~ ~-0.2 ~', air):
                    run('tp @s ~ ~-0.2 ~')

        # Particles
        run('particle minecraft:block_crumble{block_state:"packed_ice"} ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')

        self.frozen -= 1

    # Remove element if no stack
    if self.fireS <= 0: self.fire = 0
    if self.iceS <= 0: self.ice = 0
    if self.waterS <= 0: self.water = 0
    if self.electricS <= 0: self.electric = 0
    if self.natureS <= 0: self.nature = 0

    if self.health > self.max_health:
        self.health = self.max_health

    if entity('@s[type=evoker_fangs,nbt={Warmup:-9}]'):
        execute('as @e[type=!evoker,type=!evoker_fangs,tag=!notmob,type=!vex,distance=..1.5]', (
            set(self.takedmg, 50),
            set(self.electricS, 1),
            multiply(self.takedmg, self.takeem),
            doNatureDMG()
        ))

def bloom():
    # Intended for use by the player running the command
    self.temp = 0
    execute('at @e[type=slime,distance=..4,tag=bloomCore]', add(self.temp, 1))
    if self.temp >= 4:
        execute('as @e[type=slime,distance=..4,sort=random,limit=1,tag=bloomCore]', explodeBloom)

    run('summon slime ~ ~ ~ {CustomNameVisible:1b,NoAI:1b,Health:1024f,Size:0,Tags:["bloomCore","notmob","notdone"],CustomName:"Bloom Core",attributes:[{id:"minecraft:max_health",base:1024}]}')

    execute('as @n[type=slime,tag=bloomCore,tag=notdone]', (
        # Set own stats
        set(self.em, '@p'.em),
        set(self.stat.nature, '@p'.stat.nature),
        set(self.level, '@p'.lvl),
        removetag(self, 'notdone')
    ))

def explodeBloom():
    run('particle minecraft:explosion')
    # Calculate DMG
    # EM * (1 + LVL / 10) * (1 + DMG Bonus)
    self.dmg = 100 # Base DMG
    self.dmg *= self.em
    self.dmg *= (10 + self.level) # x10
    self.dmg *= (100 + self.stat.nature) # x100
    self.dmg /= 1000 # Cancel x10 x100


    # Set takedmg
    "@e[tag=!notmob,distance=..3.5]".takedmg = self.dmg

    # 90% less for players
    "@a[distance=..3.5]".takedmg = 10

    execute('as @e[tag=!notmob,distance=..3.5]', doReactionDMG)
    
    # Kill bloom core
    if entity('@s[tag=bloomCore]'):
        tp(self, '0 0 0'); kill(self)

def bloomCoreTick():
    if entity('@s[tag=hyperbloom]'):
        # If no mobs exists, kill
        if not entity('@e[tag=mob,distance=..15]'):
            kill(self)

        # Track
        execute('facing entity @n[tag=mob] feet', tp(self, '^ ^ ^0.5 ~ ~'))

        # Particle
        run('particle glow ~ ~0.5 ~ 0.1 0.1 0.1 0 20')

        execute('as @e[tag=mob,distance=..1]', (
            # Do DMG
            set(self.takedmg, '@n[type=marker,tag=notdone,tag=hyperbloom]'.dmg),
            run('particle block{block_state:"oak_leaves"} ~ ~0.9 ~ 0.1 0.3 0.1 0 100'),
            doReactionDMG(),
            kill('@n[type=marker,tag=notdone,tag=hyperbloom]'),
        ))

    else:
        if self.fireS > 0:
            # Burgeon
            # We can multiply EM by 2 to achieve 2x more DMG
            self.em *= 2
            explodeBloom()
            displayreaction({"Name": '"Burgeon"', "Color": '"gold"'})
        if self.electricS > 0:
            # Hyperbloom
            # Precalculate the DMG and store it to the new hyperbloom projectile
            self.dmg = 300 # Base DMG, x3
            self.dmg *= self.em
            self.dmg *= (10 + self.level) # x10
            self.dmg *= (100 + self.stat.nature) # x100
            self.dmg /= 1000 # Cancel x10 x100

            displayreaction({"Name": '"Hyperbloom"', "Color": '"#8800FF"'})

            summon(marker, '~ ~ ~', {"Tags": "[notmob, hyperbloom, bloomCore, notdone]"}) # Still use bloom core for ticking
            # Copy DMG
            '@n[type=marker,tag=notdone,tag=hyperbloom]'.dmg = self.dmg

            tp(self, '0 0 0'); kill(self)


    # Explode after 4s. That includes hyperbloom as well (only way hyperbloom projectile explodes)
    self.life += 1
    if self.life >= 80:
        explodeBloom()

def onnewentity():
    tag(self, 'done')
    tag(self, 'mob')
    if entity('@s[type=item]'):
        if entity('@s[nbt={Item:{components:{"minecraft:custom_data":{Useless:1}}}}]'): 
            kill(self)
        elif 'data entity @s Thrower':
            run('data modify entity @s Age set value 5800')

        removetag(self, 'mob')
        tag(self, 'notmob')
        run('data modify entity @s CustomNameVisible set value 1b')

    elif entity('@s[type = zombie]'):
        self.max_health = 750
        self.defense = 800
        self.max_shields = 0
    elif entity('@s[type = husk]'):
        self.max_health = 700
        self.defense = 1000
        self.max_shields = 0
    elif entity('@s[type = skeleton]'):
        self.max_health = 500
        self.defense = 20
        self.max_shields = 1000
        run('item replace entity @s weapon.mainhand with bow[enchantments={unbreaking:3}]')
    elif entity('@s[type = pillager]'):
        self.max_health = 450
        self.defense = 350
        self.max_shields = 200
        if entity('@s[tag=!pillagerDone]'):
            randint(self.temp, 0, 4)
            if self.temp == 0: tag(self, 'firePillager')
            if self.temp == 1: tag(self, 'icePillager')
            if self.temp == 2: tag(self, 'waterPillager')
            if self.temp == 3: tag(self, 'electricPillager')
            if self.temp == 4: tag(self, 'naturePillager')
            tag(self, 'pillagerDone')

            randint(self.temp, 0, 1)
            if self.temp == 0:
                run('item replace entity @s weapon.mainhand with crossbow[unbreakable={},enchantments={multishot:1,piercing:5}]')
            else:
                run('item replace entity @s weapon.mainhand with crossbow[unbreakable={},enchantments={piercing:5,quick_charge:5}]')

    elif entity('@s[type = vindicator]'):
        self.max_health = 500
        self.defense = 500
        self.max_shields = 250
    elif entity('@s[type = evoker]'):
        self.max_health = 6250
        self.defense = 200
        self.max_shields = 850
        self.da.a = 2000
        attribute(self, scale, 1.25)
    elif entity('@s[type = iron_golem]'):
        self.max_health = 800
        self.defense = 1500
        self.max_shields = 3000
        self.da.a = 2000
        tag(self, 'electric')
    elif entity('@s[type = spider]'):
        self.max_health = 50
        self.defense = 0
        self.max_shields = 150
        self.da.a = 100
        attribute(self, scale, 0.25)
        if entity('@s[tag=!child]'):
            for i in range(4):
                summon(spider, '~ ~ ~', {'Tags': '[child]'})
    elif entity('@s[type = stray]'):
        self.max_health = 650
        self.defense = 400
        self.max_shields = 1000
        tag(self, 'nofreeze')
        tag(self, 'icePillager')
        tag(self, 'ice')
        run('item replace entity @s weapon.mainhand with bow[enchantments={unbreaking:3,power:2}]')
        run('item replace entity @s weapon.offhand with tipped_arrow[potion_contents={custom_color:65535,custom_effects:[{id:unluck,duration:20,amplifier:6}]},custom_name=[{"text":"Stray Ice Arrow","italic":false}],lore=[[{"text":"When players are hit:","italic":false,"color":"gray"}],[{"text":"Deal 50 * EM Ice DMG with 3 stacks","italic":false,"color":"gray"}]]] 3')
    elif entity('@s[type = bogged]'):
        self.max_health = 750
        self.defense = 500
        self.max_shields = 1000
        tag(self, 'naturePillager')
        tag(self, 'nature')
        run('item replace entity @s weapon.mainhand with bow[enchantments={unbreaking:3,power:2}]')
        run('item replace entity @s weapon.offhand with tipped_arrow[potion_contents={custom_color:8439583,custom_effects:[{id:unluck,duration:20,amplifier:5}]},custom_name=[{"text":"Nature Arrow","italic":false}],lore=[[{"text":"When players are hit:","italic":false,"color":"gray"}],[{"text":"Deal EM Nature DMG","italic":false,"color":"gray"}]]] 3')
    elif entity('@s[type = ravager]'):
        self.max_health = 1500
        self.defense = 1000
        self.max_shields = 500
        self.da.a = 1000

    elif entity('@s[type = enderman]'):
        self.max_health = 600
        self.defense = 200
        self.max_shields = 1200
        tag(self, 'ice')
    elif entity('@s[type = blaze]'):
        self.max_health = 450
        self.defense = 700
        self.max_shields = 600
        tag(self, 'fire')
    elif entity('@s[type = villager]'):
        self.max_health = 2147483647
        self.defense = 0
        self.max_shields = 0
        run('data modify entity @s NoAI set value 1b')
    elif entity('@s[type = phantom]'):
        self.max_health = 300
        self.defense = 20
        self.max_shields = 500
    elif entity('@s[type = bee]'):
        self.max_health = 200
        self.defense = 300
        self.max_shields = 300
        self.da.a = 100
        tag(self, 'nature')

        run('attribute @s minecraft:scale modifier add bee 1 add_multiplied_total ')
        run('attribute @s minecraft:attack_damage modifier add beeatk 1.5 add_multiplied_total ')

    else:
        removetag(self, 'mob')

        store(self.max_health, run('attribute @s max_health get 25'))
        store(self.max_shields, run('attribute @s max_health get 25'))

        store(self.temp, run('attribute @s attack_damage get 25'))
        self.max_shields += self.temp


        store(self.defense, run('attribute @s armor get 50'))
        self.defense += 200

    # Gigantic!
    if entity('@s[tag=gigantic]'):
        run('attribute @s minecraft:scale modifier add gigantic 1 add_multiplied_total ')
        run('attribute @s minecraft:movement_speed modifier add titan 0.5 add_multiplied_total ')
        run('attribute @s minecraft:attack_damage modifier add titan 1 add_multiplied_total ')
        self.defense *= 2
        self.max_health *= 2.5
        self.max_shields *= 2.5

    # Titan!
    if entity('@s[tag=titan]'):
        run('attribute @s minecraft:movement_speed modifier add titan 2 add_multiplied_total ')
        run('attribute @s minecraft:scale modifier add titan 1 add_multiplied_total ')
        run('attribute @s minecraft:attack_damage modifier add titan 4 add_multiplied_total ')
        self.defense *= 5
        self.max_health *= 5
        self.max_shields *= 5

    # Difficulty modifiers
    if difficulty == 1: # Easy
        self.defense *= 0.75
        self.max_health /= 2
        self.max_shields /= 2
    elif difficulty == 3: # Hard
        self.defense *= 4
        self.defense /= 3
        self.max_health *= 1.5
        self.max_shields *= 2
        run('effect give @s minecraft:speed infinite 1 true')

    # Level system! Increase base stats per level
    self.level = level
    self.increase = (35 + self.level * self.level + (7 * self.level))

    # Damage Attenuation
    if self.da.a > 0:
        tag(self, 'da')
        self.da.a *= self.increase
        self.da.a /= 35

    if not entity('@s[type = villager]'):
        self.max_health *= self.increase
        self.max_health /= 35
        self.max_shields *= (100 + self.level * self.level * self.level + (10 * self.level))
        self.max_shields /= 100
        self.defense *= self.increase
        self.defense /= 100

    store(self.em, run('attribute @s attack_damage get'))
    self.takeem = 5

    # HP
    attribute(self, max_health, 1024)
    run('data modify entity @s Health set value 1024')
    self.health = self.max_health
    self.shields = self.max_shields

    # No KB
    attribute(self, knockback_resistance, 0.9)

    # Add to mob team to prevent attacking each other
    run('team join mob @s')

    # If the game has started, try to aggro
    if started == 1:
        tag(self, 'aggroqueue')
        run('data modify entity @s Slient set value 1b')

def onjoin():
    if self.gameiter != gameiter:
        run('clear @s')
    self.invincible = 20

    # Determine continue
    numOfPlayers: int
    getplayers(numOfPlayers)
    if numOfPlayers == 1 and self.floor != 0:
        print(f'#aqua#It looks like you had an ongoing session, being in floor {self.floor}!\nYou can continue (due to being in singleplayer) by clicking {"here": run(trigger continue) | u,yellow}')
    else:
        self.floor = 0


def onnewjoin():
    tag(self, 'done')
    tag(self, 'mob')

    self.max_health = 500
    self.max_shields = 500
    self.em = 5
    self.takeem = 5

    attribute(self, max_health, 6)
    attribute(self, knockback_resistance, 0.75)
    onrespawn()

def playertick():
    if self.atk > 0:
        if 'score @s atk matches 2..3':
            execute('at @s', doPlayerWeaponDamage)

        elif self.atk >= 10240:
            tellraw(self, f"#b,red#OVERKILL!!!")

        self.atk = 0

    # Health
    if self.invincible > 0:
        actionbar(self, f"#dark_gray#Health: {self.health}/{self.max_health}#gray# | #dark_gray#Shields: #dark_gray#{self.shields: var | dark_gray}#dark_gray#/{self.max_shields: var | dark_gray}#gray# | #gold#DPS: {self.dps: var | gold}")
    else:
        actionbar(self, f"#red#Health: {self.health: var | red}#red#/{self.max_health: var | red}#gray# | #aqua#Shields: #aqua#{self.shields: var | aqua}#aqua#/{self.max_shields: var | aqua}#gray# | #gold#DPS: {self.dps: var | gold}")

    # Element Effects
    if entity('@s[nbt={active_effects:[{id:"minecraft:unluck"}]}]'):
        self.takedmg = self.takeem
        if entity('@s[nbt={active_effects:[{id:"minecraft:unluck", amplifier: 1b}]}]'):
            doFireDMG()
        elif entity('@s[nbt={active_effects:[{id:"minecraft:unluck", amplifier: 2b}]}]'):
            doIceDMG()
        elif entity('@s[nbt={active_effects:[{id:"minecraft:unluck", amplifier: 3b}]}]'):
            doWaterDMG()
        elif entity('@s[nbt={active_effects:[{id:"minecraft:unluck", amplifier: 4b}]}]'):
            doElectricDMG()
        elif entity('@s[nbt={active_effects:[{id:"minecraft:unluck", amplifier: 5b}]}]'):
            doNatureDMG()
        elif entity('@s[nbt={active_effects:[{id:"minecraft:unluck", amplifier: 6b}]}]'):
            self.takedmg = 50
            self.takedmg *= self.takeem
            doIceDMG()
            self.iceS += 2
        cleareffect(self, unluck)

    # Pickups
    if entity('@s[nbt={Inventory:[{id:"minecraft:leather_horse_armor",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:leather_horse_armor[minecraft:custom_data={GetRelic:1}] 1')
        bronzerelic()
    if entity('@s[nbt={Inventory:[{id:"minecraft:iron_horse_armor",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:iron_horse_armor[minecraft:custom_data={GetRelic:1}] 1')
        silverrelic()
    if entity('@s[nbt={Inventory:[{id:"minecraft:golden_horse_armor",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:golden_horse_armor[minecraft:custom_data={GetRelic:1}] 1')
        goldrelic()
    if entity('@s[nbt={Inventory:[{id:"minecraft:diamond_horse_armor",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:diamond_horse_armor[minecraft:custom_data={GetRelic:1}] 1')
        diamondrelic()
    if entity('@s[nbt={Inventory:[{id:"minecraft:white_tulip",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:white_tulip[minecraft:custom_data={GetRelic:1}] 1')
        bronzeartifact()
    if entity('@s[nbt={Inventory:[{id:"minecraft:orange_tulip",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:orange_tulip[minecraft:custom_data={GetRelic:1}] 1')
        silverartifact()
    if entity('@s[nbt={Inventory:[{id:"minecraft:red_tulip",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:red_tulip[minecraft:custom_data={GetRelic:1}] 1')
        goldartifact()
    if entity('@s[nbt={Inventory:[{id:"minecraft:pink_tulip",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:pink_tulip[minecraft:custom_data={GetRelic:1}] 1')
        diamondartifact()
    if entity('@s[nbt={Inventory:[{id:"minecraft:blade_pottery_sherd",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:blade_pottery_sherd[minecraft:custom_data={GetRelic:1}] 1')
        commonmod()
    if entity('@s[nbt={Inventory:[{id:"minecraft:flow_pottery_sherd",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:flow_pottery_sherd[minecraft:custom_data={GetRelic:1}] 1')
        uncommonmod()
    if entity('@s[nbt={Inventory:[{id:"minecraft:prize_pottery_sherd",components:{"minecraft:custom_data":{GetRelic:1}}}]}]'):
        run('clear @s minecraft:prize_pottery_sherd[minecraft:custom_data={GetRelic:1}] 1')
        raremod()


    if entity('@s[nbt={Inventory:[{id:"minecraft:sunflower"}]}]'):
        store(self.temp, run('clear @s sunflower 0'))
        self.coins += self.temp
        tellraw(self, f'#gold#+{self.temp} Coin(s) (Picking up Coins)')
        run('clear @s sunflower')

def onfuncs():
    execute('at @s', playertick)

def dmgtextanimation():
    self.time += 1

    # Let's be smart about our IF statements and use a binsearch like way to reduce lag
    # Without any external if statement, it runs: 10 + 5 + 1lines of code per function: 16 operations per function

    if self.time <= 5:
        if self.time == 5: run('data modify entity @s text_opacity set value -1')
        if self.time == 4: run('data modify entity @s text_opacity set value -64')
        if self.time == 3: run('data modify entity @s text_opacity set value -128')
        if self.time == 2: run('data modify entity @s text_opacity set value 64')
        if self.time == 1: run('data modify entity @s text_opacity set value 16')
    if 31 <= self.time <= 35:
        if self.time == 31: run('data modify entity @s text_opacity set value -1')
        if self.time == 32: run('data modify entity @s text_opacity set value -32')
        if self.time == 33: run('data modify entity @s text_opacity set value -64')
        if self.time == 34: run('data modify entity @s text_opacity set value -96')
        if self.time == 35: run('data modify entity @s text_opacity set value -128')
    if self.time >= 36:
        if self.time == 36: run('data modify entity @s text_opacity set value 96')
        if self.time == 37: run('data modify entity @s text_opacity set value 64')
        if self.time == 38: run('data modify entity @s text_opacity set value 32')
        if self.time == 39: run('data modify entity @s text_opacity set value 16')
        if self.time == 40: 
            textdisplays -= 1
            kill(self)

    # Now, it runs 3 + 5 + 1 operations = ~9 operations per function
    # I don't use ELIF because ELIF uses a complex system and there is only 3 IF statements on the outside

def ww():                   
    execute('as @e[type=!player,distance=..16,tag=!notmob] at @s facing entity @n[tag=ww] feet', run('tp @s ^ ^ ^0.05'))
    execute('as @e[type=!player,distance=..12,tag=!notmob] at @s facing entity @n[tag=ww] feet', run('tp @s ^ ^ ^0.05'))
    execute('as @e[type=!player,distance=..10,tag=!notmob] at @s facing entity @n[tag=ww] feet', run('tp @s ^ ^ ^0.05'))
    execute('as @e[type=!player,distance=..8,tag=!notmob] at @s facing entity @n[tag=ww] feet',  run('tp @s ^ ^ ^0.05'))
    execute('as @e[type=!player,distance=..6,tag=!notmob] at @s facing entity @n[tag=ww] feet',  run('tp @s ^ ^ ^0.05'))
    execute('as @e[type=!player,distance=..5,tag=!notmob] at @s facing entity @n[tag=ww] feet',  run('tp @s ^ ^ ^0.05'))
    execute('as @e[type=!player,distance=..4,tag=!notmob] at @s facing entity @n[tag=ww] feet',  run('tp @s ^ ^ ^0.05'))
    execute('as @e[type=!player,distance=..2,tag=!notmob] at @s facing entity @n[tag=ww] feet',  run('tp @s ^ ^ ^0.05'))
    self.time += 1

    execute('as @e[type=!player,distance=..5,tag=!notmob]', run('data modify entity @s Gravity set value 0b'))
    execute('as @e[type=!player,distance=5.1..10,tag=!notmob]', run('data modify entity @s Gravity set value 1b'))


    if self.time > 10000:
        execute('as @e[type=!player,distance=..5,tag=!notmob]', run('data modify entity @s Gravity set value 1b'))
        kill(self)

    run('particle minecraft:glow_squid_ink ~ ~ ~ 1 1 1 0 3')

def summonww():
    summon(marker, '~ ~ ~', {'Tags': '[ww, notmob]'})

""" RELICS """
def applystats(lvl1: int, lvl2: int, lvl3: int):
    # selector: relic
    for i in range(self.times):
        # Random Stat
        randint('self.stat', 0, 11)
        if self.stat == 0:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl1}% Base DMG", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-BaseDMG'))
            run(f'scoreboard players add @s temp {lvl1}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-BaseDMG int 1 run scoreboard players get @s temp')
        elif self.stat == 1:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}% Critical Chance", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-CR'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-CR int 1 run scoreboard players get @s temp')
        elif self.stat == 2:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}% Critical Damage", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-CD'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-CD int 1 run scoreboard players get @s temp')
        elif self.stat == 3:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl3} Elemental Mastery", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-EM'))
            run(f'scoreboard players add @s temp {lvl3}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-EM int 1 run scoreboard players get @s temp')
        elif self.stat == 4:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl1}% Attack Speed", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-ATKSPD'))
            run(f'scoreboard players add @s temp {lvl1}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-ATKSPD int 1 run scoreboard players get @s temp')
        elif self.stat == 5:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl1}% Status Chance", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Status'))
            run(f'scoreboard players add @s temp {lvl1}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Status int 1 run scoreboard players get @s temp')
        elif self.stat == 6:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}% Fire DMG Bonus", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Fire'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Fire int 1 run scoreboard players get @s temp')
        elif self.stat == 7:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}% Ice DMG Bonus", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Ice'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Ice int 1 run scoreboard players get @s temp')
        elif self.stat == 8:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}% Water DMG Bonus", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Water'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".Water int 1 run scoreboard players get @s temp')
        elif self.stat == 9:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}% Electric DMG Bonus", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Electric'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Electric int 1 run scoreboard players get @s temp')
        elif self.stat == 10:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}% Nature DMG Bonus", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Nature'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Nature int 1 run scoreboard players get @s temp')
        elif self.stat == 11:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl1}% Multihit", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Multihit'))
            run(f'scoreboard players add @s temp {lvl1}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Multihit int 1 run scoreboard players get @s temp')

    run('data modify entity @s PickupDelay set value 0')
    removetag(self, 'relicNotDone')
def applyartistats(lvl1: int, lvl2: int, lvl3: int, lvl4: int, lvl5: int):
    for i in range(self.times):
        # Random Stat
        if self.dtemp == 1:
            randint('self.stat', 0, 5)
        else:
            randint('self.stat', 0, 6)
        if self.stat == 0:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}0% Maximum Health", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-MaxHealth'))
            run(f'scoreboard players add @s temp {lvl2}0')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-MaxHealth int 1 run scoreboard players get @s temp')
        elif self.stat == 1:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}0% Maximum Shields", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-MaxShields'))
            run(f'scoreboard players add @s temp {lvl2}0')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-MaxShields int 1 run scoreboard players get @s temp')
        elif self.stat == 2:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  -{lvl5}s Shield Regeneration Cooldown", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-ShieldCD'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-ShieldCD int 1 run scoreboard players get @s temp')
        elif self.stat == 3:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl2}0% Defense", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Defense'))
            run(f'scoreboard players add @s temp {lvl2}0')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Defense int 1 run scoreboard players get @s temp')
        elif self.stat == 4:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl1}% Health per second", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-HPRegen'))
            run(f'scoreboard players add @s temp {lvl2}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-HPRegen int 1 run scoreboard players get @s temp')
        elif self.stat == 5:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl3}0% Shield Recharge", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-ShieldRegen'))
            run(f'scoreboard players add @s temp {lvl3}0')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-ShieldRegen int 1 run scoreboard players get @s temp')
        elif self.stat == 6:
            run(f'data modify entity @s Item.components."minecraft:lore" append value {{"color": "aqua", "text": "  +{lvl4}% Dodge Chance", "italic": false}}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".R-Dodge'))
            run(f'scoreboard players add @s temp {lvl4}')
            run('execute store result entity @s Item.components."minecraft:custom_data".R-Dodge int 1 run scoreboard players get @s temp')
            self.dtemp = 1
        
    run('data modify entity @s PickupDelay set value 0')
    removetag(self, 'artifactNotDone')

def replaceSlots():
    # Relics
    if entity('@s[nbt=!{Inventory:[{Slot:9b, components:{"minecraft:custom_data":{Relic:1}}}]}]'): run('item replace entity @s container.9 with brown_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Relic Slot 1","italic":false}],lore=[[{"text":"A slot to place a relic.","italic":false,"color":"gray"}],[{"text":"Relics give random offensive stats to boost your builds.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A RELIC!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:18b, components:{"minecraft:custom_data":{Relic:1}}}]}]'): run('item replace entity @s container.18 with brown_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Relic Slot 2","italic":false}],lore=[[{"text":"A slot to place a relic.","italic":false,"color":"gray"}],[{"text":"Relics give random offensive stats to boost your builds.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A RELIC!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:27b, components:{"minecraft:custom_data":{Relic:1}}}]}]'): run('item replace entity @s container.27 with brown_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Relic Slot 3","italic":false}],lore=[[{"text":"A slot to place a relic.","italic":false,"color":"gray"}],[{"text":"Relics give random offensive stats to boost your builds.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A RELIC!","italic":false,"color":"dark_red"}]]]')

    # Artifacts
    if entity('@s[nbt=!{Inventory:[{Slot:17b, components:{"minecraft:custom_data":{Artifact:1}}}]}]'): run('item replace entity @s container.17 with white_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Flower Slot 1","italic":false}],lore=[[{"text":"A slot to place a flower.","italic":false,"color":"gray"}],[{"text":"Flowers give random defensive stats to boost your survival.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A FLOWER!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:26b, components:{"minecraft:custom_data":{Artifact:1}}}]}]'): run('item replace entity @s container.26 with white_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Flower Slot 2","italic":false}],lore=[[{"text":"A slot to place a flower.","italic":false,"color":"gray"}],[{"text":"Flowers give random defensive stats to boost your survival.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A FLOWER!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:35b, components:{"minecraft:custom_data":{Artifact:1}}}]}]'): run('item replace entity @s container.35 with white_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Flower Slot 3","italic":false}],lore=[[{"text":"A slot to place a flower.","italic":false,"color":"gray"}],[{"text":"Flowers give random defensive stats to boost your survival.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A FLOWER!","italic":false,"color":"dark_red"}]]]')

    # Mods
    if entity('@s[nbt=!{Inventory:[{Slot:10b, components:{"minecraft:custom_data":{ModSlot:1}}}]}]'): run('item replace entity @s container.10 with light_blue_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Mod Slot 1","italic":false}],lore=[[{"text":"A slot to place a Slot 1 Mod.","italic":false,"color":"gray"}],[{"text":"Slot 1 mods usually are related to Base DMG.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A MOD SLOT 1!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:11b, components:{"minecraft:custom_data":{ModSlot:2}}}]}]'): run('item replace entity @s container.11 with light_blue_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Mod Slot 2","italic":false}],lore=[[{"text":"A slot to place a Slot 2 Mod.","italic":false,"color":"gray"}],[{"text":"Slot 1 mods usually are related to Critical Chance.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A MOD SLOT 2!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:12b, components:{"minecraft:custom_data":{ModSlot:3}}}]}]'): run('item replace entity @s container.12 with light_blue_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Mod Slot 3","italic":false}],lore=[[{"text":"A slot to place a Slot 3 Mod.","italic":false,"color":"gray"}],[{"text":"Slot 1 mods usually are related to Critical Damage.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A MOD SLOT 3!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:13b, components:{"minecraft:custom_data":{ModSlot:4}}}]}]'): run('item replace entity @s container.13 with light_blue_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Mod Slot 4","italic":false}],lore=[[{"text":"A slot to place a Slot 4 Mod.","italic":false,"color":"gray"}],[{"text":"Slot 1 mods usually are related to statuses.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A MOD SLOT 4!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:14b, components:{"minecraft:custom_data":{ModSlot:5}}}]}]'): run('item replace entity @s container.14 with light_blue_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Mod Slot 5","italic":false}],lore=[[{"text":"A slot to place a Slot 5 Mod.","italic":false,"color":"gray"}],[{"text":"Slot 1 mods usually are related to utilities.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A MOD SLOT 5!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:15b, components:{"minecraft:custom_data":{ModSlot:6}}}]}]'): run('item replace entity @s container.15 with light_blue_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Mod Slot 6","italic":false}],lore=[[{"text":"A slot to place a Slot 6 Mod.","italic":false,"color":"gray"}],[{"text":"Slot 1 mods usually are related to defensive stats.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A MOD SLOT 6!","italic":false,"color":"dark_red"}]]]')
    if entity('@s[nbt=!{Inventory:[{Slot:16b, components:{"minecraft:custom_data":{ModSlot:7}}}]}]'): run('item replace entity @s container.16 with light_blue_stained_glass_pane[custom_data={Useless:1},custom_name=[{"text":"Empty Mod Slot 7","italic":false}],lore=[[{"text":"A slot to place a Slot 7 Mod.","italic":false,"color":"gray"}],[{"text":"Slot 1 mods usually are related to Weapon Augments.","italic":false,"color":"gray"}],"",[{"text":"DO NOT PLACE ANY ITEMS HERE!","italic":false,"color":"dark_red"}],[{"text":"IT WILL GET DELETED IF IT IS NOT A MOD SLOT 7!","italic":false,"color":"dark_red"}]]]')


def tickmodifiers():
    # Selector: player
    """ LEVEL """
    # We need to detect for level changes, because CURRENT HEALTH won't be updated
    if self.previouslvl != self.lvl:
        # That means it changed: Add +10% of 500 Health (and Shields), which is 50.
        self.temp = self.lvl
        self.temp -= self.previouslvl
        self.health += 50 * self.temp
        self.shields += 50 * self.temp
    self.previouslvl = self.lvl

    self.max_health = (500 * (10 + self.lvl))
    self.max_health /= 10
    self.max_shields = (500 * (10 + self.lvl))
    self.max_shields /= 10
    self.defense = (200 * (10 + self.lvl))
    self.defense /= 10

    """ ITEM REPLACEMENTS """
    replaceSlots()

    """ RELICS """
    store(self.stat.dmgbonus, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-BaseDMG'))
    store(self.stat.cr, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-CR'))
    store(self.stat.cd, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-CD'))
    store(self.em, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-EM'))
    store(self.stat.status, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-Status'))
    store(self.stat.atkspd, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-ATKSPD'))
    store(self.multihit, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-Multihit'))

    store(self.stat.fire, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-Fire'))
    store(self.stat.ice, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-Ice'))
    store(self.stat.water, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-Water'))
    store(self.stat.electric, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-Electric'))
    store(self.stat.nature, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".R-Nature'))

    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-BaseDMG'))
    self.stat.dmgbonus += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-CR'))
    self.stat.cr += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-CD'))
    self.stat.cd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-EM'))
    self.em += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-Status'))
    self.stat.status += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-Fire'))
    self.stat.fire += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-Ice'))
    self.stat.ice += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-Water'))
    self.stat.water += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-Electric'))
    self.stat.electric += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-Nature'))
    self.stat.nature += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-ATKSPD'))
    self.stat.atkspd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".R-Multihit'))
    self.multihit += self.temp

    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-BaseDMG'))
    self.stat.dmgbonus += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-CR'))
    self.stat.cr += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-CD'))
    self.stat.cd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-EM'))
    self.em += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-Status'))
    self.stat.status += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-Fire'))
    self.stat.fire += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-Ice'))
    self.stat.ice += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-Water'))
    self.stat.water += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-Electric'))
    self.stat.electric += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-Nature'))
    self.stat.nature += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-ATKSPD'))
    self.stat.atkspd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".R-Multihit'))
    self.multihit += self.temp

    # Add base numbers after relic calcs
    self.em += 5
    self.multihit += 100

    """ ARTIFACTS """
    store(self.stat.maxhealth, getdata(self,    'Inventory[{Slot:17b}].components."minecraft:custom_data".R-MaxHealth'))
    store(self.stat.maxshields, getdata(self,   'Inventory[{Slot:17b}].components."minecraft:custom_data".R-MaxShields'))
    store(self.stat.shieldcd, getdata(self,     'Inventory[{Slot:17b}].components."minecraft:custom_data".R-ShieldCD'))
    store(self.stat.defense, getdata(self,      'Inventory[{Slot:17b}].components."minecraft:custom_data".R-Defense'))
    store(self.dodge, getdata(self,             'Inventory[{Slot:17b}].components."minecraft:custom_data".R-Dodge'))
    store(self.stat.hpregen, getdata(self,      'Inventory[{Slot:17b}].components."minecraft:custom_data".R-HPRegen'))
    store(self.stat.shieldregen, getdata(self,  'Inventory[{Slot:15b}].components."minecraft:custom_data".R-ShieldRegen'))

    store(self.temp, getdata(self, 'Inventory[{Slot:26b}].components."minecraft:custom_data".R-MaxHealth'))
    self.stat.maxhealth += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:26b}].components."minecraft:custom_data".R-MaxShields'))
    self.stat.maxshields += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:26b}].components."minecraft:custom_data".R-ShieldCD'))
    self.stat.shieldcd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:26b}].components."minecraft:custom_data".R-Defense'))
    self.stat.defense += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:26b}].components."minecraft:custom_data".R-Dodge'))
    self.dodge += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:26b}].components."minecraft:custom_data".R-HPRegen'))
    self.stat.hpregen += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:26b}].components."minecraft:custom_data".R-ShieldRegen'))
    self.stat.shieldregen += self.temp
    
    store(self.temp, getdata(self, 'Inventory[{Slot:35b}].components."minecraft:custom_data".R-MaxHealth'))
    self.stat.maxhealth += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:35b}].components."minecraft:custom_data".R-MaxShields'))
    self.stat.maxshields += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:35b}].components."minecraft:custom_data".R-ShieldCD'))
    self.stat.shieldcd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:35b}].components."minecraft:custom_data".R-Defense'))
    self.stat.defense += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:35b}].components."minecraft:custom_data".R-Dodge'))
    self.dodge += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:35b}].components."minecraft:custom_data".R-HPRegen'))
    self.stat.hpregen += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:35b}].components."minecraft:custom_data".R-ShieldRegen'))
    self.stat.shieldregen += self.temp

    # Add base HP regen
    self.stat.hpregen += 5

    """ MODS """
    # Slot 1: Base DMG mods
    execute('if entity @s[nbt={Inventory:[{Slot:10b, components:{"minecraft:custom_data":{ModID: "Serration"}}}]}]', add(self.stat.dmgbonus, 75))
    execute('if entity @s[nbt={Inventory:[{Slot:10b, components:{"minecraft:custom_data":{ModID: "Critical Serration"}}}]}]', mod_CS)
    def mod_CS():
        if self.stat.dmgbonus <= 100:
            self.stat.dmgbonus += 120
        else:
            self.stat.dmgbonus += 60
    execute('if entity @s[nbt={Inventory:[{Slot:10b, components:{"minecraft:custom_data":{ModID: "Overlying Hits"}}}]}]', add(self.stat.dmgbonus, 150))

    # Slot 2: Crit rate mods
    execute('if entity @s[nbt={Inventory:[{Slot:11b, components:{"minecraft:custom_data":{ModID: "Shattering Hits"}}}]}]', add(self.stat.cr, 120))
    execute('if entity @s[nbt={Inventory:[{Slot:11b, components:{"minecraft:custom_data":{ModID: "Critical Delay"}}}]}]', mod_CD)
    def mod_CD():
        self.stat.cr += 200
        self.stat.atkspd -= 33

    # Slot 3: Crit dmg mods
    execute('if entity @s[nbt={Inventory:[{Slot:12b, components:{"minecraft:custom_data":{ModID: "Target Cracker"}}}]}]', add(self.stat.cd, 120))
    execute('if entity @s[nbt={Inventory:[{Slot:12b, components:{"minecraft:custom_data":{ModID: "Critical Sacrifice"}}}]}]', mod_CSac)
    def mod_CSac():
        self.stat.cd += 200
        self.stat.dmgbonus -= 33

    # Slot 4: Status-related mods
    execute('if entity @s[nbt={Inventory:[{Slot:13b, components:{"minecraft:custom_data":{ModID: "Elemental Composition"}}}]}]', add(self.em, 8))
    execute('if entity @s[nbt={Inventory:[{Slot:13b, components:{"minecraft:custom_data":{ModID: "Ice Superiority"}}}]}]', mod_IS)
    def mod_IS():
        self.stat.ice += 100
        self.stat.fire -= 50
    execute('if entity @s[nbt={Inventory:[{Slot:13b, components:{"minecraft:custom_data":{ModID: "Electric Superiority"}}}]}]', (
        add(self.stat.electric, 100), sub(self.stat.water, 50)
    ))

    execute('if entity @s[nbt={Inventory:[{Slot:13b, components:{"minecraft:custom_data":{ModID: "Master\'s Composition"}}}]}]', mult(self.em, 1.5))

    # Slot 5
    execute('if entity @s[nbt={Inventory:[{Slot:14b, components:{"minecraft:custom_data":{ModID: "Catalyzing Shields"}}}]}]', sub(self.stat.maxshields, 75))

    # Slot 6: Defensive upgrades
    execute('if entity @s[nbt={Inventory:[{Slot:15b, components:{"minecraft:custom_data":{ModID: "Enhanced Vitality"}}}]}]', (
        add(self.stat.maxhealth, 100), add(self.stat.defense, 100)
    ))
    execute('if entity @s[nbt={Inventory:[{Slot:15b, components:{"minecraft:custom_data":{ModID: "Enhanced Deflection"}}}]}]', (
        add(self.stat.maxshields, 200), add(self.max_shields, 500)
    ))
    execute('if entity @s[nbt={Inventory:[{Slot:15b, components:{"minecraft:custom_data":{ModID: "Repairing Shields"}}}]}]', (
        add(self.stat.shieldregen, 100), add(self.stat.shieldcd, 8)
    ))

    """ FINAL TOUCHES """
    # modify attack speed
    execute('if entity @s[nbt={Inventory:[{Slot:10b, components:{"minecraft:custom_data":{ModID: "Overlying Hits"}}}]}]', set(self.stat.atkspd, 0))
    run('execute store result storage kcf:modtemp atkspd double 0.01 run scoreboard players get @s stat.atkspd')
    run('function kcf:atkspdmacro with storage kcf:modtemp')

    
    # Update max Shields, health and defense
    self.max_health *= (100 + self.stat.maxhealth)
    self.max_health /= 100
    self.max_shields *= (100 + self.stat.maxshields)
    self.max_shields /= 100
    self.defense *= (100 + self.stat.defense)
    self.defense /= 100


def atkspdmacro(atkspd: float):
    run('attribute @s minecraft:attack_speed modifier remove statatkspd')
    run(f'attribute @s minecraft:attack_speed modifier add statatkspd {atkspd} add_multiplied_total')

def bronzerelic():
    run('summon item ~ ~ ~ {Tags:[relicNotDone],PickupDelay:100,Item:{id:"minecraft:leather_horse_armor",count:1,components:{"minecraft:custom_data":{Relic:1},"minecraft:item_name":[{"text":"Bronze Relic","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Relic Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: 20, lvl2: 30, lvl3: 1}')
    execute('as @n[type=item,tag=relicNotDone]', (set(self.times, 4), applystats()))

def silverrelic():
    run('summon item ~ ~ ~ {Tags:[relicNotDone],PickupDelay:100,Item:{id:"minecraft:iron_horse_armor",count:1,components:{"minecraft:custom_data":{Relic:1},"minecraft:item_name":[{"text":"Silver Relic","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Relic Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: 30, lvl2: 45, lvl3: 2}')
    execute('as @n[type=item,tag=relicNotDone]', (randint(self.times, 4, 5), applystats()))

def goldrelic():
    run('summon item ~ ~ ~ {Tags:[relicNotDone],PickupDelay:100,Item:{id:"minecraft:golden_horse_armor",count:1,components:{"minecraft:custom_data":{Relic:1},"minecraft:item_name":[{"text":"Gold Relic","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Relic Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: 40, lvl2: 60, lvl3: 3}')
    execute('as @n[type=item,tag=relicNotDone]', (set(self.times, 5), applystats()))

def diamondrelic():
    run('summon item ~ ~ ~ {Tags:[relicNotDone],PickupDelay:100,Item:{id:"minecraft:diamond_horse_armor",count:1,components:{"minecraft:custom_data":{Relic:1},"minecraft:item_name":[{"text":"Diamond Relic","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Relic Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: 50, lvl2: 75, lvl3: 4}')
    execute('as @n[type=item,tag=relicNotDone]', (randint(self.times, 5, 6), applystats()))

def bronzeartifact():
    run('summon item ~ ~ ~ {Tags:[artifactNotDone],PickupDelay:100,Item:{id:"minecraft:white_tulip",count:1,components:{"minecraft:custom_data":{Artifact:1},"minecraft:item_name":[{"text":"White Flower","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Flower Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: "0.2", lvl2: 1, lvl3: 2, lvl4: 5, lvl5: "0.05"}')
    execute('as @n[type=item,tag=artifactNotDone]', (randint(self.times, 3, 4), applyartistats()))
def silverartifact():
    run('summon item ~ ~ ~ {Tags:[artifactNotDone],PickupDelay:100,Item:{id:"minecraft:orange_tulip",count:1,components:{"minecraft:custom_data":{Artifact:1},"minecraft:item_name":[{"text":"Orange Flower","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Flower Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: "0.4", lvl2: 2, lvl3: 3, lvl4: 10, lvl5: "0.1"}')
    execute('as @n[type=item,tag=artifactNotDone]', (randint(self.times, 3, 4), applyartistats()))
def goldartifact():
    run('summon item ~ ~ ~ {Tags:[artifactNotDone],PickupDelay:100,Item:{id:"minecraft:red_tulip",count:1,components:{"minecraft:custom_data":{Artifact:1},"minecraft:item_name":[{"text":"Red Flower","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Flower Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: "0.6", lvl2: 3, lvl3: 6, lvl4: 15, lvl5: "0.15"}')
    execute('as @n[type=item,tag=artifactNotDone]', (randint(self.times, 3, 4), applyartistats()))
def diamondartifact():
    run('summon item ~ ~ ~ {Tags:[artifactNotDone],PickupDelay:100,Item:{id:"minecraft:pink_tulip",count:1,components:{"minecraft:custom_data":{Artifact:1},"minecraft:item_name":[{"text":"Purple Flower","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Flower Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: "0.8", lvl2: 4, lvl3: 8, lvl4: 20, lvl5: "0.2"}')
    execute('as @n[type=item,tag=artifactNotDone]', (randint(self.times, 3, 4), applyartistats()))

def opartifact():
    run('summon item ~ ~ ~ {Tags:[artifactNotDone],PickupDelay:100,Item:{id:"minecraft:pink_tulip",count:1,components:{"minecraft:custom_data":{Artifact:1},"minecraft:item_name":[{"text":"OP Flower","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Flower Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: "0.8", lvl2: 4, lvl3: 8, lvl4: 20, lvl5: "0.2"}')
    execute('as @n[type=item,tag=artifactNotDone]', (set(self.times, 10), applyartistats()))
def extraopartifact():
    run('summon item ~ ~ ~ {Tags:[artifactNotDone],PickupDelay:100,Item:{id:"minecraft:pink_tulip",count:1,components:{"minecraft:custom_data":{Artifact:1},"minecraft:item_name":[{"text":"OP Flower","italic":false}],"minecraft:lore":[{"color":"light_purple","text":"Flower Stats:", "italic": false}]}}}')
    run('data merge storage kcf:functionargs {lvl1: "0.8", lvl2: 4, lvl3: 8, lvl4: 20, lvl5: "0.2"}')
    execute('as @n[type=item,tag=artifactNotDone]', (set(self.times, 50), applyartistats()))

def givecmod(name: str, slot: int, desc: str):
    run(f'give @s blade_pottery_sherd[custom_data={{Mod:1,ModSlot:{slot},ModID:"{name}"}},custom_name=[{{"text":"[MOD] {name}","italic":false}}],lore=[[{{"text":"When this mod is activated:","italic":false,"color":"gray"}}],[{{"text":"{desc}","italic":false,"color":"gray"}}],"",[{{"text":"Fits in: Mod Slot {slot}","italic":false,"color":"dark_gray"}}]],enchantment_glint_override=true]')
def giveumod(name: str, slot: int, desc: str):
    run(f'give @s flow_pottery_sherd[custom_data={{Mod:1,ModSlot:{slot},ModID:"{name}"}},custom_name=[{{"text":"[MOD] {name}","italic":false}}],lore=[[{{"text":"When this mod is activated:","italic":false,"color":"gray"}}],[{{"text":"{desc}","italic":false,"color":"gray"}}],"",[{{"text":"Fits in: Mod Slot {slot}","italic":false,"color":"dark_gray"}}]],enchantment_glint_override=true]')
def givermod(name: str, slot: int, desc: str):
    run(f'give @s prize_pottery_sherd[custom_data={{Mod:1,ModSlot:{slot},ModID:"{name}"}},custom_name=[{{"text":"[MOD] {name}","italic":false}}],lore=[[{{"text":"When this mod is activated:","italic":false,"color":"gray"}}],[{{"text":"{desc}","italic":false,"color":"gray"}}],"",[{{"text":"Fits in: Mod Slot {slot}","italic":false,"color":"dark_gray"}}]],enchantment_glint_override=true]')


def commonmod():
    """Gives a random common mod"""
    randint(self.temp, 0, 5)
    # Should be sorted in ascending order of slots
    if self.temp == 0: givecmod({"name": '"Serration"', "slot": 1, "desc": '"+75% Base DMG"'})
    if self.temp == 1: givecmod({"name": '"Shattering Hits"', "slot": 2, "desc": '"+120% Critical Chance"'})
    if self.temp == 2: givecmod({"name": '"Target Cracker"', "slot": 3, "desc": '"+120% Critical Damage"'})
    if self.temp == 3: givecmod({"name": '"Elemental Composition"', "slot": 4, "desc": '"+8 Elemental Mastery"'})
    if self.temp == 4: givecmod({"name": '"Enhanced Vitality"', "slot": 6, "desc": '"+100% Maximum Health, +100% Defense"'})
    if self.temp == 5: givecmod({"name": '"Enhanced Deflection"', "slot": 6, "desc": '"+200% Maximum Shields, +500 Shields"'})

def uncommonmod():
    """Gives a random uncommon mod"""
    randint(self.temp, 0, 6)
    # Should be sorted in ascending order of slots
    if self.temp == 0: giveumod({"name": '"Critical Serration"', "slot": 1, "desc": '"+60% Base DMG. If Base DMG is already less than 100%, this effect is doubled"'})
    if self.temp == 1: giveumod({"name": '"Overlying Hits"', "slot": 1, "desc": '"+150% Base DMG but Attack Speed cannot be modified"'})
    if self.temp == 2: giveumod({"name": '"Critical Delay"', "slot": 2, "desc": '"+200% Critical Chance, -33% Attack Speed"'})
    if self.temp == 3: giveumod({"name": '"Critical Sacrifice"', "slot": 3, "desc": '"+200% Critical Damage, -33% Base DMG"'})
    if self.temp == 4: giveumod({"name": '"Ice Superiority"', "slot": 4, "desc": '"+100% Ice DMG Bonus, -50% Fire DMG Bonus"'})
    if self.temp == 5: giveumod({"name": '"Electric Superiority"', "slot": 4, "desc": '"+100% Electric DMG Bonus, -50% Water DMG Bonus"'})
    if self.temp == 6: giveumod({"name": '"Repairing Shields"', "slot": 6, "desc": '"+100% Shield Recharge, -0.4s Shield Recharge Delay"'})

def raremod():
    """Gives a random rare mod"""
    randint(self.temp, 0, 8)
    # Should be sorted in ascending order of slots
    # NVM, it messes up with self.temp order
    if self.temp == 0: givermod({"name": '"Crispy Hits"', "slot": 1, "desc": '"Each Ice stack the entity has increases Base DMG by +30%"'})
    if self.temp == 1: givermod({"name": '"Steel Blade"', "slot": 2, "desc": '"Non-critical hits increase Critical Steel counter by 1. Each Critical Steel counter adds a +20% final Critical Chance to attacks. Critical hits halve Critical Steel counter."'})
    if self.temp == 2: givermod({"name": '"Nature\'s Revenge"', "slot": 3, "desc": '"Each Nature stack the entity has increases Critical Damage by +15%, up to +120%. Each Critical hit deals 15 Nature DMG if the entity has the Nature status."'})
    if self.temp == 4: givermod({"name": '"Master\'s Composition"', "slot": 4, "desc": '"Increases current Elemental Mastery by 50%"'})
    if self.temp == 5: givermod({"name": '"Biotic Hits"', "slot": 4, "desc": '"On a Critical Hit: 30% to apply Viral to the entity hit."'})
    if self.temp == 6: givermod({"name": '"Catalyzing Shields"', "slot": 5, "desc": '"-75% Maximum Shields. The invincibility duration after Shields is broken is fixed at 0.6s."'})
    if self.temp == 7: givermod({"name": '"Electrical Shields"', "slot": 6, "desc": '"Duration of Magnetized is halved. While DMG is taken to Shields: Emit a small pulse, which deals 200 Electric DMG to nearby mobs (including Bloom Cores) within 3m"'})
    if self.temp == 8: givermod({"name": '"Blessing of the Sea"', "slot": 2, "desc": '"Each water stack the entity has increases Critical Chance by +50%"'})

def tick():
    execute('as @e[tag=!notmob] at @s', genericEntityTick)
    execute('as @e[tag=bloomCore] at @s', bloomCoreTick)
    execute('as @e[type=text_display,tag=dmgtext]', dmgtextanimation)
    execute('as @e[type=interaction,tag=joinmsg] if data entity @s interaction on target', (
        run('trigger start'),
        run('data remove entity @n[type=interaction,tag=joinmsg] interaction')
    ))
    execute('as @e[tag=ww] at @s', ww)

    # Bossbar
    if started == 1 and waiting == 0:
        timeleft -= 1
        timeleftS = timeleft
        timeleftS /= 20
        showtimer(timeleft)
        if timeleft <= 0:
            numOfMobs = 0
            execute('as @e[distance=..24, type=!player,tag=mob]', add(numOfMobs, 1))
            if numOfMobs > 0:
                timelives -= 1
                failed = 1
                print(f"#red,b#You failed to beat all the mobs within the specified time!\nYou now have {timelives} time lives remaining.")
                kill('@e[type=!player,tag=mob]')

                if timelives == 0:
                    print(f"#red,b#You lost all of your time lives! Game stopped.")
                    kill(all)
                    stop()

shopphase1: int
shopphase2: int

def shopphase():
    run('bossbar set timer visible false')

    kill('@e[type=!player,type=!item,tag=!notmob,tag=!important]')

    if failed != 1:
        temp = 4 + level
        print(f"#gold#+{temp} Coins (Cleared floor)")
        failed = 0

    all.coins += temp
    if level < 4:
        print(f"#light_purple#Shop phase! You have 15s to shop until your next round!")
        schedule('15s', newfloor)
    else:
        print(f"#light_purple#Shop phase! You have 30s to shop until your next round!")
        schedule('30s', newfloor)

    if level == 5:
        print(f"#green#You completed floor 5! From now on, shop items will be random and the difficulty is increased but you will get better rewards!")
    if level == 49:
        print(f"#green#You made it to floor 50! You officially beat the game! You are entering endless mode, where random mobs will spawn each floor with changed drop tables.")

    waiting = 1
    randint(shopphase1, 1, 24)
    randint(shopphase2, 1, 24)

    wait('1s', shop)

def shop():
    run('tellraw @a ["",{"text":"Always Avaliable:","color":"light_purple"},{"text":"\\n"},{"text":"\u2192 Buy Relics and Mods","underlined":false,"color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 1"},"hover_event":{"action":"show_text","value":{"text":"Displays a shop list for buying Relics and Mods","color":"gray"}}},{"text":"\\n+100 HP [2 Coins]","underlined":false,"color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 8"}},{"text":"\\n+300 HP [5 Coins]","underlined":false,"color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 9"}},{"text":"\\n"},{"text":"Current Items:","color":"light_purple"}]')

    if level >= 5:
        if shopphase1 == 1:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 2:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_fire.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 3:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_ice.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 4:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_water.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 5:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_electric.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 6:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_nature.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 7:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 8:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_fire.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 9:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_ice.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 10:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_water.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 11:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_electric.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 12:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_nature.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 13:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 14:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_fire.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 15:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_ice.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 16:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_water.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 17:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_electric.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 18:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_nature.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop') 
        if shopphase1 == 19:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 20:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_fire.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 21:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_ice.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 22:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_water.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 23:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_electric.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        if shopphase1 == 24:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_nature.shopdata\nfunction kcf:shopweapon1 with storage kcf:functionargs shop')
        
        if shopphase2 == 1:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 2:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_fire.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 3:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_ice.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 4:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_water.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 5:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_electric.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 6:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons ironsword_nature.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 7:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 8:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_fire.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 9:   run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_ice.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 10:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_water.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 11:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_electric.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 12:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons coppersword_nature.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 13:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 14:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_fire.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 15:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_ice.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 16:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_water.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 17:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_electric.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 18:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons goldensword_nature.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop') 
        if shopphase2 == 19:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 20:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_fire.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 21:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_ice.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 22:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_water.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 23:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_electric.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
        if shopphase2 == 24:  run('data modify storage kcf:functionargs shop set from storage kcs:weapons diamondsword_nature.shopdata\nfunction kcf:shopweapon2 with storage kcf:functionargs shop')
    else:
        run('tellraw @a [{"text":"Iron Sword","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 12"},"hover_event":{"action":"show_item", "id": "iron_sword", "count": 1, "components":{custom_name:[{"text":"Iron Sword","italic":false}],lore:[[{"text":"The standard sword wielded by many major swordsman with its decent DMG, status chance, and its critical abilities. Highly recommended for your first weapon.","italic":false,"color":"gray"}],"",[{"text":"Base DMG: 185","italic":false,"color":"gray"}],[{"text":"Base Status: 25%","italic":false,"color":"gray"}],[{"text":"Base Critical Chance: 20%","italic":false,"color":"gray"}],[{"text":"Base Critical Damage: 50%","italic":false,"color":"gray"}],[{"text":"Base Attack Speed: 1.6/s","italic":false,"color":"gray"}]],attribute_modifiers:[{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:1.6,slot:mainhand,id:"weapon_atkspdmod",operation:add_value}]}}},{"text":" [50 Coins]","color":"aqua"}]')        
        run('tellraw @a [{"text":"Flaming Copper Sword","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 13"},"hover_event":{"action":"show_item", "id": "copper_sword", "count": 1, "components":{custom_name:[{"text":"Flaming Copper Sword","italic":false}],lore:[[{"text":"A standard sword that is very conductive but lacks the standard damage output. Recommended to get this only after beating Floor 5.","italic":false,"color":"gray"}],"",[{"text":"Base DMG: 30","italic":false,"color":"gray"}],[{"text":"Base Status: 75%","italic":false,"color":"gray"}],[{"text":"Base Critical Chance: 15%","italic":false,"color":"gray"}],[{"text":"Base Critical Damage: 50%","italic":false,"color":"gray"}],[{"text":"Base Attack Speed: 1.6/s","italic":false,"color":"gray"}]],attribute_modifiers:[{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:1.6,slot:mainhand,id:"weapon_atkspdmod",operation:add_value}]}}},{"text":" [20 Coins]","color":"aqua"}]')        
        run('tellraw @a [{"text":"Iced Copper Sword","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 11"},"hover_event":{"action":"show_item", "id": "copper_sword", "count": 1, "components":{custom_name:[{"text":"Iced Copper Sword","italic":false}],lore:[[{"text":"A standard sword that is very conductive but lacks the standard damage output. Recommended to get this only after beating Floor 5.","italic":false,"color":"gray"}],"",[{"text":"Base DMG: 30","italic":false,"color":"gray"}],[{"text":"Base Status: 75%","italic":false,"color":"gray"}],[{"text":"Base Critical Chance: 15%","italic":false,"color":"gray"}],[{"text":"Base Critical Damage: 50%","italic":false,"color":"gray"}],[{"text":"Base Attack Speed: 1.6/s","italic":false,"color":"gray"}]],attribute_modifiers:[{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:1.6,slot:mainhand,id:"weapon_atkspdmod",operation:add_value}]}}},{"text":" [20 Coins]","color":"aqua"}]')        
        run('tellraw @a [{"text":"Hydrous Copper Sword","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 14"},"hover_event":{"action":"show_item", "id": "copper_sword", "count": 1, "components":{custom_name:[{"text":"Hydrous Copper Sword","italic":false}],lore:[[{"text":"A standard sword that is very conductive but lacks the standard damage output. Recommended to get this only after beating Floor 5.","italic":false,"color":"gray"}],"",[{"text":"Base DMG: 30","italic":false,"color":"gray"}],[{"text":"Base Status: 75%","italic":false,"color":"gray"}],[{"text":"Base Critical Chance: 15%","italic":false,"color":"gray"}],[{"text":"Base Critical Damage: 50%","italic":false,"color":"gray"}],[{"text":"Base Attack Speed: 1.6/s","italic":false,"color":"gray"}]],attribute_modifiers:[{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:1.6,slot:mainhand,id:"weapon_atkspdmod",operation:add_value}]}}},{"text":" [20 Coins]","color":"aqua"}]')        
        run('tellraw @a [{"text":"Shocking Copper Sword","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 15"},"hover_event":{"action":"show_item", "id": "copper_sword", "count": 1, "components":{custom_name:[{"text":"Shocking Copper Sword","italic":false}],lore:[[{"text":"A standard sword that is very conductive but lacks the standard damage output. Recommended to get this only after beating Floor 5.","italic":false,"color":"gray"}],"",[{"text":"Base DMG: 30","italic":false,"color":"gray"}],[{"text":"Base Status: 75%","italic":false,"color":"gray"}],[{"text":"Base Critical Chance: 15%","italic":false,"color":"gray"}],[{"text":"Base Critical Damage: 50%","italic":false,"color":"gray"}],[{"text":"Base Attack Speed: 1.6/s","italic":false,"color":"gray"}]],attribute_modifiers:[{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:1.6,slot:mainhand,id:"weapon_atkspdmod",operation:add_value}]}}},{"text":" [20 Coins]","color":"aqua"}]')        
        run('tellraw @a [{"text":"Nurturous Copper Sword","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 16"},"hover_event":{"action":"show_item", "id": "copper_sword", "count": 1, "components":{custom_name:[{"text":"Nurturous Copper Sword","italic":false}],lore:[[{"text":"A standard sword that is very conductive but lacks the standard damage output. Recommended to get this only after beating Floor 5.","italic":false,"color":"gray"}],"",[{"text":"Base DMG: 30","italic":false,"color":"gray"}],[{"text":"Base Status: 75%","italic":false,"color":"gray"}],[{"text":"Base Critical Chance: 15%","italic":false,"color":"gray"}],[{"text":"Base Critical Damage: 50%","italic":false,"color":"gray"}],[{"text":"Base Attack Speed: 1.6/s","italic":false,"color":"gray"}]],attribute_modifiers:[{type:attack_damage,amount:-0.81,slot:mainhand,id:"weapon_atkdecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:-4,slot:mainhand,id:"weapon_atkspddecrease",display:{type:"hidden"},operation:add_value},{type:attack_speed,amount:1.6,slot:mainhand,id:"weapon_atkspdmod",operation:add_value}]}}},{"text":" [20 Coins]","color":"aqua"}]')        

    def shopweapon1(Name, Cost, ItemData): run(f'tellraw @a [{{"text":"{Name}","color":"yellow","click_event":{{"action":"run_command","command":"/trigger buy set 11"}},"hover_event":{ItemData}}},{{"text":" [{Cost} Coins]","color":"aqua"}}]')
    def shopweapon2(Name, Cost, ItemData): run(f'tellraw @a [{{"text":"{Name}","color":"yellow","click_event":{{"action":"run_command","command":"/trigger buy set 12"}},"hover_event":{ItemData}}},{{"text":" [{Cost} Coins]","color":"aqua"}}]')

def triggers__buy():
    if started == 0:
        tellraw(self, f"#red#The game has not started yet!")
    elif waiting == 0:
        tellraw(self, f"#red#The shop is closed! Clear the current floor to begin the shop")
    else:

        if self.buy == 1:
            run('tellraw @s [' \
                '{"text":"Bronze Relic","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 2"},"hover_event":{"action":"show_text","value":{"text":"Gives a random Bronze relic. What will you get?","color":"gray"}}},{"text":" [5 Coins]\\n", "color":"aqua"},' \
                '{"text":"Silver Relic","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 3"},"hover_event":{"action":"show_text","value":{"text":"Gives a random Silver relic. What will you get?","color":"gray"}}},{"text":" [15 Coins]\\n", "color":"aqua"},' \
                '{"text":"Gold Relic","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 4"},"hover_event":{"action":"show_text","value":{"text":"Gives a random Gold relic. What will you get?","color":"gray"}}},{"text":" [50 Coins]\\n", "color":"aqua"},' \
                '{"text":"Diamond Relic","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 5"},"hover_event":{"action":"show_text","value":{"text":"Gives a random Diamond relic. What will you get?","color":"gray"}}},{"text":" [150 Coins]\\n", "color":"aqua"},' \
                
                '{"text":"White Flower","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 2"},"hover_event":{"action":"show_text","value":{"text":"Gives a random White Flower (common flower). What will you get?","color":"gray"}}},{"text":" [10 Coins]\\n", "color":"aqua"},' \
                '{"text":"Orange Flower","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 3"},"hover_event":{"action":"show_text","value":{"text":"Gives a random Orange Flower (uncommon flower). What will you get?","color":"gray"}}},{"text":" [30 Coins]\\n", "color":"aqua"},' \
                '{"text":"Red Flower","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 4"},"hover_event":{"action":"show_text","value":{"text":"Gives a random Red Flower (rare flower). What will you get?","color":"gray"}}},{"text":" [75 Coins]\\n", "color":"aqua"},' \
                '{"text":"Purple Flower","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 5"},"hover_event":{"action":"show_text","value":{"text":"Gives a random Purple Flower (super rare flower). What will you get?","color":"gray"}}},{"text":" [225 Coins]\\n", "color":"aqua"},' \

                '{"text":"Common Mod","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 6"},"hover_event":{"action":"show_text","value":{"text":"Gives a random common mod. What will you get?","color":"gray"}}},{"text":" [20 Coins]\\n", "color":"aqua"},' \
                '{"text":"Uncommon Mod","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 7"},"hover_event":{"action":"show_text","value":{"text":"Gives a random uncommon mod. What will you get?","color":"gray"}}},{"text":" [50 Coins]\\n", "color":"aqua"},' \
                '{"text":"Rare Mod","color":"yellow","click_event":{"action":"run_command","command":"/trigger buy set 8"},"hover_event":{"action":"show_text","value":{"text":"Gives a random rare mod. What will you get?","color":"gray"}}},{"text":" [100 Coins]", "color":"aqua"}' \
            ']')
        elif self.buy == 2: buy({"Cost": 5, "Command": '"function kcf:bronzerelic"'})
        elif self.buy == 3: buy({"Cost": 15, "Command": '"function kcf:silverrelic"'})
        elif self.buy == 4: buy({"Cost": 50, "Command": '"function kcf:goldrelic"'})
        elif self.buy == 5: buy({"Cost": 150, "Command": '"function kcf:diamondrelic"'})
        elif self.buy == 21: buy({"Cost": 10, "Command": '"function kcf:bronzeartifact"'})
        elif self.buy == 22: buy({"Cost": 30, "Command": '"function kcf:silverartifact"'})
        elif self.buy == 22: buy({"Cost": 75, "Command": '"function kcf:goldartifact"'})
        elif self.buy == 23: buy({"Cost": 225, "Command": '"function kcf:diamondartifact"'})
        elif self.buy == 8: buy({"Cost": 2, "Command": '"scoreboard players add @s health 100"'})
        elif self.buy == 9: buy({"Cost": 5, "Command": '"scoreboard players add @s health 300"'})
        elif self.buy == 11: 
            if level >= 5:    
                if shopphase1 == 1:   buyweapon({"ID": '"ironsword"'})
                if shopphase1 == 2:   buyweapon({"ID": '"ironsword_fire"'})
                if shopphase1 == 3:   buyweapon({"ID": '"ironsword_ice"'})
                if shopphase1 == 4:   buyweapon({"ID": '"ironsword_water"'})
                if shopphase1 == 5:   buyweapon({"ID": '"ironsword_electric"'})
                if shopphase1 == 6:   buyweapon({"ID": '"ironsword_nature"'})
                if shopphase1 == 7:   buyweapon({"ID": '"coppersword"'})
                if shopphase1 == 8:   buyweapon({"ID": '"coppersword_fire"'})
                if shopphase1 == 9:   buyweapon({"ID": '"coppersword_ice"'})
                if shopphase1 == 10:  buyweapon({"ID": '"coppersword_water"'})
                if shopphase1 == 11:  buyweapon({"ID": '"coppersword_electric"'})
                if shopphase1 == 12:  buyweapon({"ID": '"coppersword_nature"'})
                if shopphase1 == 13:  buyweapon({"ID": '"goldensword"'})
                if shopphase1 == 14:  buyweapon({"ID": '"goldensword_fire"'})
                if shopphase1 == 15:  buyweapon({"ID": '"goldensword_ice"'})
                if shopphase1 == 16:  buyweapon({"ID": '"goldensword_water"'})
                if shopphase1 == 17:  buyweapon({"ID": '"goldensword_electric"'})
                if shopphase1 == 18:  buyweapon({"ID": '"goldensword_nature"'})
                if shopphase1 == 19:  buyweapon({"ID": '"diamondsword"'})
                if shopphase1 == 20:  buyweapon({"ID": '"diamondsword_fire"'})
                if shopphase1 == 21:  buyweapon({"ID": '"diamondsword_ice"'})
                if shopphase1 == 22:  buyweapon({"ID": '"diamondsword_water"'})
                if shopphase1 == 23:  buyweapon({"ID": '"diamondsword_electric"'})
                if shopphase1 == 24:  buyweapon({"ID": '"diamondsword_nature"'})
            else:
                buy({"Cost": 50, "Command": '"function kcf:giveweapon {ID: \\"coppersword_ice\\"}"'})
        elif self.buy == 12: 
            if level >= 5:    
                if shopphase2 == 1:   buyweapon({"ID": '"ironsword"'})
                if shopphase2 == 2:   buyweapon({"ID": '"ironsword_fire"'})
                if shopphase2 == 3:   buyweapon({"ID": '"ironsword_ice"'})
                if shopphase2 == 4:   buyweapon({"ID": '"ironsword_water"'})
                if shopphase2 == 5:   buyweapon({"ID": '"ironsword_electric"'})
                if shopphase2 == 6:   buyweapon({"ID": '"ironsword_nature"'})
                if shopphase2 == 7:   buyweapon({"ID": '"coppersword"'})
                if shopphase2 == 8:   buyweapon({"ID": '"coppersword_fire"'})
                if shopphase2 == 9:   buyweapon({"ID": '"coppersword_ice"'})
                if shopphase2 == 10:  buyweapon({"ID": '"coppersword_water"'})
                if shopphase2 == 11:  buyweapon({"ID": '"coppersword_electric"'})
                if shopphase2 == 12:  buyweapon({"ID": '"coppersword_nature"'})
                if shopphase2 == 13:  buyweapon({"ID": '"goldensword"'})
                if shopphase2 == 14:  buyweapon({"ID": '"goldensword_fire"'})
                if shopphase2 == 15:  buyweapon({"ID": '"goldensword_ice"'})
                if shopphase2 == 16:  buyweapon({"ID": '"goldensword_water"'})
                if shopphase2 == 17:  buyweapon({"ID": '"goldensword_electric"'})
                if shopphase2 == 18:  buyweapon({"ID": '"goldensword_nature"'})
                if shopphase2 == 19:  buyweapon({"ID": '"diamondsword"'})
                if shopphase2 == 20:  buyweapon({"ID": '"diamondsword_fire"'})
                if shopphase2 == 21:  buyweapon({"ID": '"diamondsword_ice"'})
                if shopphase2 == 22:  buyweapon({"ID": '"diamondsword_water"'})
                if shopphase2 == 23:  buyweapon({"ID": '"diamondsword_electric"'})
                if shopphase2 == 24:  buyweapon({"ID": '"diamondsword_nature"'})            
            else:
                buy({"Cost": 100, "Command": '"function kcf:giveweapon {ID: \\"ironsword\\"}"'})
        elif self.buy == 13: 
            if level < 5:    
                buy({"Cost": 20, "Command": '"function kcf:giveweapon {ID: \\"coppersword_fire\\"}"'})
        elif self.buy == 14: 
            if level < 5:    
                buy({"Cost": 20, "Command": '"function kcf:giveweapon {ID: \\"coppersword_water\\"}"'}) 
        elif self.buy == 15: 
            if level < 5:    
                buy({"Cost": 20, "Command": '"function kcf:giveweapon {ID: \\"coppersword_electric\\"}"'})
        elif self.buy == 16: 
            if level < 5:    
                buy({"Cost": 20, "Command": '"function kcf:giveweapon {ID: \\"coppersword_nature\\"}"'})
def buy(Cost: int, Command: str):
    run('''
$scoreboard players set @s temp $(Cost)
execute if score @s coins < @s temp run tellraw @s [{"text": "You don't have enough coins! You need ", "color": "red"}, {"score": {"objective": "temp", "name": "@s"}}, {"text": " coins but you only have "}, {"score": {"objective": "coins", "name": "@s"}}, {"text": "!"}]
$execute if score @s coins >= @s temp run $(Command)
execute if score @s coins >= @s temp run tellraw @s [{"text": "Successfully bought for ", "color": "green"}, {"score": {"objective": "temp", "name": "@s"}}, {"text": " coins!"}]
execute if score @s coins >= @s temp run scoreboard players operation @s coins -= @s temp 
    ''')

def buyweapon(ID: str):
    run(f'''data modify storage kcf:functionargs Cost set from storage kcs:weapons {ID}.shopdata.Cost''')
    run(f"""data modify storage kcf:functionargs Command set value 'function kcf:giveweapon {{ID: "{ID}"}}'""")
    run('function kcf:buy with storage kcf:functionargs')

def stop():
    level = 0
    started = 0
    waiting = 0
    all.floor = 0
    kill('@e[type=!player,tag=!important]')
    kill('@e[type=item]')
    run('scoreboard objectives remove coins')
    run('bossbar set timer visible false')

    gamemode(all, adventure)
    tp(all, '8 4 8')

def start():
    spawnArena()
    wait('5t', start2)

def resetself():
    self.coins = 100

    self.defense = 200
    run('clear @s')

    run('xp set @s 0 levels')
    run('xp set @s 0')
    self.cscounter = 0

    removeStatuses()
    tickmodifiers()

    self.health = 500
    self.shields = 500

def start2():
    kill('@e[type=!player,tag=!important]')
    kill('@e[type=item]')
    level = 0
    started = 1
    waiting = 0
    textdisplays = 0
    gameiter += 1
    timelives = 3

    all.gameiter = gameiter

    # Delete coins to remove offline players' coins
    run('scoreboard objectives remove coins')
    run('scoreboard objectives add coins dummy {"text":"Coins","color":"gold"}')
    run('scoreboard objectives setdisplay sidebar coins')

    tp(all, '8 -60 8')
    newfloor()
    gamemode(all, adventure)
    run('clear @a')

    def giverandomstarting():
        randint(self.temp, 1, 5)
        if self.temp == 1: giveweapon({"ID": '"stonesword_fire"'})
        if self.temp == 2: giveweapon({"ID": '"stonesword_ice"'})
        if self.temp == 3: giveweapon({"ID": '"stonesword_water"'})
        if self.temp == 4: giveweapon({"ID": '"stonesword_electric"'})
        if self.temp == 5: giveweapon({"ID": '"stonesword_nature"'})

    effect(all, instant_health, 1, 14)
    effect(all, saturation, 1, 14)
    give(all, carrot, 48)
    
    execute('as @a', resetself)
    execute('as @a', tickmodifiers)

    wait('1t', execute('as @a at @s', giverandomstarting))

def newfloor():
    timeleft = 1800
    run('bossbar set timer players @a')
    showtimer({"timeleft": 1799})
    run('bossbar set timer visible true')

    level += 1
    all.floor = level
    print(f'#green#New round! You are now on floor {level}')

    # Set stats
    all.takeem = level

    arenaNumOfPlayers = 0
    execute('positioned 8 -60 8 as @a[distance=..24]', add(arenaNumOfPlayers, 1))

    # Hard difficulty: 2x mobs
    if difficulty == 3: 
        arenaNumOfPlayers *= 2

    # mobs
    for j in range(arenaNumOfPlayers):
        if level < 50:
            if level == 1:
                summon(zombie, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 2:
                summon(skeleton, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 3:
                for i in range(3): summon(skeleton, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 4:
                for i in range(6): summon(zombie, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 5:
                summon(pillager, '0 100 0', {'Tags': '[spawnNotDone, gigantic, waterPillager, elite, pillagerDone]', 'equipment': '{mainhand:{id: crossbow}}'})
            if level == 6:
                for i in range(3): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]', 'equipment': '{mainhand:{id: crossbow}}'})
            if level == 7:
                for i in range(2): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]', 'equipment': '{mainhand:{id: crossbow}}'})
                for i in range(3): summon(zombie, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 8:
                for i in range(4): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]', 'equipment': '{mainhand:{id: crossbow}}'})
            if level == 9:
                for i in range(8): summon(husk, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 10:
                summon(evoker, '0 100 0', {'Tags': '[spawnNotDone, boss, gigantic]'})
            if level == 11:
                for i in range(2): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]', 'equipment': '{mainhand:{id: crossbow}}'})
                for i in range(3): summon(skeleton, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 12:
                summon(stray, '0 100 0', {'Tags': '[spawnNotDone, gigantic, elite]'})
            if level == 13:
                for i in range(2): summon(blaze, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 14:
                for i in range(2): summon(evoker, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 15:
                summon(enderman, '0 100 0', {'Tags': '[spawnNotDone, elite]'})
            if level == 16:
                for i in range(2): summon(blaze, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(2): summon(stray, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 17:
                for i in range(2): summon(spider, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 18:
                for i in range(2): summon(blaze, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(2): summon(stray, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 19:
                for i in range(2): summon(phantom, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 20:
                summon(iron_golem, '0 100 0', {'Tags': '[spawnNotDone, boss]'})
            if level == 21:
                for i in range(3): summon(bee, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(zombie, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(husk, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 22:
                for i in range(5): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(5): summon(bee, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 23:
                for i in range(3): summon(spider, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(stray, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(5): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 24:
                for i in range(10): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 25:
                summon(bee, '0 100 0', {'Tags': '[spawnNotDone, titan, elite]'})
            if level == 26:
                for i in range(3): summon(phantom, '0 100 0', {'Tags': '[spawnNotDone, gigantic]'})
                for i in range(8): summon(zombie, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 27:
                summon(evoker, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(vindicator, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 28:
                for i in range(3): summon(blaze, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(stray, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 29:
                for i in range(3): summon(skeleton, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(stray, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(bogged, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 30:
                summon(ravager, '0 100 0', {'Tags': '[spawnNotDone, gigantic, boss]'})
            if level == 31:
                summon(ravager, '0 100 0', {'Tags': '[spawnNotDone, elite]'})
                for i in range(3): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(vindicator, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 32:
                summon(ravager, '0 100 0', {'Tags': '[spawnNotDone, elite]'})
                summon(evoker, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(vindicator, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 33:
                summon(iron_golem, '0 100 0', {'Tags': '[spawnNotDone, elite]'})
                for i in range(6): summon(bee, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(phantom, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 34:
                summon(iron_golem, '0 100 0', {'Tags': '[spawnNotDone, elite]'})
                for i in range(6): summon(bee, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(3): summon(blaze, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 35:
                summon(iron_golem, '0 100 0', {'Tags': '[spawnNotDone, boss, gigantic]'})
            if level == 36:
                for i in range(5): summon(husk, '0 100 0', {'Tags': '[spawnNotDone]'})
                for i in range(5): summon(zombie, '0 100 0', {'Tags': '[spawnNotDone]'})
            if level == 37:
                for i in range(5): summon(vindicator, '0 100 0', {'Tags': '[spawnNotDone]'})    
            if level == 38:
                summon(warden, '0 100 0', {'Tags': '[spawnNotDone]'})             
            if level == 39:
                summon(spider, '0 100 0', {'Tags': '[spawnNotDone]'})            
                summon(zombie, '0 100 0', {'Tags': '[spawnNotDone]'})  
                summon(skeleton, '0 100 0', {'Tags': '[spawnNotDone]'})            
                summon(husk, '0 100 0', {'Tags': '[spawnNotDone]'})            
                summon(stray, '0 100 0', {'Tags': '[spawnNotDone]'})            
                summon(bogged, '0 100 0', {'Tags': '[spawnNotDone]'})            
                summon(pillager, '0 100 0', {'Tags': '[spawnNotDone]'})            
                summon(vindicator, '0 100 0', {'Tags': '[spawnNotDone]'})            

            if level == 40:
                summon(pillager, '0 100 0', {'Tags': '[spawnNotDone, gigantic, naturePillager, boss, pillagerDone, titan]', 'equipment': '{mainhand:{id: crossbow, components: {unbreakable: {},enchantments: {multishot: 10}}}}'})

        run('spreadplayers 8 8 8 16 under -32 false @e[tag=spawnNotDone]')
        # Sometimes it might fail, in that case, just TP to mid
        wait('1t', execute('positioned 0 100 0', teleport('@e[tag=spawnNotDone,distance=..3]', '8 -58 8')))


        removetag('@e[tag=spawnNotDone]', 'spawnNotDone')

    # Wait 1 tick to prevent bug of shop phase starting
    wait('1t', set(waiting, 0))

def removeStatuses():
    self.viral = 0
    self.magnetized = 0
    self.corrosion = 0
    self.electrified = 0
    self.burning = 0
    self.frozen = 0
    self.acidified = 0

    self.fire = 0
    self.ice = 0
    self.water = 0
    self.electric = 0
    self.nature = 0
    self.fireS = 0
    self.iceS = 0
    self.waterS = 0
    self.electricS = 0
    self.natureS = 0


def onrespawn():
    tickmodifiers()
    self.shields = self.max_shields
    self.health = self.max_health

    self.invincible = 100
    effect(self, resistance, 'infinite', 4, True)
    effect(self, saturation, 'infinite', 0, True)

    # Remove statuses
    removeStatuses()


'''
// Add damage CD bypasses
# damage_type_tag minecraft:bypasses_cooldown
{
    "values": [
        "minecraft:mob_attack",
        "minecraft:magic",
        "minecraft:indirect_magic",
        "minecraft:arrow",
        "minecraft:outside_border",
        "minecraft:out_of_world",
        "minecraft:explosion",
        "minecraft:dragon_breath",
        "minecraft:mob_projectile",
        "minecraft:lightning_bolt",
        "minecraft:player_attack"
    ]
}
'''