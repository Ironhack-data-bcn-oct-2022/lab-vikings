import random

# Soldier
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
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"

    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strenght):
        super().__init__(health, strenght)
        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"
        

# War
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if self.saxonArmy:
            saxon = random.choice(self.saxonArmy)
            if self.vikingArmy:
                viking = random.choice(self.vikingArmy)

                m = saxon.receiveDamage(viking.attack())
                print(m)
                if (saxon.health <= 0):
                    self.saxonArmy.remove(saxon)
                return m
            else:
                print("There are no more Vikings left!")
        else:
            print("There are no more Saxons left!")
        return None

    def saxonAttack(self):
        if self.saxonArmy:
            saxon = random.choice(self.saxonArmy)
            if self.vikingArmy:
                viking = random.choice(self.vikingArmy)

                m = viking.receiveDamage(saxon.attack())
                print(m)
                if (viking.health <= 0):
                    self.vikingArmy.remove(viking)
                return m
            else:
                print("There are no more Vikings left!")
        else:
            print("There are no more Saxons left!")
        return None

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."