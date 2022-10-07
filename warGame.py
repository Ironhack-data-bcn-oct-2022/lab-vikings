import vikingsClasses as VK
import os
import time

def printMainMenu():
    print("----------------------- WARGAME MAIN MENU -----------------------")
    print("1. Raise Viking raiding army")
    print("2. Raise Saxon defending army")
    print("3. Raise Random Armies")
    print("4. Start the War")
    print("5. Quit WarGame")
    option = int(input("What will you do next? "))
    return option

def printWarMenu():
    print("----------------------- WARGAME WAR MENU -----------------------")
    print("1. Vikings attack!")
    print("2. Saxons attack!")
    print("3. Show war status")
    print("4. Go to main menu")


def createTeamVikings(warGame):
    print("Viking Raiding season is coming! Get ready to pillage the Saxon lands.")

    x = input("Add a new Viking to the Raid? [Y/N]")
    while x == 'Y' or x == 'y':
        name = input("How is this Viking called? ")
        health = int(input(f"How much health does {name} have? "))
        strength = int(input(f"How much strength does {name} have? "))
        warGame.addViking(VK.Viking(name, health, strength))

        x = input("Add a new Viking to the Raid? [Y/N]")
    print("The Viking Raiders are ready!")
    time.sleep(1)
    os.system("clear")
    return warGame
    

def createTeamSaxons(warGame):
    print("Saxons! The Vikings are aproaching, will you try and defend you homeland?")

    x = input("Add a new Saxon to the Defending Army? [Y/N]")
    while x == 'Y' or x == 'y':
        health = int(input(f"How much health does this Saxon have? "))
        strength = int(input(f"How much strength does this Saxon have? "))
        warGame.addSaxon(VK.Saxon(health, strength))

        x = input("Add a new Saxon to the Defending Army? [Y/N]")
    print("The Saxon Defenders are ready!")
    time.sleep(1)
    os.system("clear")
    return warGame


def raiseStandardArmies(warGame):
    for n in range(10):
        warGame.addSaxon(VK.Saxon(50,10))
        warGame.addViking(VK.Viking("Ragnar",50,20))
    print("The Standard Armies have been raised!")
    time.sleep(1)
    os.system("clear")
    return warGame
    

if __name__=='__main__':
    flagEnd = True
    warGame = VK.War()
    warGame.showStatus()
    
    while(flagEnd == True):
        option = printMainMenu()
        if (option == 1):                   # VikingArmy
            os.system("clear")
            warGame = createTeamVikings(warGame)

        elif (option == 2):                 # SaxonArmy
            os.system("clear")
            warGame = createTeamSaxons(warGame)

        elif (option == 3):                 # Raise standard armies
            os.system("clear")
            warGame = raiseStandardArmies(warGame)

        elif (option == 4):                 # Start War
            os.system("clear")
            warFlag = True
            printWarMenu()
            while (warFlag == True):
                warOption = int(input("What will happen next? "))
                if (warOption == 1):           # Vikings attack
                    warGame.vikingAttack()
                
                elif (warOption == 2):         # Saxons attack
                    warGame.saxonAttack()
                
                elif (warOption == 3):         # Show status
                    m = warGame.showStatus()
                    print(m)
                    time.sleep(1)
                
                elif (warOption == 4):         # Go to main menu
                    warFlag = False
                    os.system("clear")
                

        elif (option == 5):                 # Quit Game
            flagEnd = False

