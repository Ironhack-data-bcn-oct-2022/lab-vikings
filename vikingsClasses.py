
import sre_compile
from this import d


class Soldier():
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health=self.health -damage
class Viking(Soldier):
    def __init__(self, name,health, strength):
        super().__init__(health, strength)
        self.name=name
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return  f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
            return "Odin Owns You All!"

class Saxon(Soldier):
    def __init__(self,health, strength):
        super().__init__(health, strength)
    def receiveDamage(self,damage):
        self.health=self.health-damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"           
        else:
            return "A Saxon has died in combat"

import random
class War():

    def __init__(self):
            self.vikingArmy = []
            self.saxonArmy = []
        
    def addViking(self, Viking):
    
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
       self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
            
        received_damage = random_saxon.receiveDamage(random_viking.attack())
                
        for Saxon in self.saxonArmy:
            if Saxon.health <= 0:
                self.saxonArmy.remove(Saxon)
            
            return received_damage
    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
            
        received_damage = random_viking.receiveDamage(random_saxon.attack())
            
        for Viking in self.vikingArmy:
            if Viking.health <= 0:
                self.vikingArmy.remove(Viking)
            
        return received_damage
    def showStatus(self):
            
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
            
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
                return "Vikings and Saxons are still in the thick of battle."
