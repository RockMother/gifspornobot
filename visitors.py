import pymongo
import os

def getDb():
    client = pymongo.MongoClient(os.environ["MONGODB_URI"])
    return client.get_database("heroku_4wv17rnt")

def getCollection():
    return getDb().visitors

def saveVisited(chat_id, submission_id):
    visitors = getCollection()
    result = visitors.find_one({ 'chatId': chat_id })
    if result == None:
        result = visitors.insert_one({ 'chatId': chat_id, 'visited': []})
    visitors.update( {'chatId': chat_id}, {'$push': {'visited': submission_id}})
    
def getVisited(chat_id):
    result = getCollection().find_one({'chatId': chat_id})
    if result == None:
        return []
    return result['visited']
