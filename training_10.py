from pymongo import MongoClient, GEO2D
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    # db.caracteristiques.aggregate([
    #     {"$project": {
    #         "lat": {
    #             "$convert": {
    #                 "input": {
    #                     "$reduce": {
    #                         "input": {
    #                             "$split": ['$lat', ',']},
    #                         "initialValue": '',
    #                         "in": {
    #                             "$concat": ['$$value', '.', '$$this']}
    #                     }
    #                 },
    #                 "to": 'double',
    #                 "onError": 0
    #             }
    #         }
    #     }}
    # ])

    db.caracteristiques.aggregate([
        {"$set": {"coordinates": [{"$toDecimal": "$long"}, {"$toDecimal": "$lat"}]}},
        {"$out": "caracteristiques"}])
    #
    # db.caracteristiques.create_index([("coordinates", GEO2D)])
    '''
    TRAINING : 
    Convert `long` and `lat` in `caracteristiques` to GeoJSON Point for all documents
    Create 2dsphere index
    
    ONLY 2 QUERIES ALLOWED
    '''


if __name__ == '__main__':
    main()
