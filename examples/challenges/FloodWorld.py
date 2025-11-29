from KCFSyntax import *

"""
This world requires a fabric mod.
This datapack serves as additional modifiers.
"""

def loop_sec():
    """
    Function that runs every second
    """

    # Schedule to run after a second
    schedule('10t', loop_sec)

    # MODIFIER: No XP
    run('xp set @a 0 levels')
    run('xp set @a 0')

    execute('as @e[type=item] at @s unless entity @a[distance=..50]', kill(self))
    execute('at @a', fill('~5 ~5 ~5', '~-5 ~-5 ~-5', water, keep))

def onnewjoin():
    # MODIFIER: No armor AND 50% less health
    run('attribute @s minecraft:armor modifier add modifier -1 add_multiplied_total')
    run('attribute @s minecraft:max_health modifier add modifier -0.5 add_multiplied_total')
    tp(self, '0 100 0')
def playertick():
    fill('~5 319 ~5', '~-5 319 ~-5', barrier)

def onrespawn():
    # Respawn somewhere at spawn
    onnewjoin()

def onnewentity():
    # MODIFIER: Give 2x more health and more armor
    run('attribute @s minecraft:max_health modifier add modifier 1 add_multiplied_total')
    run('attribute @s minecraft:armor modifier add modifier 8 add_value')
    run('data modify entity @s Health set value 1000')
    tag(self, 'done')
    

    def gigantic():
        run('attribute @s minecraft:max_health modifier add giant 2 add_multiplied_total')
        run('attribute @s minecraft:armor modifier add giant 16 add_value')
        run('attribute @s minecraft:armor_toughness modifier add giant 12 add_value')
        run('attribute @s minecraft:scale modifier add giant 1 add_multiplied_total')
        run('attribute @s minecraft:attack_damage modifier add giant 1 add_multiplied_total')
        run('attribute @s minecraft:attack_knockback modifier add giant 4 add_value')
        run('attribute @s minecraft:step_height modifier add giant 1 add_value')
        run('attribute @s minecraft:jump_strength modifier add giant 3 add_multiplied_total')
        run('attribute @s minecraft:movement_speed modifier add giant 1 add_multiplied_total')
        run('data modify entity @s Health set value 1000')

        if entity('@s[type=creeper]'):
            run('data modify entity @s ExplosionRadius set value 8')

        if not entity('@s[type=skeleton]') and not entity("@s[type=stray]") and not entity("@s[type=bogged]"):
            run('item replace entity @s weapon.mainhand with golden_axe')
        else:
            run('item replace entity @s weapon.mainhand with bow[enchantments={power: 5, punch: 2}]')

    randint(self.temp, 1, 100)
    if self.temp == 1:
        gigantic()

    if entity('@s[tag=gigantic]'):
        gigantic()

def tick():
    execute('as @e[tag=!done,type=!player,type=!item]', onnewentity)
    execute('as @a at @s', playertick)

def load():
    "Code that runs every reload"
    var('kcash', 'totalKillCount')
    loop_sec()

# Translate file into MCF files
import Build
