from pathlib import Path

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
        option = int(input())
        cls.menuChose(option)

    @classmethod
    def menuChose(cls, option):
        if option == 1:
            pass
        elif option == 2:
            cls.printFile("Instructions.txt")
        elif option == 3:
            cls.printFile("Credits.txt")
        elif option == 4:
            cls.printFile("ClassStats.txt")

class BattleGame:

    @classmethod
    def startGame(cls):
        cls.printHomeScreen()
        

    @staticmethod
    def printHomeScreen():
        UiMaker.printFile("HomeScreen.txt")
        input()
        UiMaker.printMenuChose()
        

def main():
    btgm = BattleGame()
    btgm.startGame()

if __name__ == "__main__":
    main()