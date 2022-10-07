from random import randint
# Soldier


class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health-=damage

# Viking


class Viking (Soldier):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon (Soldier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def receiveDamage(self, damage):
        self.health-=damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else: 
            return f"A Saxon has died in combat"
# War



class War ():
    vikingArmy=[]
    saxonArmy=[]
    def random_index(self, army):
        if army == "viking":
            return randint(0,(len(self.vikingArmy)-1))
        if army == "saxon":
            return randint(0,(len(self.saxonArmy)-1))
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        viking_num = self.random_index("viking")
        saxon_num = self.random_index("saxon")
        self.saxonArmy[saxon_num].receiveDamage(self.vikingArmy[viking_num].strength)
        if self.saxonArmy[saxon_num].health <= 0:
            self.saxonArmy.pop(saxon_num)
    def saxonAttack(self):
        viking_num = self.random_index("viking")
        saxon_num = self.random_index("saxon")
        self.vikingArmy[viking_num].receiveDamage(self.saxonArmy[saxon_num].strength)
        if self.vikingArmy[viking_num].health <= 0:
            self.vikingArmy.pop(viking_num)
    def showStatus(self):
        if bool(self.saxonArmy)==False:
            return "Vikings have won the war of the century!"
        elif bool(self.vikingArmy)==False:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
