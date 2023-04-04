import pymongo
import certifi

con_str = "mongodb+srv://giancarlocalette0:admin@cluster0.55crveh.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore")