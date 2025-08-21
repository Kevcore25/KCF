from KCFSyntax import *
_damagedEntity = "@n[nbt={HurtTime:10s},tag=!self]"

_player = "@s[type=player]"
_debugger = "@a[tag=debug]"

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

def dokill():
    if entity(_player):
        run('damage @s 2 out_of_world')
        self.health = self.max_health
        self.shields = self.max_shields
    elif entity('@s[tag=!notmob]'):
        kill(self)

def load():
    var('atk', 'custom:damage_dealt')
    var('dmgtaken', 'custom:damage_resisted')

    var('xpos')
    var('ypos')
    var('zpos')

    sec()
    tick10()

    trigger('stats')

def triggers__stats():
    run('tellraw @s ["",{"text":"Player Bonus Stats:","color":"aqua"},{"text":"\\n"},{"text":"Base DMG: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.dmgbonus"},"color":"green"},{"text":"%","color":"green"},{"text":" | Elemental Mastery: ","color":"light_purple"},{"score":{"name":"@s","objective":"em"},"color":"green"},{"text":"\\n"},{"text":"Status Chance: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.status"},"color":"green"},{"text":"%","color":"green"},{"text":"\\n"},{"text":"Critical Chance: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.cr"},"color":"green"},{"text":"%","color":"green"},{"text":" | Critical Damage: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.cd"},"color":"green"},{"text":"%","color":"green"},{"text":"\\n"},{"text":"Attack Speed: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.atkspd"},"color":"green"},{"text":"%","color":"green"},{"text":"\\n"},{"text":"Bonus Elemental DMG:","color":"aqua"},{"text":"\\n"},{"text":"Fire: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.fire"},"color":"green"},{"text":"%","color":"green"},{"text":" | Ice: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.ice"},"color":"green"},{"text":"%","color":"green"},{"text":" | Water: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.water"},"color":"green"},{"text":"%","color":"green"},{"text":"\\nElectric: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.electric"},"color":"green"},{"text":"%","color":"green"},{"text":" | Nature: ","color":"light_purple"},{"text":"+","color":"green"},{"score":{"name":"@s","objective":"stat.nature"},"color":"green"},{"text":"%","color":"green"},{"text":"\\n "}]')

def giveweapon(Item, Name, Description, DMG, CR, CD, ATKSPD, Status, Fire, Ice, Water, Electric, Nature):
    run(f'give @s {Item}[custom_name=[{{"text":"{Name}","italic":false}}],lore=[[{{"text":"{Description}","italic":false,"color":"gray"}}],"",[{{"text":"Base DMG: {DMG}","italic":false,"color":"gray"}}],[{{"text":"Base Status: {Status}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Chance: {CR}%","italic":false,"color":"gray"}}],[{{"text":"Base Critical Damage: {CD}%","italic":false,"color":"gray"}}],[{{"text":"Base Attack Speed: {ATKSPD}/s","italic":false,"color":"gray"}}]],custom_data={{DMG: {DMG}, CR: {CR}, CD: {CD}, ATKSPD: {ATKSPD}, Status: {Status}, Fire: {Fire}, Ice: {Ice}, Water: {Water}, Electric: {Electric}, Nature: {Nature}}},attribute_modifiers=[{{type:attack_damage,amount:-0.9,slot:mainhand,id:"251",operation:add_value}},{{type:attack_speed,amount:-4,slot:mainhand,id:"252",operation:add_value}},{{type:attack_speed,amount:{ATKSPD},slot:mainhand,id:"253",operation:add_value}}]]')

