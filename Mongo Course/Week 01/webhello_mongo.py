import bottle
import pymongo


@bottle.route('/')
def index():
     connection = pymongo.MongoClient('localhost', 27017)

     db = connection.video

     movies = db.movies

     item = movies.find_one()

     return '<b> Movie title: %s' % item['title']


bottle.run(host='localhost', port=8080)
