import json
from typing import Collection
from flask import Flask, render_template, url_for, request
import requests
from pymongo import MongoClient
from prometheus_flask_exporter import PrometheusMetrics

import time
from bson import json_util
from time import sleep
import os
import socket
from datetime import datetime

def stress_test():
    a = b = 1
    element = 1750000

    for _ in range(int(element-2)):
        a, b = b, a + b

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# fmt = '%Y-%m-%d %H:%M:%S'

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

def getdata(search):
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
    
@app.route("/")
def index():
     return render_template("index.html", ipaddr = socket.gethostbyname(socket.gethostname()))


@app.route("/updatedb")
def updatedb():
     my_db.drop_collection(my_collection)
     return render_template("updatedb.html", total_count = getdata(artist_name))


@app.route("/dropdb")
def dropdb():
     my_collection.drop()
     return render_template("dropdb.html")

@app.route("/display")
def display():
     result = []
     full_list = my_collection.find({"artistName" : artist_name})
     dist_field = full_list.distinct("collectionName")
     for el in dist_field:
         result.append([my_collection.find_one({"collectionName": el, "artistName" : artist_name})["releaseDate"], el])
     return render_template("display.html", dist_field = sorted(result))

@app.route("/displayall", methods=['POST', 'GET'])
def displayall():
     if request.method == "POST" and (request.form['number']).isdigit():
         record_num = request.form['number']
         full_list = my_collection.find({"artistName": artist_name}).limit(int(record_num))
     else:
         full_list = my_collection.find({"artistName": artist_name})
     
     return render_template("displayall.html", full_list = full_list)

@app.route('/stress')
def stress():
    timestamp = datetime.today().replace(microsecond=0)
    stress_test()
    return render_template('stress.html', timestamp=timestamp)     

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')