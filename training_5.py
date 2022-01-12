from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    db.vehicules.update_many({"num_veh": "B01"}, {"$unset": {"vehicules.obsm": 1}})

    '''
    TRAINING : DELETE column `obsm` in `vehicules` 
        ONLY for documents where `num_veh` is `B01`
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
