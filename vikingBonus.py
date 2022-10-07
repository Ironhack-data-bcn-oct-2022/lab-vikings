
# Soldier

import random
from vikingsClasses import Soldier, Viking, Saxon, War
battle = War()

list_vikings=[]
for name in range(1,50):
    list_vikings.append("a"*name)



batalla_v=[]
def agrega_vikingo(number):

    for vik in range(number):
        vikingo = Viking(random.choice(list_vikings), random.randint(1,20),random.randint(1,20))
        battle.addViking(vikingo)


batalla_s=[]
def agrega_britanico(numbersax):
    
    for sax in range(numbersax):
        saxon1 = Saxon(random.randint(1,15),random.randint(1,15))
        battle.addSaxon(saxon1)

agrega_vikingo(10)
agrega_britanico(10)
not_finished =  "Vikings and Saxons are still in the thick of battle."

random_attack = [battle.vikingAttack, battle.saxonAttack]

while battle.showStatus() == not_finished:
    random.choice(random_attack)()

print(battle.showStatus())











#ef viking_creator(number):


    
