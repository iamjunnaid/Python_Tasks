import mysql.connector

conne = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Sqlpassword',
    database = 'first_database'
)

my_cursor = conne.cursor()

conne.commit()
conne.close()
print('Connection Successfull')