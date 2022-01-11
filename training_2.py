from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    '''
    TRAINING : Get all `vehicules` where `motor` is >= `3` and < 5
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
