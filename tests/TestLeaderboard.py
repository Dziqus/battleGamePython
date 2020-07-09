from pathlib import Path
import unittest
import importlib.util

path = Path(__file__).parent.parent.absolute()
spec = importlib.util.spec_from_file_location("Leaderboard",  path / "Leaderboard.py")
Leaderboard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Leaderboard)

class TestLeaderboard(unittest.TestCase):

    def test1(self):
        user1 = Leaderboard.User(1, "jack", 10,10)
        user2 = Leaderboard.User(2, "marsh", 9 ,11)
        user3 = Leaderboard.User(3, "zak", 2, 2)

        leaderboard = Leaderboard.Leaderboard()

        leaderboard.addUserToLeaderBoard(user1)
        leaderboard.addUserToLeaderBoard(user2)
        leaderboard.addUserToLeaderBoard(user3)

        jsonStr = leaderboard.dumpData()

        leaderboardTest = Leaderboard.Leaderboard()
        leaderboardTest.loadData(jsonStr)

        leaderboardTest.saveData()

        self.assertEqual(leaderboardTest.userList[1].name ,leaderboard.userList[1].name)

if __name__ == '__main__':
    unittest.main()