def everyelemsword():
    giveweapon({
        'Item': '"iron_sword"',
        'Name': '"FIRE Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30,
        "CR": 25,
        "CD": 50,
        "ATKSPD": 1.6,
        "Status": 75,
        "Fire": 1,
        "Ice": 0,
        "Water": 0,
        "Electric": 0,
        "Nature": 0
    })
    giveweapon({
        'Item': '"iron_sword"',
        'Name': '"ICE Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30,
        "CR": 25,
        "CD": 50,
        "ATKSPD": 1.6,
        "Status": 75,
        "Fire": 0,
        "Ice": 1,
        "Water": 0,
        "Electric": 0,
        "Nature": 0
    })
    giveweapon({
        'Item': '"iron_sword"',
        'Name': '"WATER Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30,
        "CR": 25,
        "CD": 50,
        "ATKSPD": 1.6,
        "Status": 75,
        "Fire": 0,
        "Ice": 0,
        "Water": 1,
        "Electric": 0,
        "Nature": 0
    })
    giveweapon({
        'Item': '"iron_sword"',
        'Name': '"Electric Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30,
        "CR": 25,
        "CD": 50,
        "ATKSPD": 1.6,
        "Status": 75,
        "Fire": 0,
        "Ice": 0,
        "Water": 0,
        "Electric": 1,
        "Nature": 0
    })
    giveweapon({
        'Item': '"iron_sword"',
        'Name': '"NATURE Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30,
        "CR": 25,
        "CD": 50,
        "ATKSPD": 1.6,
        "Status": 75,
        "Fire": 0,
        "Ice": 0,
        "Water": 0,
        "Electric": 0,
        "Nature": 1
    })
def everyelem():
    giveweapon({
        'Item': '"iron_sword"',
        'Name': '"EVERY ELEMENT Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 30,
        "CR": 25,
        "CD": 50,
        "ATKSPD": 1.6,
        "Status": 33,
        "Fire": 1,
        "Ice": 1,
        "Water": 1,
        "Electric": 1,
        "Nature": 1
    })
def givebasic():
    giveweapon({
        'Item': '"iron_sword"',
        'Name': '"Basic Sword"',
        "Description": '"Basic sword for testing"',
        "DMG": 100,
        "CR": 50,
        "CD": 50,
        "ATKSPD": 1.6,
        "Status": 50,
        "Fire": 0,
        "Ice": 1,
        "Water": 0,
        "Electric": 0,
        "Nature": 0
    })
def diamondsword():
    giveweapon({
        'Item': '"diamond_sword"',
        'Name': '"Diamond Sword"',
        "Description": '"Diamond Sword with the Ice status"',
        "DMG": 200,
        "CR": 25,
        "CD": 120,
        "ATKSPD": 1.6,
        "Status": 20,
        "Fire": 0,
        "Ice": 1,
        "Water": 0,
        "Electric": 0,
        "Nature": 0
    })

def displayreactionm(Name: str, Color: str, x: float, y: float, z: float):
    run(f'execute at @s positioned ~{x} ~{y} ~{z} run summon text_display ^ ^ ^ {{Tags:[notmob,dmgtext],teleport_duration:0,start_interpolation:-1,interpolation_duration:0,transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}, billboard:"center",see_through:1b,text:{{"color":"{Color}","text":"{Name}","bold":true}},background:268435456,glow_color_override:1b,Glowing:1b, shadow: 1b}}')

def displayreaction(Name: str, Color: str):
    run(f'data modify storage kcf:functionargs Name set value "{Name}"')
    run(f'data modify storage kcf:functionargs Color set value "{Color}"')
    run('''
execute store result storage kcf:functionargs x float 0.1 run random value -6..6
execute store result storage kcf:functionargs y float 0.1 run random value 10..16
execute store result storage kcf:functionargs z float 0.1 run random value -6..6

function kcf:displayreactionm with storage kcf:functionargs
    ''')

def displaydmg(Symbol: str, takedmg: int, Color: str):
    if 'entity @s[tag=notmob]': return
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
    
    

def displaydmgM(Symbol: str, takedmg: int, Color: str, x: float, y: float, z: float):
    run(f'execute at @s positioned ~{x} ~{y} ~{z} run summon text_display ^ ^ ^ {{Tags:[notmob,notDone,dmgtext],teleport_duration:0,start_interpolation:-1,interpolation_duration:0,transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}, billboard:"center",see_through:1b,text:{{"color":"{Color}","text":"{Symbol} {takedmg}","bold":false}},background:268435456,glow_color_override:1b,Glowing:1b, shadow: 1b}}')
