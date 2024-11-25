from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["crm"]
collection = db["test"]

test = {
    "name" : "test",
    "hospital" : "test",
    "priority" : "test"
}


collection.insert_one(test)

retreive = collection.find_one(test)
print(retreive)

collection.delete_one(test)