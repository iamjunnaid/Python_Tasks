"""
Create MySQL table from Python
Now you know how to connect to a MySQL server from Python, In this section, we will learn how to create a table in MySQL from Python. 
Let\’s create table Laptop under the First_database.
"""
import mysql.connector

conne = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Sqlpassword',
    database = 'first_database'
)

mysql_Create_Table = """CREATE TABLE LAPTOP(
                Id int(11) NOT NULL,
                Name varchar(250) NOT NULL,
                Price float NOT NULL,
                Purchase_date Date NOT NULL,
                PRIMARY KEY(Id))"""

cursor = conne.cursor()
exec = cursor.execute(mysql_Create_Table)
print('Laptop Table Created Successfully')

