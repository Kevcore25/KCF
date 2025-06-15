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
    StaminaRegenCD = 25

def displaystamina():
    # Stamina is scaled by 100x, so it must be divided first
    self.temp = self.stamina / 100
    
    # Display
    run('title @s title ""')    
    run('title @s times 0 5 5')
    if self.stamina < 1000:
        run('title @s subtitle ["       ", {score: {objective: "temp", name: "@s"}, color: "red"}]')
    elif self.stamina < 2500:
        run('title @s subtitle ["       ", {score: {objective: "temp", name: "@s"}, color: "gold"}]')
    else:
        run('title @s subtitle ["       ", {score: {objective: "temp", name: "@s"}, color: "yellow"}]')

def regenstamina():    
    self.stamina += 25
    self.stamina *= 102
    self.stamina /= 100
    if self.stamina > self.currentMax:
        self.stamina = self.currentMax

def onrespawn():
    self.stamina = 10000
    self.currentMax = 10000

def onnewjoin():
    self.stamina = 10000

def nostamina():
    effect(self, slowness, 1, 3)
    effect(self, weakness, 1, 2)
    effect(self, mining_fatigue, 1, 2)
    run("attribute @s jump_strength base set 0")
    run("attribute @s attack_damage base set -1000")
    run("attribute @s block_interaction_range base set 0")

    if self.increased == 0:
        self.increased = 1

        self.currentMax += 500

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
            self.stamina -= 150
            self.staminaCD = StaminaRegenCD
            self.attacking = 0

        if self.stamina < 0:
            self.stamina = 0

        if self.stamina < 500:
            nostamina()
        else:
            hasstamina()

    execute("as @a", executeall)

def createmobs():
    for i in range(1000):
        summon(warden)