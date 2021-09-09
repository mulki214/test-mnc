import pymongo
from pymongo import MongoClient

connection = MongoClient("mongodb://MindiKindi2021:MindiKindi2021@cluster0-shard-00-00.olk9i.mongodb.net:27017,cluster0-shard-00-01.olk9i.mongodb.net:27017,cluster0-shard-00-02.olk9i.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-groo2n-shard-0&authSource=admin&retryWrites=true&w=majority")