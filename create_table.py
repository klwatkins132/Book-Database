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

mycursor.execute("DROP TABLE IF EXISTS BOOK")


value = " CREATE TABLE book (" \
  + "IDnumber INT KEY AUTO_INCREMENT," \
  + "BookTitle VARCHAR(100)," \
  + "BookAuthor VARCHAR(100)," \
  + "BookGenre VARCHAR(100)," \
  + "BookPrice INT," \
  + "BookQuantity INT )"

mycursor.execute(value)
mydb.close()