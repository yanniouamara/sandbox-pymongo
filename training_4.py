from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    '''
    TRAINING : Add the column `why_not`='because' in `vehicules` 
        ONLY for documents where `motor` is >= `3` and < 5
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
