
# Soldier


from email.base64mime import header_length
import random

class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage  
        self.health = self.health - damage
        pass



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

        
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War(Viking, Saxon):
    def __init__(self):
        self.vikingArmy = [] 
        self.saxonArmy = []
        


    def addViking(self, Viking):
        self.Viking = Viking
        self.vikingArmy.append(self.Viking)
        pass


    def addSaxon(self, Saxon):
        self.Saxon = Saxon
        self.saxonArmy.append(self.Saxon)
        pass

    def vikingAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        vik_attack = sax.receiveDamage(vik.attack())
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        
        return vik_attack        
        
       

    def saxonAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        sax_attack = vik.receiveDamage(sax.attack())
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        
        return sax_attack       


    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."

        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."


        

    