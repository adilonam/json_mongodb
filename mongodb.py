

from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MongoDb:
    json_array = []
    client = None
    uri = ""
    def __init__(self, uri) -> None:
        self.uri = uri
    def read_file(self):
        import json

        with open('./data/json_array.json', 'r') as file:
            self.json_array = json.load(file)

        for ja in self.json_array:
            ja['_id'] = ObjectId(ja['_id']['$oid'])


    def connect_db(self):
        # uri = "mongodb+srv://adilabbadi1996:xfClbv4jzWQLkmis@cluster0.thnqkdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Create a new client and connect to the server
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        self.client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")



    def save_data(self):
        db = self.client['First']  

        # Create or access a collection
        collection = db['Customers'] 

        # Insert data into the collection
        for data in self.json_array:
            filter_query = {"_id": data['_id']}
            update_query = {"$set": data}
            collection.update_one(filter_query , update_query, upsert=True)
        print("Data inserted successfully into MongoDB.")
    
    def start(self):
        self.connect_db()
        self.read_file()
        self.save_data()




        
