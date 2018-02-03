import pymongo


conn = pymongo.MongoClient("mongodb://localhost")
db = conn.school
students = db.students

try:
    docs = students.find()
except Exception as e:
    print("Unexpected erro!", type(e), e)

for doc in docs:
    min_score = min([
        score["score"] for score in doc["scores"] if score["type"] == "homework"
    ])

    doc["scores"].remove(
        {
            "type": "homework",
            "score": min_score
        })

    students.replace_one({"_id": doc["_id"]}, doc)