def displaydmgMD(Symbol: str, dec: int, whole: int, Color: str, x: float, y: float, z: float, compactLetter: str):
    run(f'execute at @s positioned ~{x} ~{y} ~{z} run summon text_display ^ ^ ^ {{Tags:[notmob,notDone,dmgtext],teleport_duration:0,start_interpolation:-1,interpolation_duration:0,transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.5f,0.5f,0.5f]}}, billboard:"center",see_through:1b,text:{{"color":"{Color}","text":"{Symbol} {whole}.{dec}{compactLetter}","bold":false}},background:268435456,glow_color_override:1b,Glowing:1b, shadow: 1b}}')


def elementEffects():
    if self.fire > 0 and not entity('@s[type=blaze]'):
        # Blaze: immune
            
        self.takedmg = 2 * self.takeem * self.fireS

        # Zombie: 7x effectiveness
        if entity('@s[type=zombie]'):
            self.takedmg *= 7

        doReactionDMG()
    if self.ice > 0:
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

    if self.nature > 0:
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

        doReactionDMG()

        self.electrified -= 1

    if self.viral > 0:
        self.takedmg = 20 * self.takeem
        doReactionDMG()

        if entity(_player):
            "@a[distance=1.1..2.5]".takedmg = self.takedmg / 2
            execute("as @a[distance=1.1..2.5]", doReactionDMG)
        else:
            "@e[type=!player,distance=1.1..2.5]".takedmg = self.takedmg / 2
            execute("as @e[type=!player, distance=1.1..2.5]", doReactionDMG)

        self.viral -= 1

def elementEffects10t():
    # Burning
    if self.burning > 0:
        self.takedmg = 8 * self.takeem

        # Shield = 2x less
        if self.shields > 0:
            self.takedmg /= 2

        doFireDMG() # DO FIRE DMG, not reaction DMG
        run('particle minecraft:flame ~ ~0.6 ~ 0.2 0.3 0.2 0 5 normal @a')

        self.burning -= 1


def tick10():
    schedule('10t', tick10)
    execute('as @e at @s', elementEffects10t)

def endermanEffects():
    # Enderman ice status
    self.ice = 20
    self.iceS = 1

    # Enderman Magnetic effect
    execute('as @a[distance=..2.5]', set(self.takedmg, 5))
    execute('as @a[distance=..2.5]', mult(self.takedmg, self.takeem))
    execute('as @a[distance=..2.5]', set(self.iceS, 1))
    execute('as @a[distance=..2.5]', doElectricDMG)


def sec():
    schedule('1s', sec)

    effect(all, resistance, 10, 4, True)

    execute('as @e at @s', elementEffects)

    # Enderman ice status
    execute('as @e[type=enderman] at @s', endermanEffects)
    execute('as @e[type=stray]', set('self.iceS', 1))
    execute('as @e[type=stray]', set('self.ice', 20))
    execute('as @e[type=blaze]', set('self.fireS', 1))
    execute('as @e[type=blaze]', set('self.fire', 20))
    execute('as @a', tickrelics)



def rollFire():
    store(self.rolltemp, getdata(self, 'SelectedItem.components."minecraft:custom_data".Fire'))    
    
    self.rolltemp2 = 0
    if self.rolltemp == 1:
        randint(self.rolltemp, 0, 10000)     
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
        randint(self.rolltemp, 0, 10000)        
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
        randint(self.rolltemp, 0, 10000)        
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
        randint(self.rolltemp, 0, 10000)        
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
        randint(self.rolltemp, 0, 10000)        
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
    
    # Calc based on stats
    self.cr *= (100 + self.tempcr)

    randint(self.rolltemp, 0, 10000)    
    tellraw(_debugger, f"#yellow#CRIT RATE: {self.cr} > {self.rolltemp}")

    if self.cr > self.rolltemp:
        # Get CD
        store(self.cd, getdata(self, 'SelectedItem.components."minecraft:custom_data".CD')) # e.g. 50%
        # CD = WCD + WCD * CD

        self.tempcd = self.stat.cd

        # Frozen bonus
        if _damagedEntity.frozen > 0:
            self.tempcd += 4 * self.em * self.iceS

        self.cd += self.cd * self.tempcd / 100
        self.cd += 100
        tellraw(_debugger, f"#yellow#CRIT DMG Multiplier: {self.cd}x")
        # Assume, CD = 50%, statCD = 100%
        # 50% += 50% * 100% / 100
        # 50% += 50%
        # 100%, expected result

        # Multiply DMG 
        self.dmg *= self.cd
        self.dmg /= 100
        run('data modify storage kcf:functionargs Color set value "yellow"')
    else:
        run('data modify storage kcf:functionargs Color set value "white"')

