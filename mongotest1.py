import pymongo
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://ayesha:ayesha@ayesha.qeyjt5d.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
d={
    "name":"Ayesha",
    "email":"ayeshafarhana@gmail.com",
    "phnno":"123456789"
}
db1 =uri['mongotest']
coll=db1['test']
coll.insert_one(d)