from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    db.vehicules.aggregate([{"$lookup" :
                                 {"from": "caracteristiques",
                                  "localField": "_id",
                                  'foreignField': "Num_Acc",
                                  'as': 'adr'}})

    '''
    TRAINING : 
        Get all `adr`.`caracteristiques` and `num_veh`.`vehicules` 
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