# DMG

def doDMG():
    doFinalDMG()
    run('data modify storage kcf:functionargs Color set value "white"')

def defcalc():
    self.tempdefense = self.defense

    # Fire reduction
    self.tempdefense -= self.takeem * self.fireS * 3

    # Corrosive reduction
    if self.corrosion > 0:
        self.tempdefense *= 100 - (45 + self.takeem)
        self.tempdefense /= 100

    # Burning reduction
    if self.burning > 0:
        self.tempdefense *= 100 - (28 + self.takeem)
        self.tempdefense /= 100

    # Reduction
    self.reduc = 50000 / (self.tempdefense + 500)

    # Can't be negative or 0!!
    if self.reduc < 1:
        self.reduc = 1

    self.takedmg *= self.reduc
    self.takedmg /= 100

def doFinalDMG():
    self.shieldCD = 40
    
    if self.invincible > 0:
        return
    
    # Do SHIELD DMG
    if self.shields > 0:
        run('data modify storage kcf:functionargs Color set value "aqua"')

        # Magnetized: 2x dmg
        if self.magnetized > 0:
            self.takedmg *= (10 + 2 * self.takeem)
            self.takedmg /= 10
      
        self.takedmg /= 2
        self.sgduration = 20 * self.shields / self.max_shields
        self.shields -= self.takedmg

        if self.shields <= 0:   # Spider: Instant Die
            if entity('@s[type=spider]'):
                self.takedmg = self.health
                doVoidDMG()
            else:
                if entity(_player):
                    times(self, 2, 10, 5)
                    title(self, f"#aqua#<<                    >>")
                    subtitle(self, "")
                self.shields = 0
                # Set Invcilibabiltiy
                self.invincible = self.sgduration
                self.invincible += 1
    
    # DO HEALTH DMG
    else:
        # Evoker: +1000% health DMG
        if entity('@s[type=evoker]'):
            self.takedmg *= 10

        # Reduce defense from EM
        defcalc()

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

    if not entity(_player):
        "@a[distance=..10]".dmgdealt += self.takedmg

    if self.takedmg > 0:
        # displaydmg(Symbol, Color, self.takedmg)
        run('execute store result storage kcf:functionargs takedmg int 1 run scoreboard players get @s takedmg')
        run('function kcf:displaydmg with storage kcf:functionargs')
    tellraw(_debugger, f"Final DMG: {self.takedmg}")
    run('damage @s 0.01')
    showhp()



def doVoidDMG():
    self.shieldCD = 40
    if self.invincible > 0:
        return
    
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
    self.shieldCD = 40
    if self.invincible > 0:
        return
    
    # Spider: 3x more HP DMG
    if entity('@s[type=spider]'):
        self.takedmg *= 3

    ## DEFENSE
    defcalc()

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

    if self.invincible > 0:
        dninv(self.healthpct, self.shieldpct)
    else:
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

        displayname(self.healthpct, self.shieldpct, healthcolor)

def doReactionDMG():
    # Blaze: 50% reduction
    if entity('@s[type=blaze]'):
        self.takedmg /= 2

    run('data modify storage kcf:functionargs Symbol set value "🧪"')
    doDMG()

def doPhysDMG():

    # Skeleton: 2x effectiveness
    if entity('@s[type=skeleton]'):
        self.takedmg *= 2
    # Iron Golem: 90% reduction
    if entity('@s[type=iron_golem]'):
        self.takedmg /= 10

    run('data modify storage kcf:functionargs Symbol set value "🗡"')
    doDMG()

