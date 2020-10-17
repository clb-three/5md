import json
from datetime import datetime

import pymongo

import server
from model.serialization.stringable import Stringable


class Session(Stringable):
    """A representation of a game session on the server"""

    def __init__(self, gamestate, started_time=datetime.now()):
        self.started_time = started_time
        self.gamestate = gamestate

    @classmethod
    def from_dict(cls, obj):
        return Session(obj['gamestate'], obj['started_time'])


class Database:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["5md"]
        self.sessions = db["sessions"]

    def store(self, gamestate):
        """Store a game in DB"""
        session = Session(gamestate)
        d = session.__dict__
        d['gamestate'] = json.loads(str(d['gamestate']))
        self.sessions.insert_one(d)

    def get_young_session(self):
        """Get a recent session or None if no such session"""
        try:
            most_recent = self.sessions.find().sort('started_time', pymongo.DESCENDING).next()
            now = datetime.now()
            difference = now - most_recent['started_time']
            if difference.total_seconds() / 60 >= 30:
                return None
            return Session.from_dict(most_recent)
        except StopIteration:
            return None


if __name__ == '__main__':
    db = Database()
    g = server.get_gameloop().gamestate
    db.store(g)
    print(db.get_young_session())
