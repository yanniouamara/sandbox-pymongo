from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    '''
    TRAINING : Create index on `num_veh`in `caracteristique`
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
