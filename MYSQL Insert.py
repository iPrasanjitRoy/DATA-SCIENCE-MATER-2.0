import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO TEST.Test_Table VALUES (1001, 'Roy', 50.5, 200, 'PWS')")

mydb.commit()

mydb.close()