def doFireDMG():
    self.fire = 60
    self.fireS += 1

    if self.fireS > 10: self.fireS = 10

    # Skeleton/Husk: 50% reduction
    if entity('@s[type=skeleton]') or entity('@s[type=husk]'):
        self.takedmg /= 2
    # BLaze: 80% reduction
    if entity('@s[type=blaze]'):
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

    # Max 7 stacks
    if self.iceS > 7: self.iceS = 7

    # Enderman/Stray: 80% less
    if entity('@s[type=enderman]') or entity('@s[type=stray]'):
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

    # Max 5 stacks
    if self.electricS > 5: 
        self.electricS = 5
        self.electric = 80
    
    run('data modify storage kcf:functionargs Symbol set value "⚡"')
    doDMG()


def doNatureDMG():
    self.nature = 60
    self.natureS += 1
    run('data modify storage kcf:functionargs Symbol set value "🦠"')
    doDMG()



def calcPlayerWeaponDamage():
    # Calculates player DMG for weapon
    # Net DMG = (Base DMG) * (Bonus base DMG | 100)
    store(self.dmg, getdata(self, 'SelectedItem.components."minecraft:custom_data".DMG'))
    self.dmg *= (100 + self.stat.dmgbonus)
    self.dmg /= 100

    # Get the status
    store(self.status, getdata(self, 'SelectedItem.components."minecraft:custom_data".Status'))
    self.status *= 100 + self.stat.status # Scaled to 100x. so 10000 = 100%

    # Elements
    self.gotamt = 0
    store(self.gotfire, rollFire)

    if self.gotfire == 1: 
        self.dmg *= (100 + self.stat.fire)
        self.dmg /= 100

        self.gotamt += 1
    store(self.gotice, rollIce)
    if self.gotice == 1: 
        self.dmg *= (100 + self.stat.ice)
        self.dmg /= 100
        self.gotamt += 1

    store(self.gotwater, rollWater)
    if self.gotwater == 1: 
        self.dmg *= (100 + self.stat.water)
        self.dmg /= 100
        self.gotamt += 1
    store(self.gotelectric, rollElectric)
    if self.gotelectric == 1: 
        self.dmg *= (100 + self.stat.electric) 
        self.dmg /= 100
        self.gotamt += 1
    store(self.gotnature, rollNature)
    if self.gotnature == 1: 
        self.dmg *= (100 + self.stat.nature)
        self.dmg /= 100
        self.gotamt += 1

    # Apply criticals
    calcCriticals()

    _damagedEntity.takedmg = self.dmg
    _damagedEntity.takeem = self.em

    if self.gotamt >= 1:
        if self.gotfire == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doFireDMG)
        elif self.gotice == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doIceDMG)
        elif self.gotwater == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doWaterDMG)
        elif self.gotelectric == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doElectricDMG)
        elif self.gotnature == 1: execute('as @n[nbt={HurtTime:10s},tag=!self]', doNatureDMG)

    else:
        execute('as @n[nbt={HurtTime:10s},tag=!self]', doPhysDMG)


def displayname(healthpct: int, shieldpct: int, healthcolor: int):
    run(f'data modify entity @s CustomName set value [{{"color":"{healthcolor}","text":"♥{healthpct}%"}},{{"color":"gray","text":" | "}},{{"color":"blue","text":"⛊{shieldpct}%"}}]')
def dninv(healthpct: int, shieldpct: int):
    run(f'data modify entity @s CustomName set value [{{"color":"dark_gray","text":"♥{healthpct}%"}},{{"color":"gray","text":" | "}},{{"color":"dark_gray","text":"⛊{shieldpct}%"}}]')

def applyElectrified():
    self.electrified += 4
    if self.electrified > 12:
        self.electrified = 12

