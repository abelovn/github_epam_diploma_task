import json
from flask import Flask, render_template, url_for, request
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


from bson import json_util
from time import sleep
from flask import url_for

app = Flask(__name__)

# Variables


dbname = 'epam'
dbaddr = 'localhost'
dbport = 27017
collection = 'beatles-collection'
artistName = 'The Beatles'

# Connect to db
client = MongoClient(dbaddr, dbport)
mydb = client[dbname]
mycollection = mydb[collection]




try:
   # The ismaster command is cheap and does not require auth.
#    
   print("Server is  available")
   print(client.server_info())

   
except ConnectionFailure:
   print("Server not available")


print("*****************")    
print(mydb.list_collection_names())



# Start local project
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')