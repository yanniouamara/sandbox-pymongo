from pymongo import MongoClient
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]


    db.caracteristiques.find({"location":
                                  {"$geoWithin":
                                       {'$centerSphere':
                                            [[43.4938100, -1.5230700], 5000]
                                        }
                                   }
                              },
                             {"Num_acc": 1}
                             )
    '''
    TRAINING : 
    Get all `Num_Acc` in `caracteristiques` around 5km from ["43,4938100", " -1,5230700"]
    
    ONLY 1 QUERY ALLOWED
    '''


if __name__ == '__main__':
    main()
