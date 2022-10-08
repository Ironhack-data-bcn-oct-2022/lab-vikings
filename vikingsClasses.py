
# Soldier

from ctypes import resize
from os import remove
from re import sub
import random


class Soldier():
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength 

    def attack (self):
        return self.strength
    def receiveDamage (self,damage):
        self.health -= self.damage 
       

# Viking

class Viking(Soldier):

    def __init__(self, name, health, strength):
        self.name = name 
        super().__init__(health, strength)

    def receiveDamage(self,damage):
        self.health -= damage 
        if self.health > 0: 
            return f"{self.name} has received {damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat"

    def battleCry (self):
        return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength): 
        super().__init__(health, strength)

    def receiveDamage(self,damage):
        self.health -= damage 
        if self.health > 0: 
            return f"A Saxon has received {damage} points of damage"
        else: 
            return "A Saxon has died in combat"

# War


class War():
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        
        #result = 'Not enough parties for the war'
        #if( len(self.saxonArmy)*len(self.vikingArmy) >0):

            TheSaxon = random.choice(self.saxonArmy)
            TheViking = random.choice(self.vikingArmy)
          
            damagevalue = TheViking.strength 
            result = TheSaxon.receiveDamage(damagevalue)

            if(result == "A Saxon has died in combat"):
                self.saxonArmy.remove(TheSaxon)
            

            return result 
    
    def saxonAttack(self):
        
        #result = 'Not enough parties for the war'
        #if(len(self.vikingArmy)*len(self.saxonArmy) >0):

            TheSaxon = random.choice(self.saxonArmy)
            TheViking = random.choice(self.vikingArmy)
           
            damagevalue = TheSaxon.strength 
            result = TheViking.receiveDamage(damagevalue)

            if result == f"{TheViking.name} has died in act of combat":
                self.vikingArmy.remove(TheViking)
        
            return result 

    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
             return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0:
                return "Saxons have fought for their lives and survive another day..."

        else: 
            return"Vikings and Saxons are still in the thick of battle."

        
        



        

        
    
