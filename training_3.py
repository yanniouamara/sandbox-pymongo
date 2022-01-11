from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    '''
    TRAINING : Create 1 `vehicules` where 
        `motor` = 6
        `id_vehicules` = '154 742 270'
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
