import random
from vikingsClasses import War
from vikingsClasses import Saxon
from vikingsClasses import Soldier
from vikingsClasses import Viking
list1 =[]
list2 =[]

game_is_on = True

def generateViking():
    name = 'Harald'
    strength = 150
    health = 300
    return Viking(name,health, strength)

def generateSaxon():
    health = 60
    strength = 25
    return Saxon(health, strength)

x = generateSaxon()
y = generateViking()

for i in range(100):
    list1.append(x)
    list2.append(y)


while game_is_on:
    


    print(list1)
    print(list2)
