import sqlite3


connection = sqlite3.connect('test.db')

cursor = connection.cursor()

# sql = "".join([
#     "CREATE TABLE IF NOT EXISTS students(",
#     "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,",
#     " name VARCHAR(50),",
#     " age INTEGER)"
# ])

# print(sql)
# sql = "".join([
#     "drop table Students"
# ])

sql = "".join([
    "INSERT INTO Students (name, age) VALUES('Peter', 12)"
])

# sql = "".join([
#     "select * from Students"
# ])

cursor.execute("SELECT * FROM students")
# cursor.execute(sql)
# connection.commit()
# cursor.close()
# connection.close()

data = cursor.fetchall()
for line in data:
    print(line)