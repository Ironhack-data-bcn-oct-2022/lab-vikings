from random import choice
from vikingsClasses import Soldier, War, Viking, Saxon
saxon = Saxon(60,25)
def vikingGenerator():
    odin = Viking("Odin", 0, 20000000)
    erik = Viking("Erik", 25, 55)
    harald = Viking("Harald", 300, 150)
    viking = choice([odin,erik,harald])
    return viking
def armyGenerator(num=1):
    randomWar=War()
    for i in range(0,num):
        randomWar.addSaxon(saxon)
        randomWar.addViking(vikingGenerator())
    while randomWar.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        randomWar.vikingAttack()
        if randomWar.showStatus() != "Vikings and Saxons are still in the thick of battle.":
            break
        randomWar.saxonAttack()
        if randomWar.showStatus() != "Vikings and Saxons are still in the thick of battle.":
            break
        randomWar.saxonAttack()
    print(randomWar.showStatus())
#num_sold=input("How many soldiers do you want to have each army?")
#while num_sold.isdigit()==False:
#    num_sold=input("Please input a positive integer number")
#armyGenerator(int(num_sold))
armyGenerator(4)