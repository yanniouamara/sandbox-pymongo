from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    vehicules = db.vehicules.find({"motor": {"$gt": 2, "$lt": 5}})

    '''
    TRAINING : Get all `vehicules` where `motor` is >= `3` and < 5
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
