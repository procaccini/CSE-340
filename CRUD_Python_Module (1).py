# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'Gengar00' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, data):
        return self.collection.find(data, {'_id': False})

#    def read_one(self, data):
#        return self.collection.find(data, {'_id': False})

    
    # implement update
    def update(self, query, new_data):
        if query is not None and new_data is not None:
            result = self.collection.update_one(query, {'$set': new_data})
            return result.modified_count > 0
        else:
            raise Exception("Query or new data is missing")

    # implement delete
    def delete(self, data):
        if data is not None:
            result = self.collection.delete_one(data)
            return result.deleted_count > 0
        else:
            raise Exception("No data provided for delete")