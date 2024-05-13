from pymongo import MongoClient


class DbService:
    DECKS_COLLECTION = "decks"
    EVENTS_COLLECTION = "events"
    PERSONAL_POOL = "personal_pool"
    PILOTS_COLLECTION = "pilots"
    POOL_COLLECTION = "pool"

    def __init__(self, uri="mongodb://localhost:27017", db_name="mtg_decks_db"):
        self.__uri = uri
        self.__db_name = db_name
        self.__client = MongoClient(self.__uri)
        self.__db = self.__client[self.__db_name]

    def pool_collection(self):
        return self.__db[self.POOL_COLLECTION]

    def personal_pool_collection(self):
        return self.__db[self.PERSONAL_POOL]

    def deck_collection(self):
        return self.__db[self.DECKS_COLLECTION]

    def pilots_collection(self):
        return self.__db[self.PILOTS_COLLECTION]

    def events_collection(self):
        return self.__db[self.EVENTS_COLLECTION]

