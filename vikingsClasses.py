
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, demage):
        self.health=self.health-demage




# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        #**if the `Viking` is still alive**, 
        #it should return **"NAME has received DAMAGE
        #points of damage"**
        #**if the `Viking` dies**, it should return 
        #**"NAME has died in act of combat"**

        self.health=self.health-damage

        if self.health>0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")


    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        #**if the `Viking` is still alive**, 
        #it should return **"NAME has received DAMAGE
        #points of damage"**
        #**if the `Viking` dies**, it should return 
        #**"NAME has died in act of combat"**

        self.health-=damage

        if self.health>0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return "A Saxon has died in combat"

# War


class War:

    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []

    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)



    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        s = Saxon.receiveDamage(Viking.strength)

        if Saxon.health<=0:
            self.saxonArmy.remove(Saxon)
        
        return s


    def saxonAttack(self):
        Saxon = random.choice(self.saxonArmy)
        Viking = random.choice(self.vikingArmy)
        v = Viking.receiveDamage(Saxon.strength)

        if Viking.health<=0:
            self.vikingArmy.remove(Viking)
        
        return v

    def showStatus(self):

        if len(self.vikingArmy)==0:
            return 'Saxons have fought for their lives and survive another day...'

        elif len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'

        else:
            return 'Vikings and Saxons are still in the thick of battle.'

        




