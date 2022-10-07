
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
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
            return f'{self.name} has received {self.damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battleCry(self): 
        return 'Odin Owns You All!'

# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health = self.health - damage 
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'



# War


class War:
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
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        vik_attack = s.receiveDamage(v.attack())
        if s.health <= 0:
            self.saxonArmy.remove(s)
        return vik_attack

    def saxonAttack(self):
        s = random.choice(self.saxonArmy)
        v = random.choice(self.vikingArmy)
        sax_attack = v.receiveDamage(s.attack())
        if v.health <= 0:
            self.vikingArmy.remove(v)
        return sax_attack
    
    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) <= 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return 'Vikings and Saxons are still in the thick of battle.'    






