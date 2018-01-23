import pymongo

from pymongo import MongoClient


connection = MongoClient('localhost', 27017)

db = connection.video

movies = db.movies

item = movies.find_one()

print(item['title'])