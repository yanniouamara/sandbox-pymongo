from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    db.vehicules.aggregate([{"$lookup":
                                 {"from": "caracteristiques",
                                 "localField": "Num_Acc",
                                 'foreignField': "Num_Acc",
                                 'as': 'lookupadr'}
                             },
                            {"$project":
                                 {"_id": "0",
                                  "lookupadr.adr": 1,
                                  "num_veh": 1}
                             }
                            ])

'''
    TRAINING : 
        Get all `adr`.`caracteristiques` and `num_veh`.`vehicules` 
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
