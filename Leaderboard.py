from pathlib import Path
import json

class Leaderboard:
    def __init__(self, userList=None):
        if userList == None:
            self.userList = []
        else:
            self.userList = userList
            
    def sortUserListByWins(self):
        self.userList.sort(key=lambda user: user.wins, reverse=True)

    def getUserById(self, id):
        return next((user for user in self.userList if user.id == id), None)

    def addUserToLeaderBoard(self, user):
        self.userList.append(user)

    def dumpData(self):
        return json.dumps([user.dump() for user in self.userList], indent=4)

    # loads user data from default file path or 
    def loadData(self, path=None):
        fullPath = "leaderboard.json" if path is None else path/"leaderboard.json"
        with open(fullPath,"r") as json_file:
            self.userList = [self.__getUserFromJson(user) for user in json.loads(json_file.read())]

    # sets objects userList from users that are found in a json string 
    def loadDataWithJson(self, jsonStr):
        self.userList = [self.__getUserFromJson(user) for user in json.loads(jsonStr)]

    def saveData(self, path=None):
        fullPath = "leaderboard.json" if path is None else path/"leaderboard.json"
        file = open(fullPath, "w")
        charactersWritten = file.write(self.dumpData())
        file.close()

    @staticmethod
    def __getUserFromJson(jsonUser):
        return User(int(jsonUser['User']['id']),
                jsonUser['User']['name'],
                jsonUser['User']['wins'],
                jsonUser['User']['looses'])

class User:
    def __init__(self, id, name, wins, looses):
        self.id = id
        self.name = name
        self.wins = wins
        self.looses = looses
        self.totalGames = wins+looses

    def dump(self):
        return {"User": {'id': self.id,
                         'name': self.name,
                         'wins': self.wins,
                         'looses': self.looses,
                         'totalGames': self.totalGames}}