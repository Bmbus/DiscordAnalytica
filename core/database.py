from pymongo import MongoClient
from CONFIG import CONNECTION, CLUSTER, DB
from dataminer import utcnow


class DbClient:
    """CREATES A CONNECTION TO YOUR DATABASE"""
    def __init__(self):
        cluster = MongoClient(CONNECTION)
        db = cluster[CLUSTER]
        self.collection = db[DB]

    def __call__(self, *args, **kwargs):
        return self.collection


class Database(DbClient):
    """EXECUTE DATABASE STUFF"""
    def init_db(self, guildid: str):
        try:
            self.collection.insert_one(db_layout(guildid))
            return
        except:
            return

    def delete_db(self, guildid: str):
        try:
            self.collection.delete_one({"_id": guildid})
            return
        except:
            return


def db_layout(guildid: str):
    """DEFAULT DATABASE LAYOUT"""
    default_data = {"_id": guildid,
                    "message": [],
                    "status": [],
                    "reaction": [],
                    "bot_requests": [],
                    "userjoins": [],
                    "userleave": [],
                    "mentions": [],
                    "bot_msg": [],
                    "server_join": utcnow,
                    "prefix": "",
                    "other_prefix": []
                    }

    return default_data
