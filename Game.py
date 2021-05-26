from pathlib import Path
from enum import Enum
from pprint import pprint
import random
import time
import os

ROWS, COLUMNS = os.popen('stty size', 'r').read().split()

class UiMaker:
    textMenus = Path("./TextMenus/")

    @classmethod
    def printFile(self, filename):
        textFile = open(self.textMenus / str(filename) ,'r')
        for line in textFile:
            print(line, end='')

    @classmethod
    def getFileContent(self, filename):
        with open(self.textMenus / str(filename), 'r') as textfile:
            return textfile.read()

    @classmethod
    def printMenuChoose(self):
        self.printFile("MainMenu.txt")
        option = input()
        os.system('clear')
        self.menuChoose(int(option))

    @classmethod
    def menuChoose(self, option):
        # start game
        if option == 1:
            BattleGame.startGame()
        # instructions
        elif option == 2:
            self.printFile("Instructions.txt")
        # credits
        elif option == 3:
            self.printFile("Credits.txt")
        # class stats
        elif option == 4:
            self.printFile("ClassStats.txt")
        input()
        os.system('clear')
        self.printMenuChoose()

    @classmethod
    def classChooser(self):
        self.printFile("ClassChooser.txt")

class Warrior:
    def __init__(self, name, health=1, attkMax=1, blckMax=1, mana=1, className=1):
        self.Name = name
        self.Health = health
        self.AttkMax = attkMax
        self.BlckMax = blckMax
        self.Mana = mana
        self.ClassName = className

    def chooseClass(self, className):
        if className == 1:
            self.Health = 1000
            self.AttkMax = 140
            self.BlckMax = 30
            self.Mana = 30
            self.ClassName = WarriorClasses(1).name
        elif className == 2:
            self.Health = 1200
            self.AttkMax = 100
            self.BlckMax = 60
            self.Mana = 20
            self.ClassName = WarriorClasses(2).name
        elif className == 3:
            self.Health = 700
            self.AttkMax = 200
            self.BlckMax = 20
            self.Mana = 50
            self.ClassName = WarriorClasses(3).name

class WarriorClasses(Enum):
    BERSERKER = 1
    TANK = 2
    WIZARD = 3

class BattleGame:

    @staticmethod
    def printHomeScreen():
        os.system('clear')
        if int(COLUMNS) < 80:
            UiMaker.printFile("HomeScreenSmall.txt")
        else:
            UiMaker.printFile("HomeScreen.txt")
        input()
        os.system('clear')
        UiMaker.printMenuChoose()
        
    @classmethod
    def startGame(self):
        print("Name the first warrior:")
        warrior1 = Warrior(input())
        UiMaker.classChooser()
        warrior1.chooseClass(int(input()))
        print("Name the second warrior:")
        warrior2 = Warrior(input())
        UiMaker.classChooser()
        warrior2.chooseClass(int(input()))

        self.checkWarriorName(warrior1, warrior2)
        self.startFight(warrior1, warrior2)

    @classmethod
    def checkWarriorName(self, warrior1, warrior2):
        if warrior1.Name == warrior2.Name:
            # add numbers to differentiate the warriors if their names are the same
            warrior1.Name += "1"
            warrior2.Name += "2"
            print("Unfortunately warriors names are the same so we changed it to " + warrior1.Name + " and " + warrior2.Name)

    @classmethod
    def startFight(self, warrior1 : Warrior, warrior2 : Warrior):
        while warrior1.Health > 0 and warrior2.Health > 0 :
            if self.checkForWinner(warrior1, warrior2):
                break
            if self.checkForWinner(warrior2, warrior1):
                break
        input()
        self.printHomeScreen()

    @classmethod
    def checkForWinner(self, warrior1, warrior2):
        self.getActionResult(warrior1, warrior2)
        if warrior1.Health < 0:
            self.printWinner(warrior2)
            return True
        elif warrior2.Health < 0:
            self.printWinner(warrior1)
            return True

    @classmethod
    def printWinner(self, winner):
        print(winner.Name + " won with " + str(winner.Health) + " health left")

    @classmethod
    def getActionResult(self, warrior1, warrior2):
        print(UiMaker.getFileContent("BattleActionMenu.txt").replace("warriorName", warrior1.Name))
        action = int(input())
        buffBonus = 20
        # action 1 is attack which increases the final damage by 'buffBonus'
        if action == 1:
            attack = random.randrange(0,warrior1.AttkMax) + buffBonus
            defense = random.randrange(0, warrior1.BlckMax)
        # action 2 is attack which increases the final defense by 'buffBonus'
        elif action == 2:
            attack = random.randrange(0,warrior1.AttkMax) 
            defense = random.randrange(0, warrior1.BlckMax) + buffBonus

        attackDamage = attack - random.randrange(warrior2.BlckMax)
        self.calculateDamage(warrior1, warrior2, attackDamage)

        counterDamage = random.randrange(0,warrior2.AttkMax) - defense
        self.calculateDamage(warrior2, warrior1, counterDamage)

        print(warrior2.Name + " has " + str(warrior2.Health) + " health left")
        print(warrior1.Name + " has " + str(warrior1.Health) + " health left")
        time.sleep(1)

    @classmethod
    def calculateDamage(self, warrior1, warrior2, damage):
        # warriors block the attack if the final damage is lower than 0
        # final damage is damage of warrior1 subtracted by defense of warrior2
        if damage <= 0:
            print("Warrior "+warrior2.Name+" blocked the attack!")
            time.sleep(1)
        else:
            print("Warrior " + warrior1.Name + " did " + str(damage) + " damage to " + warrior2.Name)
            warrior2.Health -= damage
            time.sleep(1)
def main():
    btgm = BattleGame()
    btgm.printHomeScreen()

if __name__ == "__main__":
    main()