def genericEntityTick():
    # Generic shields and stuff

    if "entity @s[tag=!done]":
        onnewentity()

    if self.invincible > 0:
        self.invincible -= 1

    # Regen shield
    if not self.water > 0 and not self.magnetized > 0:
        if self.shields < self.max_shields and self.shieldCD == 0:
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

            doPhysDMG()
        
        # Heal
        if not entity(_player):
            if self.health > 0:
                run('data modify entity @s Health set value 1024')
        else:
            self.dmgtaken = 0

        # Electric
        if self.electric > 0:
            self.takedmg = 2 * self.takeem * self.electricS
            doReactionDMG()
            # Spread
            if entity(_player):
                "@a[distance=1.1..2.5]".takedmg = self.takedmg
                execute('as @a[distance=1.1..2.5]', doReactionDMG)
            else:
                "@e[type=!player,tag=!notmob,distance=1.1..2.5]".takedmg = self.takedmg
                execute('as @e[type=!player,tag=!notmob,distance=1.1..2.5]', doReactionDMG)
        # Water
        if self.water > 0:
            # IF MOB
            if entity('@s[type=!player]'):
                "@a[distance=..4]".health += self.takeem * self.waterS / 5
                self.health += self.takeem / 5 * 2
            else:
                "@e[type=!player,distance=..4]".health += self.takeem * self.waterS
                self.health += self.takeem / 5

        self.shieldCD = 40
        showhp()

        # Fix duplicate bug
        if not entity(_player):
            self.dmgtaken = 0

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
            # BLOOM
            displayreaction({"Name": '"🪷 Bloom"', "Color": '"green"'})

    if self.natureS > 0:
        if self.fireS > 0:
            # BURNING
            self.burning += 8 # loses 1 per tick, so 4 / 0.5 = 6
            if self.burning > 24: self.burning = 24
            displayreaction({"Name": '"🔥 Burning"', "Color": '"gold"'})
            # Remove a stack
            self.fireS -= 1; self.natureS -= 1

        if self.natureS > 0 and self.iceS > 0:
            # VIRAL
            self.viral += 4
            if self.viral > 12: self.viral = 12
            displayreaction({"Name": '"🦠 Viral"', "Color": '"#16bf8b"'})
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

    ## REACTION TICKS

    # Magnetic status
    if self.magnetized > 0:
        self.magnetized -= 1
        run('particle minecraft:firework ~ ~1.2 ~ 0.2 0.1 0.2 0 5 normal @a')

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
        execute('as @e[type=!evoker,type=!evoker_fangs,tag=!notmob,type=!vex,distance=..1.5]', set(self.takedmg, 50))
        execute('as @e[type=!evoker,type=!evoker_fangs,tag=!notmob,type=!vex,distance=..1.5]', set(self.electricS, 1))
        execute('as @e[type=!evoker,type=!evoker_fangs,tag=!notmob,type=!vex,distance=..1.5]', multiply(self.takedmg, self.takeem))
        execute('as @e[type=!evoker,type=!evoker_fangs,tag=!notmob,type=!vex,distance=..1.5]', doNatureDMG)

def onnewentity():
    tag(self, 'done')
    tag(self, 'mob')
    if entity('@s[type = zombie]'):
        self.max_health = 1200
        self.defense = 850
        self.max_shields = 0
    elif entity('@s[type = husk]'):
        self.max_health = 1000
        self.defense = 1000
        self.max_shields = 0
    elif entity('@s[type = skeleton]'):
        self.max_health = 500
        self.defense = 0
        self.max_shields = 1000
    elif entity('@s[type = pillager]'):
        self.max_health = 500
        self.defense = 200
        self.max_shields = 250
    elif entity('@s[type = evoker]'):
        self.max_health = 4000
        self.defense = 200
        self.max_shields = 1000
        attribute(self, scale, 1.25)
    elif entity('@s[type = iron_golem]'):
        self.max_health = 2000
        self.defense = 2000
        self.max_shields = 10000
    elif entity('@s[type = spider]'):
        self.max_health = 50
        self.defense = 0
        self.max_shields = 100
        attribute(self, scale, 0.25)
        if entity('@s[tag=!child]'):
            for i in range(4):
                summon(spider, '~ ~ ~', {'Tags': '[child]'})
    elif entity('@s[type = stray]'):
        self.max_health = 650
        self.defense = 400
        self.max_shields = 1000
        tag(self, 'nofreeze')
    elif entity('@s[type = enderman]'):
        self.max_health = 600
        self.defense = 200
        self.max_shields = 1200
    elif entity('@s[type = blaze]'):
        self.max_health = 450
        self.defense = 700
        self.max_shields = 600
    else:
        removetag(self, 'mob')

        store(self.max_health, run('attribute @s max_health get 25'))
        store(self.max_shields, run('attribute @s max_health get 25'))

        store(self.temp, run('attribute @s attack_damage get 25'))
        self.max_shields += self.temp


        store(self.defense, run('attribute @s armor get 50'))
        self.defense += 200

    store(self.em, run('attribute @s attack_damage get'))
    self.takeem = 5

    # HP
    attribute(self, max_health, 1024)
    run('data modify entity @s Health set value 1024')
    self.health = self.max_health
    self.shields = self.max_shields

    # No KB
    attribute(self, knockback_resistance, 0.9)


    run('data modify entity @s CustomNameVisible set value 1b')


