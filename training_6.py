from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    db.vehicules.create_index({"num.veh": 1})

    '''
    TRAINING : Create index on `num_veh`in `caracteristiques`
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
