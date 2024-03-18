'''
We are implementing the Hospital Information System. In this exercise, I have created two tables, Hospital and Doctor. You need to 
create those two tables on your database server before starting the exercise.

'''
import mysql.connector
conne = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Sqlpassword',
    database = ''
)

cursor = conne.cursor()
try:
    db = "Create database Hospital"
    cursor.execute(db)
    print('Hospital Database Created')

except:
    print('Hospital Database Creation Error')