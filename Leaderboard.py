import json

class Leaderboard:
    def __init__(self, userList=None):
        if userList == None:
            self.userList = []
        else:
            self.userList = userList

    @classmethod
    def readLeaderboard(cls):
        with open("leaderboard.json","r") as json_file:
            return json.load(json_file)

    def addUserToLeaderBoard(self, user):
        self.userList.append(user)

    def dumpData(self):
        return json.dumps([user.dump() for user in self.userList], indent=4)

    # sets objects userList from users that are found in a json string 
    def loadData(self, jsonStr):
        self.userList = [self.__getUserFromJson(user) for user in json.loads(jsonStr)]

    def saveData(self):
        file = open("leaderboard.json", "w")
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