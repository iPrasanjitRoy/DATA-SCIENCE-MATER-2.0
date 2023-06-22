import pymongo 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://prasanji:12345@cluster0.bxthqdz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)




db = client['PWSkill']
data = {"name" : "Prasanjit",
        "Age" : 50,
        "Subject" : "DataScience"
        }

coll_PWSkill = db["My_Record"]

coll_PWSkill.insert_one(data) 


for i in coll_PWSkill.find_one({'name' : 'Prasanjit'}):
    print(i) 


random = [
  {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "address": "123 Main Street",
    "city": "New York",
    "state": "NY",
    "country": "USA"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "age": 35,
    "email": "janesmith@example.com",
    "address": "456 Elm Street",
    "city": "Los Angeles",
    "state": "CA",
    "country": "USA"
  },
  {
    "id": 3,
    "name": "Alex Johnson",
    "age": 25,
    "email": "alexjohnson@example.com",
    "address": "789 Oak Street",
    "city": "Chicago",
    "state": "IL",
    "country": "USA"
  }
]


coll_PWSkill.insert_many(random) 

for i in coll_PWSkill.find():
    print(i) 

for i in coll_PWSkill.find({'id' : {"$gte" :    2}}): 
    print(i) 




