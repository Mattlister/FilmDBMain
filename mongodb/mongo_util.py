# import datetime module
import datetime
# import pymongo module
import pymongo
# connection string
client = pymongo.MongoClient("mongodb+srv://gsweene2:<Qu4ntum2020!>@firstcluster-obuqd.mongodb.net/filmDB?retryWrites=true&w=majority")
# test
db = client['SampleDatabase']
# define collection
collection = db['SampleCollection']
# sample data
document = {"company":"Capital One",
"city":"McLean",
"state":"VA",
"country":"US"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
print(id)