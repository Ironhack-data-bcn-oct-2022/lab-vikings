
# Soldier

import random

class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
        
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= self.damage
    pass

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage" 
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"       

    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon


class Saxon(Soldier):
    def __init__ (self,health,strength):
        super().__init__(health, strength)
    
    def receiveDamage(self,damage):
        #self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage" 
        elif self.health <= 0:
            return "A Saxon has died in combat" 
    pass

# War


class War():
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []




    def addViking(self, viking):
        self.vikingArmy.append(viking)


    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy) 
        message = random_saxon.receiveDamage(random_viking.strength) 
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return  message

        
    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy) 
        message = random_viking.receiveDamage(random_saxon.strength) 
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return  message
    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."