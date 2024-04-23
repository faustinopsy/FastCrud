from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['usuarios']
        self.collection = self.db['usuarios']
