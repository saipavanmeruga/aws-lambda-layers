import mysql.connector
def caller():
  print("inside caller function for mysql")
  mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword")

  print(mydb)

caller()