def onnewjoin():
    tag(self, 'done')

    self.max_health = 500
    self.max_shields = 500
    self.health = 500
    self.shields = 500
    self.defense = 200
    self.em = 5

def playertick():

    if self.atk > 0:
        # tag self to not take dmg by self
        tag(self, 'self')

        # get entity damaged
        calcPlayerWeaponDamage()

        removetag(self, 'self')

        self.atk = 0

    # Health
    if self.invincible > 0:
        actionbar(self, f"#dark_gray#Health: {self.health}/{self.max_health}#gray# | #dark_gray#Shields: #dark_gray#{self.shields: var | dark_gray}#dark_gray#/{self.max_shields: var | dark_gray}")
    else:
        actionbar(self, f"#red#Health: {self.health}/{self.max_health}#gray# | #aqua#Shields: #aqua#{self.shields: var | aqua}#aqua#/{self.max_shields: var | aqua}")

def onfuncs():
    playertick()


def dmgtextanimation():
    self.temp += 1

    # if self.temp == 4: run('data modify entity @s transformation.scale set value [1f,1f,1f]')
    if self.temp == 5: run('data modify entity @s text_opacity set value -1')
    if self.temp == 4: run('data modify entity @s text_opacity set value -64')
    if self.temp == 3: run('data modify entity @s text_opacity set value -128')
    if self.temp == 2: run('data modify entity @s text_opacity set value 64')
    if self.temp == 1: run('data modify entity @s text_opacity set value 16')

    if self.temp == 21: run('data modify entity @s text_opacity set value -1')
    if self.temp == 22: run('data modify entity @s text_opacity set value -32')
    if self.temp == 23: run('data modify entity @s text_opacity set value -64')
    if self.temp == 24: run('data modify entity @s text_opacity set value -96')
    if self.temp == 25: run('data modify entity @s text_opacity set value -128')
    if self.temp == 26: run('data modify entity @s text_opacity set value 96')
    if self.temp == 27: run('data modify entity @s text_opacity set value 64')
    if self.temp == 28: run('data modify entity @s text_opacity set value 32')
    if self.temp == 29: run('data modify entity @s text_opacity set value 16')
    if self.temp == 30: 
        kill(self)

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
def applystats():
    # selector: relic
    randint(self.times, 16, 24)
    for i in range(self.times):
        # Random Stat
        randint('self.stat', 0, 10)

        if self.stat == 0:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+10% Base DMG", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".BaseDMG'))
            self.temp += 15
            run('execute store result entity @s Item.components."minecraft:custom_data".BaseDMG int 1 run scoreboard players get @s temp')
        elif self.stat == 1:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+10% Critical Chance", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".CR'))
            self.temp += 10
            run('execute store result entity @s Item.components."minecraft:custom_data".CR int 1 run scoreboard players get @s temp')
        elif self.stat == 2:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+10% Critical Damage", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".CD'))
            self.temp += 10
            run('execute store result entity @s Item.components."minecraft:custom_data".CD int 1 run scoreboard players get @s temp')
        elif self.stat == 3:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+1 Elemental Mastery", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".EM'))
            self.temp += 1
            run('execute store result entity @s Item.components."minecraft:custom_data".EM int 1 run scoreboard players get @s temp')
        elif self.stat == 4:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+1 Elemental Mastery", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".EM'))
            self.temp += 1
            run('execute store result entity @s Item.components."minecraft:custom_data".EM int 1 run scoreboard players get @s temp')
        elif self.stat == 5:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+10% Status Rate", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".Status'))
            self.temp += 10
            run('execute store result entity @s Item.components."minecraft:custom_data".Status int 1 run scoreboard players get @s temp')
        elif self.stat == 6:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+5% Fire DMG Bonus", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".Fire'))
            self.temp += 5
            run('execute store result entity @s Item.components."minecraft:custom_data".Fire int 1 run scoreboard players get @s temp')
        elif self.stat == 7:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+5% Ice DMG Bonus", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".Ice'))
            self.temp += 5
            run('execute store result entity @s Item.components."minecraft:custom_data".Ice int 1 run scoreboard players get @s temp')
        elif self.stat == 8:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+5% Water DMG Bonus", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".Water'))
            self.temp += 5
            run('execute store result entity @s Item.components."minecraft:custom_data".Water int 1 run scoreboard players get @s temp')
        elif self.stat == 9:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+5% Electric DMG Bonus", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".FiElectricre'))
            self.temp += 5
            run('execute store result entity @s Item.components."minecraft:custom_data".Electric int 1 run scoreboard players get @s temp')
        elif self.stat == 10:
            run('data modify entity @s Item.components."minecraft:lore" append value {"color": "aqua", "text": "+5% Nature DMG Bonus", "italic": false}')
            store('self.temp', getdata(self, 'Item.components."minecraft:custom_data".Nature'))
            self.temp += 5
            run('execute store result entity @s Item.components."minecraft:custom_data".FiNaturere int 1 run scoreboard players get @s temp')

    run('data modify entity @s PickupDelay set value 0')


