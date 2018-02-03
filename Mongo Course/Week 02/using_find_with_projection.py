import pymongo
import sys


connection = pymongo.MongoClient("mongodb://localhost")

# db = connection.school
db = connection.reddit
# scores = db.scores
stories = db.stories


def find():
    print("find reporting for duty!")

    # query = {'type': 'exam'}
    # query = {'type': 'exam', 'score': {'$gt': 50, '$lt':70}}
    query = {'title': {'$regex': 'apple|google', '$options': 'i'}}
    # projection = {'student_id': 1, '_id': 0}
    projection = {'title': 1, '_id': 0}
    
    try:
        # cursor = scores.find(query, projection)
        cursor = stories.find(query, projection)
        # cursor = scores.find(query)
    except Exception as e:
        print("Unexpected erro!", type(e), e)

    sanity = 0
    for doc in cursor:
        print(doc)
        sanity +=1
        if sanity > 10:
            break

find()