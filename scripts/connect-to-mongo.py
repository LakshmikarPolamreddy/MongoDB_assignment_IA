"""
#DAV6100:M13 Assignment
#Author: brandon chiazza
#Version: 1.0

You will need to install dependencies for this script most likely. pymongo, dnspython, and pprint (optional). To install these modules use pip, sudo or conda
Example: 

#python -m pip install pymongo 
#python -m pip install dnspython
"""

#import relevant modules
import pymongo
import pprint

#the following connects to your client. note this is only an example. You will need to use your connection string specified in your mongodb instance
#connect
client = pymongo.MongoClient("mongodb+srv://root:<your_cluster_password>@cluster0-tk9ld.mongodb.net/test?retryWrites=true&w=majority")

#specify database
db = client.sample_airbnb

#specifyt connection
col = db.listingsAndReviews

#query specific listing and store as result
query = {"_id":"10006546"}
result = col.find(query)

#print results
for x in result:
  print(x)


