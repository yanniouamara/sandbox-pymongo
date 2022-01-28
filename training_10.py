from pymongo import MongoClient, GEO2D
from settings import *


def main():
    client = MongoClient(MONGODB_DSN)
    db = client[MONGODB_DB]

    db.caracteristiques.aggregate([
        {"$set":
            {"lat_":
                {"$replaceOne":
                     {"input": "$lat",
                      "find": ",",
                      "replacement": "."}
                 }
             }
         },
        {"$set":
            {"long_":
                {"$replaceOne":
                     {"input": "$long",
                      "find": ",",
                      "replacement": "."}
                 }
             }
         },
        {"$set": {
            "location":
                [{"type": "Point"},
                 {"coordinates":
                     [{"$convert":
                         {
                               "input": "$long_",
                               "to": "double",
                               "onError": 0}
                     },
                         {"$convert":
                             {
                               "input": "$lat_",
                               "to": "double",
                               "onError": 0
                             }
                         }]
                  }
                 ]}
        }
    ]).pretty()

    db.caracteristiques.create_index([("coordinates", GEO2D)])
    '''
    TRAINING : 
    Convert `long` and `lat` in `caracteristiques` to GeoJSON Point for all documents
    Create 2dsphere index
    
    ONLY 2 QUERIES ALLOWED
    '''


if __name__ == '__main__':
    main()