def tickrelics():
    # Selector: player
    store(self.stat.dmgbonus, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".BaseDMG'))
    store(self.stat.cr, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".CR'))
    store(self.stat.cd, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".CD'))
    store(self.em, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".EM'))
    store(self.stat.status, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".Status'))

    store(self.stat.fire, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".Fire'))
    store(self.stat.ice, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".Ice'))
    store(self.stat.water, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".Water'))
    store(self.stat.electric, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".Electric'))
    store(self.stat.nature, getdata(self, 'Inventory[{Slot:9b}].components."minecraft:custom_data".Nature'))

    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".BaseDMG'))
    self.stat.dmgbonus += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".CR'))
    self.stat.cr += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".CD'))
    self.stat.cd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".EM'))
    self.em += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".Status'))
    self.stat.status += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".Fire'))
    self.stat.fire += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".Ice'))
    self.stat.ice += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".Water'))
    self.stat.water += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".Electric'))
    self.stat.electric += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:18b}].components."minecraft:custom_data".Nature'))
    self.stat.nature += self.temp

    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".BaseDMG'))
    self.stat.dmgbonus += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".CR'))
    self.stat.cr += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".CD'))
    self.stat.cd += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".EM'))
    self.em += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".Status'))
    self.stat.status += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".Fire'))
    self.stat.fire += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".Ice'))
    self.stat.ice += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".Water'))
    self.stat.water += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".Electric'))
    self.stat.electric += self.temp
    store(self.temp, getdata(self, 'Inventory[{Slot:27b}].components."minecraft:custom_data".Nature'))

    self.em += 5


def summonrelic():
    run('summon item ~ ~ ~ {Tags:[relicNotDone],PickupDelay:100,Item:{id:"minecraft:coal",count:1,components:{"minecraft:custom_data":{},"minecraft:lore":[{"color":"light_purple","text":"Relic Stats:", "italic": false}]}}}')
    execute('as @n[type=item,tag=relicNotDone]', applystats)


def tick():
    execute('as @e[tag=!notmob] at @s', genericEntityTick)
    execute('as @e[type=text_display,tag=dmgtext]', dmgtextanimation)
    execute('as @e[tag=ww] at @s', ww)

    
def onrespawn():
    self.shields = self.max_shields
    self.health = self.max_health

