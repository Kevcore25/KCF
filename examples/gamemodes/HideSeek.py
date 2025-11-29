from KCFSyntax import *

_seekers = "@a[team=hunter]"
_hiders = "@a[team=player]"

def load():
    sec()

    # Add teams
    run("team add hunter")
    run("team add player")

    # Set gamerules
    run('gamerule doTileDrops false')
    run('gamerule doMobSpawning false')
    run('gamerule fallDamage false')
    run('gamerule reducedDebugInfo true')

    # Add a start trigger
    trigger('start')

    # Add color changing trigger - it is custom
    var('colour', 'trigger')

def triggers__start():
    if gamestart == 1:
        tellraw(self, f"#red#The game already started!")
    else:
        tellraw(self, f"#green#Starting...")
        start()

def tick():
    # Executes every tick

    # Check if an arrow is at the ground
    # Explode if it is.
    execute('as @e[type=spectral_arrow, nbt={inGround:1b}] at @s', lambda: summon('tnt', '~ ~ ~', {'explosion_power': 6, 'fuse': 0}))
    execute('as @e[type=arrow, nbt={inGround:1b}] at @s', lambda: summon('tnt', '~ ~ ~', {'explosion_power': 3, 'fuse': 0}))
    kill('@e[type=spectral_arrow, nbt={inGround:1b}]')
    kill('@e[type=arrow, nbt={inGround:1b}]')

def giveseekstuff():
    give(_seekers, arrow, 6)
    give(_seekers, spectral_arrow, 1)
    give(_seekers, wind_charge, 32)
    give(_seekers, ender_pearl, 4)
    give(_seekers, diamond_sword)

def freeze():
    attribute(self, movement_speed, 0)
    attribute(self, jump_strength, 0)

def freezehiders():
    execute("as @a[team=player]", freeze)

def start2():
    # Worldborder
    run("worldborder center ~ ~")
    run("worldborder set 50")

    # Tp others
    tparound(all, 15, 25)

    # set timer
    timer = 60
    execute('as @a', add('timer', 30))

    gamestart = 1
    
    execute('as @a', lambda: resetattribute(self, scale))

    removetag(all, 'died')

    # random player get hunter
    run("team join player @a")
    run("team join hunter @r")

    give(all, bow)

    wait('14s', giveseekstuff)

    run('give @a[team=player] tipped_arrow[potion_contents={custom_color:11546150,custom_effects:[{id:blindness,duration:700,amplifier:0},{id:slowness,duration:600,amplifier:4},{id:glowing,duration:600,amplifier:1}]}] 1')

    # Attributes must be one selector only
    execute('as @a[team=player]', lambda: attribute(self, scale, 0.5))
    execute('as @a[team=player]', lambda: attribute(self, max_health, 6))
    execute('as @a[team=player]', lambda: resetattribute(self, attack_damage))
    execute('as @a[team=player]', lambda: resetattribute(self, attack_speed))
    execute('as @a[team=hunter]', lambda: attribute(self, attack_speed, 10))
    execute('as @a[team=hunter]', lambda: attribute(self, attack_damage, 10))

    effect(_seekers, blindness, 16)
    effect(_seekers, slowness, 15, 5)

    effect(_seekers, speed, 1000, 1, True)

    effect(all, saturation, 100000, 0, True)

    effect(_hiders, invisibility, 10000, 0)

    give(_hiders, wind_charge, 4)
    give(_hiders, ender_pearl)

    # Title
    times(all, 5, 80, 10)
    title(_seekers, f"#red#You are a seeker!")
    subtitle(_seekers, f"#gray#Kill all hiders! Bow shoots explosive arrows.")
    title(_hiders, f"#aqua#You are a hider!")
    subtitle(_hiders, f"#gray#Don't get killed for {timer}s!")

    wait('30s', freezehiders)

def start(self):
    print("Finding a spot...")
    tag(self, 'abc')
    run('worldborder set 1000000')
    
    gamemode(all, adventure)

    resetattribute(self, movement_speed)
    resetattribute(self, jump_strength)

    cleareffect(all)

    run('clear @a')

    effect(all, resistance, 1, 4, True)
    
    # Random area
    tparound(self, 3000)
 
    wait('1s', runstart)

def runstart():
    execute('as @a[tag=abc] at @s', start2)
    removetag(all, 'abc')

def ondeath():
    tag(self, 'died')

def onrespawn():
    gamemode(self, spectator)

def sec():
    wait('1s', sec)

    if gamestart == 1:
        timer -= 1

        # display
        actionbar(all, f"#yellow#Time remaining: #aqua#{timer: var}s")

        if timer <= 0:
            gamestart = 0
            title(all, f"#green,b#Hiders Win!!")
            subtitle(all, "")
            effect(all, glowing)
        else:
            tempp = 0
            execute('at @a[team=player, tag=!died]', add('tempp', 1))

            if tempp == 0:
                gamestart = 0
                subtitle(all, "")
                title(all, f"#green,b#Seekers Win!!")

    effect(_seekers, resistance, 2, 4, True)

def onfuncs():
    # Function automatically is as @a
    
    if "entity @s[team=player]" and gamestart == 1:
        run('scoreboard players enable @s colour')
        self.colour += 0
        if self.colour == 0:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =0] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=0] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =0] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =0] 1')
        elif self.colour == 1:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =16711680] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=16711680] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =16711680] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =16711680] 1')
        elif self.colour == 2:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =16744448] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=16744448] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =16744448] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =16744448] 1')
        elif self.colour == 3:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =16776960] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=16776960] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =16776960] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =16776960] 1')
        elif self.colour == 4:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =24832] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=24832] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =24832] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =24832] 1')
        elif self.colour == 5:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =65280] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=65280] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =65280] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =65280] 1')
        elif self.colour == 6:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =65535] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=65535] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =65535] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =65535] 1')
        elif self.colour == 7:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =255] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=255] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =255] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =255] 1')
        elif self.colour == 8:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =16711935] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=16711935] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =16711935] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =16711935] 1')
        elif self.colour == 9:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =8388863] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=8388863] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =8388863] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =8388863] 1')
        elif self.colour == 10:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =16777215] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=16777215] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =16777215] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =16777215] 1')
        elif self.colour == 11:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =6044928] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=6044928] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =6044928] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =6044928] 1')
        elif self.colour == 12:
            run('item replace entity @s armor.head with leather_helmet[dyed_color    =4210752] 1')
            run('item replace entity @s armor.chest with leather_chestplate[dyed_color=4210752] 1')
            run('item replace entity @s armor.legs with leather_leggings[dyed_color  =4210752] 1')
            run('item replace entity @s armor.feet with leather_boots[dyed_color     =4210752] 1')
        else:
            run('item replace entity @s armor.head with leather_helmet 1')
            run('item replace entity @s armor.chest with leather_chestplate 1')
            run('item replace entity @s armor.legs with leather_leggings 1')
            run('item replace entity @s armor.feet with leather_boots 1')
