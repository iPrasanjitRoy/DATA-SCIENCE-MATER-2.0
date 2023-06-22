import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from TEST2.Test_Table")

for i in mycursor.fetchall():
    print(i)

mydb.close()



