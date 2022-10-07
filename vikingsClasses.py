
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

        #methods

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
        return f"Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"



# War

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
        a_saxon = random.choice(self.saxonArmy)
        a_viking = random.choice(self.vikingArmy)
        
        dmg_received_saxon = a_saxon.receiveDamage(a_viking.attack())
       
        if a_saxon.health <= 0:
            self.saxonArmy.remove(a_saxon)

        return dmg_received_saxon

    def saxonAttack(self):
        a_saxon = random.choice(self.saxonArmy)
        a_viking = random.choice(self.vikingArmy)

        dmg_received_viking = a_viking.receiveDamage(a_saxon.attack())
        
        if a_viking.health <= 0:
            self.vikingArmy.remove(a_viking)
        
        return dmg_received_viking

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if ( len(self.vikingArmy) >= 1 ) and ( len(self.saxonArmy) >= 1 ):
            return "Vikings and Saxons are still in the thick of battle."


    
