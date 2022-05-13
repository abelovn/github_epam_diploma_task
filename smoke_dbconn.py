import pymongo
# import random

dbname = 'epam'
dbaddr = 'localhost'
dbport = 27017
collection = 'beatles-collection'
artistName = 'The Beatles'

# uri = 'mongodb://<dbuser>:<dbpassword>@XXXX.cloudclusters.io/<database_name>?authSource=admin'.format(dbuser,dbpassword)
uri = 'mongodb://localhost:27017/?authSource=admin'
## Get mongo client
client = pymongo.MongoClient(uri)
mydb = client[dbname]

mycollection = mydb[collection]


# def find_document(collection, elements, multiple=False):
#     """ Function to retrieve single or multiple documents from a provided
#     Collection using a dictionary containing a document's elements.
#     """
#     if multiple:
#         results = collection.find(elements)
#         return [r for r in results]
#     else:
#         return collection.find_one(elements)


documentcount = mycollection.count_documents({})
print (documentcount)


# result = find_document(mycollection, {'kind': 'song'}, True)
# print(result)

