
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):

        self.health = self.health - damage



# Viking


class Viking(Soldier):
    def __init__(self,name,health, strength):
        super().__init__(health,strength)
        self.name = name

    def receiveDamage(self,damage):
            self.health = self.health - damage
            if self.health > 0:
                return f"{self.name} has received {damage} points of damage"
            if self.health <= 0:
                return f"{self.name} has died in act of combat"

    def battleCry(self):
        return ("Odin Owns You All!")



# Saxon


class Saxon(Soldier):
    def __init__(self,health, strength):
        super().__init__(health,strength)

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        if self.health <= 0:
            return f"A Saxon has died in combat"    

        
    


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)


    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        
        damage_recieved = random_saxon.receiveDamage(random_viking.attack())

        self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health > 0]

        return damage_recieved


    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        
        damage_recieved = random_viking.receiveDamage(random_saxon.attack())

        self.vikingArmy = [viking for viking in self.vikingArmy if viking.health > 0]

        return damage_recieved


    def showStatus(self):

        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy ==[]:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy != [] and self.vikingArmy !=[]: 
            return "Vikings and Saxons are still in the thick of battle."


    
