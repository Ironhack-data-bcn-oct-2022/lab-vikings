
# Soldier
from random import random


class Soldier:
    def __init__(self, health, strength): 
        self.health = health
        self.strength = strength
    def attack(self): 
        return self.strength
    def receiveDamage(self, damage): 
        self.health -= damage

# Viking


class Viking(Soldier): 
    def __init__(self, name, strenght, health): 
        Soldier.__init__(self, health, strenght)
        self.name = name

    def battleCry(self): 
        return "Odin Owns You All!"

    def receiveDamage(self, damage): 
        super().receiveDamage(damage)
        if self.health > 0: 
            return "{} has received {} points of damage".format(self.name, damage)
        else: 
            return "{} has died in act of combat".format(self.name)

# Saxon
class Saxon(Soldier): 
    def __init__(self, health, strenght): 
        Soldier.__init__(self, health, strenght)

    def receiveDamage(self, damage): 
        super().receiveDamage(damage)
        if self.health > 0: 
            return "A Saxon has received {} points of damage".format(damage)
        else: 
            return "A Saxon has died in combat"

# War
class War: 
    def __init__(self): 
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking): 
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon): 
        self.saxonArmy.append(saxon)

    def vikingAttack(self): 
        viking = self.vikingArmy[0]
        saxon = self.saxonArmy[0]
        random = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0: 
            self.saxonArmy.pop(0)
        return random

    def saxonAttack(self): 
        viking = self.vikingArmy[0]
        saxon = self.saxonArmy[0]
        random= viking.receiveDamage(saxon.strength)
        if viking.health <= 0: 
            self.vikingArmy.pop(0)
        return random

    def showStatus(self): 
        if len(self.saxonArmy) <= 0: 
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0: 
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0: 
            return "Vikings and Saxons are still in the thick of battle."
TA!!!!!!!!!!!