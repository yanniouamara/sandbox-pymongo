from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    '''
    TRAINING : 
    Convert `long` and `lat` in `caracteristiques` to GeoJSON Point for all documents
    Create 2dsphere index
    
    ONLY 2 QUERIES ALLOWED
    '''


if __name__ == '__main__':
    main()
