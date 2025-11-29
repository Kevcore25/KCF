from KCFSyntax import *


def loop_sec():
    """
    Function that runs every second
    """

    # Schedule to run after a second
    schedule('10t', loop_sec)

    def rain():
        # Introduced in V.6, this new feature allows us to run Python script
        """@run

        l = []
        width = 10
        length = 10
        for x in range(width + 1):
            for z in range(length + 1):
                l.append((x - width // 2, z - length // 2))

        width = 25
        length = 25
        for x in range(width + 1):
            for z in range(length + 1):
                c = ((x - width // 2) * 10, (z - length // 2) * 10)
                if c not in l:
                    l.append(c)
                    
        for i in l:        
            x = i[0]
            z = i[1]
            run(f"summon small_fireball ~{x} 300 ~{z} {{acceleration_power:5d,Motion:[0.0,-10.0,0.0]}}")
        """

        cleareffect(self, fire_resistance)
        run('xp set @s 0 levels')
        run('xp set @s 0')


    def rain2():
        # Introduced in V.6, this new feature allows us to run Python script
        """@run

        l = []
        width = 10
        length = 10
        for x in range(width + 1):
            for z in range(length + 1):
                l.append((x - width // 2, z - length // 2))

        for i in l:        
            x = i[0]
            z = i[1]
            run(f"summon small_fireball ~{x} ~5 ~{z} {{acceleration_power:1d,Motion:[0.0,-5.0,0.0]}}")
        """

        cleareffect(self, fire_resistance)
        run('xp set @s 0 levels')
        run('xp set @s 0')

    execute('as @a at @s unless data entity @s {Dimension:"minecraft:the_nether"}', rain)
    execute('as @a at @s if data entity @s {Dimension:"minecraft:the_nether"}', rain2)

def loop_sec2():
    kill("@e[type=small_fireball]")
    schedule('100t', loop_sec2)


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
    execute('as @e[tag=!done,type=!player,type=!item,type=!small_fireball]', onnewentity)

def onnewjoin():
    # MODIFIER: No armor
    run('attribute @s minecraft:armor modifier add modifier -1 add_multiplied_total')

def load():
    "Code that runs every reload"
    var('kcash')
    loop_sec()
    loop_sec2()

# Translate file into MCF files
import Build
