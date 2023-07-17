import pymongo

myclient = pymongo.MongoClient("mongodb://apiuser:apipass@mongodb:27017/test") 
mydb = myclient["test"] #db
