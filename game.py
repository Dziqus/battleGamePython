from pathlib import Path
from enum import Enum
from pprint import pprint
import os

rows, columns = os.popen('stty size', 'r').read().split()

class UiMaker:

    @classmethod
    def printFile(cls, filename):
        textMenus = Path("./TextMenus/")
        textFile = open(textMenus / str(filename) ,'r')
        for line in textFile:
            print(line, end='')

    @classmethod
    def printMenuChose(cls):
        cls.printFile("MainMenu.txt")
        option = input()
        os.system('clear')
        cls.menuChose(int(option))

    @classmethod
    def menuChose(cls, option):
        if option == 1:
            BattleGame.startGame()
        elif option == 2:
            cls.printFile("Instructions.txt")
        elif option == 3:
            cls.printFile("Credits.txt")
        elif option == 4:
            cls.printFile("ClassStats.txt")
        input()
        os.system('clear')
        cls.printMenuChose()

class BattleGame:

    @classmethod
    def startGame(cls):
        print("Name the first warrior:")
        warrior1 = Warrior(input())
        UiMaker.printFile("ClassChooser.txt")
        warrior1.choseClass(int(input()))

    @staticmethod
    def printHomeScreen():
        os.system('clear')
        if int(columns) < 80:
            UiMaker.printFile("HomeScreenSmall.txt")
        else:
            UiMaker.printFile("HomeScreen.txt")
        input()
        os.system('clear')
        UiMaker.printMenuChose()

class Warrior:
    
    def __init__(self, name, health=1, attkMax=1, blckMax=1, mana=1, className=1):
        self.Name = name
        self.Health = health
        self.AttkMax = attkMax
        self.BlckMax = blckMax
        self.Mana = mana
        self.ClassName = className

    def choseClass(self, className):
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

def main():
    btgm = BattleGame()
    btgm.printHomeScreen()

if __name__ == "__main__":
    main()