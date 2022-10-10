
# Soldier


from cmath import rect
from unicodedata import name


class Soldier():
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage



# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
            
    def receiveDamage(self, damage):
        
        self.health -= damage
        
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        
        self.health -= damage
       
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

import random

class War():


    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon (self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        received_damage_by_saxon = random_saxon.receiveDamage(random_viking.attack())

        
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        
        return received_damage_by_saxon

    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        received_damage_by_viking = random_viking.receiveDamage(random_saxon.attack())

        
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)

        return received_damage_by_viking

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"

        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."

        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."


