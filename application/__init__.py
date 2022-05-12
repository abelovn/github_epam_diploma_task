import json
from typing import Collection
from flask import Flask, render_template, url_for, request
import requests
from pymongo import MongoClient

import time
from bson import json_util
from time import sleep
import os

app = Flask(__name__)

# db_name = 'epam'
# db_addr = 'localhost'
# db_port = 27017
# collection = 'beatles-collection'
# artist_name = 'The Beatles'
#connection_str = 'mongodb://localhost:27017/?authSource=admin'

# default
db_name = "test"
aartist_name = "test"
collection = "test"
connection_str = "test"
fmt = '%Y-%m-%d %H:%M:%S'

try:
    
    db_name = os.environ['db_name']
    artist_name = os.environ['artist_name']
    collection = os.environ['collection']
    connection_str = os.environ['connection_str']
except:
    print("Env vars are not set")    

try:
    # client = MongoClient(db_addr, db_port)
    client = MongoClient(connection_str)
    my_db = client[db_name]
    my_collection = my_db[collection]
except:
    print("DB connection failed")
def insert_document(collection, data):
   
    return my_collection.insert_one(data).inserted_id

def getData(search):
    start = time.time()
    total_count = 0
    record_count = 1
    record_offset = 0
    max_offset = 200
    while record_count > 0:
        try:
            response = (requests.get('https://itunes.apple.com/search?term=' 
            + str(search)+'&offset='
            + str(record_offset)+'&limit=' 
            + str(max_offset-1))).json()
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')
            continue
        record_count = response["resultCount"]
        total_count += record_count 
        record_offset = int(record_offset) + max_offset
        for one_record in response["results"]:
            if not one_record:
                insert_document(my_collection, None)
                continue
            insert_document(my_collection, one_record)
        end = time.time()
        print(end - start)    
    return total_count
    
# Main page
@app.route("/")
def index():
     return render_template("index.html")

# Drop db and get records
@app.route("/updatedb")

def updatedb():
     my_db.drop_collection(my_collection)
     return render_template("updatedb.html", total_count = getData(artist_name))

# @app.route("/count")
# def update():
#      documentcount = my_collection.count_documents({})
#      print (my_collection.distinct("collectionName"))

#      return render_template("count.html", documentcount = documentcount)     

# Output the data by collectionName sorted by relaseDate
@app.route("/display")
def display():
     result = []
     full_list = my_collection.find({"artistName" : artist_name})
     dist_field = full_list.distinct("collectionName")
     for el in dist_field:
         result.append([my_collection.find_one({"collectionName": el, "artistName" : artist_name})["releaseDate"], el])
     return render_template("display.html", dist_field = sorted(result))

# Output all data
@app.route("/displayall", methods=['POST', 'GET'])
def displayall():
     if request.method == "POST" and (request.form['number']).isdigit():
         record_num = request.form['number']
         full_list = my_collection.find({"artistName": artist_name}).limit(int(record_num))
     else:
         full_list = my_collection.find({"artistName": artist_name})
     
     return render_template("displayall.html", full_list = full_list)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')