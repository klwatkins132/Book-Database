import mysql.connector
import os

from dotenv import load_dotenv

load_dotenv()

Host = os.getenv('Host')
User = os.getenv('User')
Passwd = os.getenv('Passwd')
Database = os.getenv('Database')
Auth_plugin = os.getenv('Auth_plugin')

mydb = mysql.connector.connect(
Host, User, Passwd, Database, Auth_plugin,
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM book")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)