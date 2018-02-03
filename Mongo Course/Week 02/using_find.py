import pymongo
import sys

# Estabilish connection
connection = pymongo.MongoClient("mongodb://localhost")

# Get a handle to the school db
db = connection.school
scores = db.scores


def find():
    print("find reporting for duty!")

    query = {'type': 'exam'}
    try:
        cursor = scores.find(query)
    except Exception as e:
        print("Unexpected erro!", type(e), e)

    sanity = 0
    for doc in cursor:
        print(doc)
        sanity +=1
        if sanity > 10:
            break

def find_one():
    print("Find one reporting for duty!")

    query = {'student_id': 10}

    try:
        doc = scores.find_one(query)
    except Exception as e:
        print("Unexpected erro!", type(e), e)

    print(doc)


# find_one()

find()
