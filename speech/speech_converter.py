import pymongo
from pymongo import MongoClient
from bson import ObjectId
import speech_recognition as sr


# Mongo Connection 
client= MongoClient("mongodb://localhost:27017/?readPreference=primary&ssl=false&directConnection=true")
db = client['mydatabase']
collection = db['callerDetails']


def speech_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    
# Example usage
audio_files = [r"C:\\Users\\Intern\\Downloads\\harvard.wav"]
for audio_file in audio_files:
    text1 = speech_to_text(audio_file)
    
print("TEXT:", {text1})
# Save Text to mongodb
Transcribe = text1
result = collection.update_one({"_id": ObjectId("66dad9d345f66a62219bda08")}, 
                               {"$set": {"text": Transcribe}}, upsert=True)

# result = collection.update_many({"_id": ObjectId("66dad9d345f66a62219bda08")}, 
#                                {"$set": {"text": Transcribe}},
#                                upsert = { "$set" : { "is_Active" : "False" }})

# query_filter = { "<field to match>" : "<value to match>" }
# update_operation = { "$set" : 
#     { "<field name>" : "<value>" }
# }
# updated_document = collection.find_one({"_id":ObjectId("66dad9ca45f66a62219bda05") })

print('/n')
print("Updated Document:", result)
