from KCFSyntax import *

"""
Example: Stamina system
"""

def load():
    # Global is not necessary, it just helps with PyLance
    global StaminaRegenCD

    # Declare custom type vars
    var("jump", "custom:jump")
    var("sprinting", "custom:sprint_one_cm")
    var("attacking", "custom:damage_dealt")

    # Config values
    StaminaRegenCD = 30

def displaystamina():
    # Stamina is scaled by 100x, so it must be divided first
    self.actualstamina = self.stamina / 100
    
    # Display
    run('title @s title ""')    
    run('title @s times 0 5 5')
    # Change colour based on how low stamina is
    if self.stamina < 1000:
        run('title @s subtitle ["       ", {score: {objective: "actualstamina", name: "@s"}, color: "red"}]')
    elif self.stamina < 2500:
        run('title @s subtitle ["       ", {score: {objective: "actualstamina", name: "@s"}, color: "gold"}]')
    else:
        run('title @s subtitle ["       ", {score: {objective: "actualstamina", name: "@s"}, color: "yellow"}]')

def regenstamina():   
    # Regenerates stamina using a quadratic scale 
    self.stamina += 25
    self.stamina *= 1.02 # KCF-Py only accepts up to 3 decimal precisions

    if self.stamina > self.currentMax:
        self.stamina = self.currentMax

def onrespawn():
    # onrespawn() is a built-in function which is ran when respawning

    # Reset values when dead
    self.stamina = 10000
    self.currentMax = 10000

def onnewjoin():
    # onnewjoin() is a built-in function which is ran when a player first joins 
    self.stamina = 10000

def nostamina():
    # Run effect commands
    effect(self, slowness, 1, 3)
    effect(self, weakness, 1, 2)
    effect(self, mining_fatigue, 1, 2)

    # As of previous versions, the attribute function does not exist.
    # This also shows that you can still use MC commands within KCF-Py
    run("attribute @s jump_strength base set 0")
    run("attribute @s attack_damage base set -1000")
    run("attribute @s block_interaction_range base set 0")

    # As of previous versions, bool vars do not exist so a int is used instead
    # This is to ensure that the max stamina increases from "exercising"
    if self.increased == 0 and self.currentMax < 15000:
        self.increased = 1

        self.currentMax += 50

def hasstamina():
    run("attribute @s jump_strength base set 0.42")
    run("attribute @s attack_damage base set 1")
    run("attribute @s block_interaction_range base set 4.5")

    if self.stamina == self.currentMax:
        self.increased = 0


def tick():
    def executeall():
        if self.stamina < self.currentMax:
            if self.staminaCD > 0:
                self.staminaCD -= 1 
            else:
                regenstamina()
            displaystamina()
        
        if self.sprinting > 0:
            self.stamina -= 25
            self.staminaCD = StaminaRegenCD
            self.sprinting = 0
        if self.jump > 0:
            self.stamina -= 500
            self.staminaCD = StaminaRegenCD
            self.jump = 0
        if self.attacking > 0:
            self.stamina -= 250
            self.staminaCD = StaminaRegenCD
            self.attacking = 0

        if self.stamina < 0:
            self.stamina = 0

        if self.stamina < 500:
            nostamina()
        else:
            hasstamina()

    # Run a function as everyone
    # The "execute("as @a", executeall)" is so mandatory for many projects that in the future, a built-in function may exist just for it!
    execute("as @a", executeall)