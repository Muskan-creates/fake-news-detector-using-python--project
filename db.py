import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fakenewsdetection"
)

mycursor = mydb.cursor()