from pathlib import Path
import unittest
import importlib.util

path = Path(__file__).parent.parent.absolute()
spec = importlib.util.spec_from_file_location("Leaderboard",  path / "Leaderboard.py")
Leaderboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Leaderboard)

class TestLeaderboard(unittest.TestCase):
    def createDefaultLeaderboard(self):
        user1 = Leaderboard.User(1, "jack", 4,10)
        user2 = Leaderboard.User(2, "marsh", 9 ,11)
        user3 = Leaderboard.User(3, "zak", 2, 2)

        leaderboard = Leaderboard.Leaderboard()

        leaderboard.addUserToLeaderBoard(user1)
        leaderboard.addUserToLeaderBoard(user2)
        leaderboard.addUserToLeaderBoard(user3)
        return leaderboard
        
    def testLeaderboardDump(self):

        leaderboard = self.createDefaultLeaderboard()
        jsonStr = leaderboard.dumpData()

        leaderboardTest = Leaderboard.Leaderboard()
        leaderboardTest.loadDataWithJson(jsonStr)

        self.assertEqual(leaderboardTest.userList[1].name ,leaderboard.userList[1].name)

    def testSavingAndReadingFromFile(self):
        
        leaderboard = self.createDefaultLeaderboard()
        self.assertEqual(leaderboard.userList[1].name, "marsh")
        leaderboard.saveData(Path("tests"))

        leaderboard2 = Leaderboard.Leaderboard()
        
        self.assertEqual(len(leaderboard2.userList), 0)

        leaderboard2.loadData(Path("tests"))

        self.assertGreater(len(leaderboard2.userList), 0)
        self.assertEqual(leaderboard2.userList[1].name, "marsh")

    def testGetUserById(self):
        leaderboard = self.createDefaultLeaderboard()
        self.assertEqual(leaderboard.getUserById(2).name, leaderboard.userList[1].name)

    def testChangeUserData(self):
        leaderboard = self.createDefaultLeaderboard()
        self.assertEqual(leaderboard.getUserById(1).wins, 4)
        leaderboard.getUserById(1).wins += 1
        self.assertEqual(leaderboard.getUserById(1).wins, 5)

    def testOverwriteJsonFile(self):
        leaderboard = self.createDefaultLeaderboard()
        self.assertEqual(leaderboard.getUserById(1).wins, 4)
        leaderboard.getUserById(1).wins += 1
        leaderboard.saveData(Path("tests"))
        leaderboard2 = Leaderboard.Leaderboard()
        leaderboard2.loadData(Path("tests"))
        self.assertEqual(leaderboard2.getUserById(1).wins, 5)


if __name__ == '__main__':
    unittest.main()