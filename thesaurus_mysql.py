# pip install mysql-connector-python
import mysql.connector

con = mysql.connector.connect(
    user="xxxxx",
    password="xxxxx",
    host="x.x.x.x",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    # returns a list of tuples
    for result in results:
        print(result[0])
else:
    print("No word found!")