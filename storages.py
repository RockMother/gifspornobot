""" Provide access to the storage"""
import pymongo

class MongoStorage():
    """" Mongo storage """
    def __init__(self, connection_string, database_name):
        self.connection_string = connection_string
        self.database_name = database_name

    def __get_db(self):
        return pymongo.MongoClient(self.connection_string).get_database(self.database_name)

    def __get_collection(self):
        return self.__get_db().visitors

    def save_visited(self, chat_id, submission_id):
        """ Save visited """
        visitors = self.__get_collection()
        result = visitors.find_one({ 'chatId': chat_id })
        if result is None:
            result = visitors.insert_one({ 'chatId': chat_id, 'visited': []})
        visitors.update( {'chatId': chat_id}, {'$push': {'visited': submission_id}})
    
    def get_visited(self, chat_id):
        """ Gets visited list """
        result = self.__get_collection().find_one({'chatId': chat_id})
        if result is None:
            return []
        return result['visited']
