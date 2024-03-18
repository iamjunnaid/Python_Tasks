'''
Insert timestamp and DateTime into a MySQL table using Python
For example, you have a date column in a MySQL table. Let's see how to prepare an insert query to add DateTime into a table from Python

'''
from datetime import datetime
import mysql.connector

try:
    conne = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'first_database'
        )
    mysql_insert_query = '''INSERT INTO LAPTOP(Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)'''
    cursor = conne.cursor()
    curr_Date = datetime.now()
    format_date = curr_Date.strftime('%Y-%m-%d %H:%M:%S')
    insert_tupla = [(8,'Lenovo Thinkpad T495',2199,curr_Date),
                    (9,'Microsoft Surface',1599,curr_Date),
                    (10,'Dell Ideapad',1399,curr_Date)]
    result = cursor.executemany(mysql_insert_query,insert_tupla)
    conne.commit()
    print('Date Record Successfully')

except mysql.connector.Error as error:
    conne.rollback()
    print('Failed to insert Date Record {}'.format(error))

finally:
    if conne.is_connected():
        cursor.close()
        conne.close()
        print('Connection Closed')
