from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    db.vehicules.insert_one({"_id": '154 742 270', "motor": 6})
    '''
    TRAINING : Create 1 `vehicules` where 
        `motor` = 6
        `id_vehicules` = '154 742 270'
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
