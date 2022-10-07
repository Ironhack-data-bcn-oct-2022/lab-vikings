import vikingsClasses
import random

battle = vikingsClasses.War()

viking_names = []
vikings_file = open(r'C:\Users\Marc\Desktop\Universidad\IronHack\Week1\viking_names.txt', 'r')
lines = vikings_file.readlines()
for line in lines:
    viking_names.append(line.split(":")[0])

def create_vikings(viking_num):
    for num in range(0,viking_num):
        vikingo = vikingsClasses.Viking(random.choice(viking_names), random.randint(1,20), random.randint(5,10))

        battle.addViking(vikingo)

def create_saxons(saxon_num):
    for num in range(0,saxon_num):
        saxon = vikingsClasses.Saxon(random.randint(1,20), random.randint(5,10))

        battle.addSaxon(saxon)

create_vikings(2)
create_saxons(2)

not_finished =  "Vikings and Saxons are still in the thick of battle."

random_attack = [battle.vikingAttack, battle.saxonAttack]

while battle.showStatus() == not_finished:
    random.choice(random_attack)()

print(battle.showStatus())