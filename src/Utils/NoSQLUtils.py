from pymongo import MongoClient


def getMongodbConnection():
    try:
        return MongoClient('localhost', 32768)
        print("Connected to mongodb successfully!!!")
    except:
        print("Could not connect to MongoDB")

def addToMongodb(conn, jsonData):
    # database
    db = conn.database

    # Created or Switched to collection names: my_gfg_collection
    collection = db.CurrencyRates

    # Insert Data
    rec_id = collection.insert_one(jsonData)
