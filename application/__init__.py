import json
from typing import Collection
from flask import Flask, render_template, url_for, request
import requests
from pymongo import MongoClient

import time
from bson import json_util
from time import sleep
from flask import url_for

app = Flask(__name__)

dbname = 'epam'
dbaddr = 'localhost'
dbport = 27017
collection = 'beatles-collection'
artistName = 'The Beatles'

client = MongoClient(dbaddr, dbport)
mydb = client[dbname]
mycollection = mydb[collection]


def insert_document(collection, data):
   
    return collection.insert_one(data)

def getData(search):
    start = time.time()
    total_count = 0
    record_count = 1
    record_offset = 0
    max_offset = 200
    while record_count > 0:

        response = (requests.get('https://itunes.apple.com/search?term=' + str(search)+
            '&offset='+
            str(record_offset)+
            '&limit='+
            str(max_offset-1))
        ).json()
        record_count = response["resultCount"]
        total_count += record_count 
        record_offset = int(record_offset) + max_offset
        for one_record in response["results"]:
            if not one_record:
                insert_document(mycollection, None)
                continue
            insert_document(mycollection, one_record)
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
     mydb.drop_collection(mycollection)
     return render_template("updatedb.html", totalCount = getData(artistName))




@app.route("/count")
def update():
     documentcount = mycollection.count_documents({})
     print (mycollection.distinct("collectionName"))

     return render_template("count.html", documentcount = documentcount)     

# Output the data by collectionName sorted by relaseDate
@app.route("/display")
def display():
     result = []
     fullList = mycollection.find({"artistName":artistName})
     distField = fullList.distinct("collectionName")
     for el in distField:
         result.append([mycollection.find_one({"collectionName":el, "artistName":artistName})["releaseDate"], el])
     return render_template("display.html", distField = sorted(result))

# Output all data
@app.route("/displayall", methods=['POST', 'GET'])
def displayall():
     if request.method == "POST" and (request.form['number']).isdigit():
         recNum = request.form['number']
         fullList = mycollection.find({"artistName":artistName}).limit(int(recNum))
     else:
         fullList = mycollection.find({"artistName":artistName})
     
     return render_template("displayall.html", fullList = fullList)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')