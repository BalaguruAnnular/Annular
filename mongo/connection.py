# import pymongo
# from pymongo import MongoClient
# from bson import ObjectId
# client= MongoClient("mongodb://localhost:27017/?readPreference=primary&ssl=false&directConnection=true")
# db = client['mydatabase']
# collection = db['user']

with open('speech_converter.py', 'w', newline='') as file:
    text= file.write()
    print(text)


# Transcribe = {"txt":"{text1}"}
# result = collection.update_one({"_id": ObjectId("66d9491de0d306369fb4e44d")}, {"$set": Transcribe}, upsert=True)

# print(result)
#to check the updated document:
# updated_document = collection.find_one(result)
