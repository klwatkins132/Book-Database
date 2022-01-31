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

sql = "INSERT INTO book (BookTitle, BookAuthor, BookGenre, BookPrice, BookQuantity) VALUES (%s, %s,%s, %s, %s)"
val = [
  ('The Looking Glass Wars', 'Frank Beddor', 'Fantasy', 37.99, 3),
  ('Contact', 'Carl Sagan', 'Fantasy', 25.99, 8),\
  ('The Dark Tower: The Gunslinger', 'Stephen King', 'Fantasy', 35.99, 6),\

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")