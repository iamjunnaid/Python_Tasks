'''
We are implementing the Employee Information System. In this exercise, I have created tables that includes the Photo and Biodata

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
    db = "Create database Employee"
    cursor.execute(db)
    print('Employee Database Created')

except:
    print('Employee Database Creation Error')