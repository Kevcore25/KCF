from KCFSyntax import *

level: int

"""
Lose a permanent heart when dead.
At 0 Hearts, you will get BANNED!

There are 2 ways of regaining hearts:
1. Spend 30 XP. 
2. Buy with KCash (10,000 KCash)
3. Craft a heart.
"""

# We can use the built-in PyMCF features
def load():
    trigger('regain')
    var('lvl', 'level')
    var('kcash', 'totalKillCount')
    level = 1

    min() # Run the minutely function

def triggers__regain():
    """Buy 1 heart for 30 XP"""
    if self.heartsLost > 2:
        self.getlvl = 30 + self.regainamt
        # Check for XP
        if self.lvl >= self.regainamt:
            def removexp(getlvl):
                run(f'xp add @s -{getlvl} levels')
            removexp(self.getlvl)
            removeHeartLost()
            tellraw(self, f'#green#Bought 1 maximum hearts for {self.getlvl} Experience Levels!')
            self.regainamt += 5
        else:
            tellraw(self, f'#red#You need {self.getlvl} Experience Levels to buy a heart back!')
    else:
        tellraw(self, f'#red#You already reached the maximum hearts!\nYou can only buy up to 8 maximum hearts with XP.\nCraft the Heart Increaser item to increase it up to 12 maximum hearts!')

def ondeath():
    # Increment hearts lost by 1
    addHeartLost()

    # Update HP attribute
    updateHP()    
    
    # Tell player
    self.heartsLeft = 10 - self.heartsLost
    tellraw(self, f'#red#You lost a heart from dying! You now have {self.heartsLeft} hearts.')

def updateHP():
    """Updates the HP attribute of the player based on heartsLost"""

    # Create macro for Atrribute
    def updatehpmacro(hp: int):
        run(f'attribute @s minecraft:max_health base set {hp}')

    # Calculate formula. Formula is 20 - 2heartsLost
    self.hp = 20 - self.heartsLost * 2

    # Update
    updatehpmacro(self.hp)

def removeHeartLost():
    """Removes 1 Heart Lost"""
    if not self.heartsLost <= -2:
        self.heartsLost -= 1

    updateHP()

def addHeartLost():
    """Adds 1 Heart Lost"""
    self.heartsLost += 1
    if self.heartsLost >= 10:
        self.heartsLost = 7
        run('execute at @s run ban @p You ran out of hearts!')

    updateHP()

def gainheart():
    if self.heartsLost > -2:
        removeHeartLost()
        tellraw(self, f'#green#Gained 1 maximum heart!')
        run('clear @s minecraft:heart_of_the_sea[minecraft:item_name="Heart Increaser"] 1')
    else:
        tellraw(self, f'#red#You already reached the maximum hearts!')
    run('advancement revoke @s only gr12smp:rightclick')

def gainheart10():
    if self.heartsLost > 0:
        removeHeartLost()
        tellraw(self, f'#green#Gained 1 maximum heart!')
    else:
        tellraw(self, f'#red#You already reached the maximum hearts!\nCraft the Heart Increaser item to increase it up to 12!')

def onnewjoin():
    # Give recipe on first join
    run('recipe give @s gr12smp:heart')

def onfuncs():
    # Replace totems in INV with gapples.
    # Hoppers may immediately grab the totem sometimes so this patches it
    if entity('@s[nbt={Inventory:[{id:"minecraft:totem_of_undying"}]}]'):
        tellraw(self, f'#red#Totems are banned! It will be exchanged for 1 Golden Apple')
        give(self, golden_apple)
        run('clear @s totem_of_undying 1')

def min():
    schedule('60s', min)
    all.kcash += 10

def tick():
    # Replace totems with gapple on item spawn
    def gapplereplace():
        tag(self, 'done')

        if entity('@s[nbt={Item: {id: "minecraft:totem_of_undying"}}]'):
            run('data modify entity @s Item set value {id: "minecraft:golden_apple", count: 1}')

    execute('as @e[type=item, tag=!done]', gapplereplace)

"""
# recipe gr12smp:heart
{
  "type": "minecraft:crafting_shaped",
  "pattern": [
    " # ",
    "#X#",
    " # "
  ],
  "key": {
    "X": [
      "minecraft:wither_skeleton_skull",
      "minecraft:heavy_core",
      "minecraft:elytra",
      "minecraft:piglin_head"
    ],
    "#": [
      "minecraft:netherite_ingot"
    ]
  },
  "result": {
    "id": "minecraft:heart_of_the_sea",
    "components": {
      "minecraft:food": {
        "nutrition": 0,
        "saturation": 0,
        "can_always_eat": true
      },
      "minecraft:consumable": {
        "consume_seconds": 1000000,
        "animation": "bow",
        "has_consume_particles": false
      },
      "minecraft:item_name": "Heart Increaser",
      "minecraft:lore": [
        {
          "text": "Increases maximum hearts by 1, up to 12.",
          "color": "gray",
          "italic": false
        }
      ],
      "minecraft:enchantment_glint_override": true
    },
    "count": 1
  },
  "show_notification": true
}

# advancement gr12smp:rightclick
{
  "criteria": {
    "requirement": {
      "trigger": "minecraft:using_item",
      "conditions": {
        "item": {
          "components": {
            "minecraft:consumable": {
                "consume_seconds": 1000000,
                "animation": "bow",
                "has_consume_particles": false
            }
          }
        }
      }
    }
  },
  "rewards": {
    "function": "kcf:gainheart"
  }
}

"""


"""
Level System!
For now, level is disabled.

For Pillagers, Skeletons, Strays/Bogged, Witches, and Breezes (projectile/non-physical attacking mobs):
    Each level increases maximum HP by 20%, movement speed by 10%, and also adds 1 armor point

For everything else (including creepers):
    Each level increases maximum HP by 10%, and also adds 1 armor point
"""

# def onnewentity():
#     """Not a built-in function"""

#     self.level = level

#     def nonatkmod():


#     # Currently, OR is broken...
#     if entity('@s[type = pilllager]'):

#     elif entity('@s[type=skeleton]')