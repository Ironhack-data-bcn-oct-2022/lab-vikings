import unittest
from vikingsClasses import War, Viking, Saxon

print('hello')

myWar = War()
HugoTheViking = Viking('Hugo',100,500)
PisanoTheViking = Viking('Pisano',100,800)



myWar.addViking(HugoTheViking)
myWar.addViking(PisanoTheViking)


myWar.addSaxon(Saxon(200,30))
myWar.addSaxon(Saxon(200,30))


print(len(myWar.saxonArmy))

result = myWar.vikingAttack()
print(result)

print(len(myWar.saxonArmy))