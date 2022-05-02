import unittest

from pymongo import MongoClient

dbname = 'epam'
dbaddr = 'localhost'
dbport = 27017
collection = 'beatles-collection'
artistName = 'The Beatles'

# Connect to db
client = MongoClient(dbaddr, dbport)
mydb = client[dbname]
mycollection = mydb[collection]

class TestSum(unittest.TestCase):
    def test_mongodb_connect(self):
        self.assertEqual(print(mydb.list_collection_names()), None)

if __name__ == '__main__':
    unittest.main()        