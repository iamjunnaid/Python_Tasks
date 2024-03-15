'''
Insert multiple rows into MySQL table using the cursor's executemany()
In the previous example, we have used execute() method of cursor object to insert a single record.

What if you want to insert multiple rows into a table in a single insert query from the Python application. Use the cursor's 
executemany() function to insert multiple records into a table.

Syntax of the executemany() method.


'''
import mysql.connector

try:
        conne = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'first_database'
        )
        cursor = conne.cursor()
        mysql_insert_query = '''INSERT INTO LAPTOP(Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)'''
        record = [(4, 'HP Pavilion',799,'2024-03-12'),
                  (5,'MSI WS75',599,'2024-03-11'),
                  (6,'Microsoft Surface',1199,'2024-03-12')]
        cursor.executemany(mysql_insert_query,record)
        conne.commit()
        print(cursor.rowcount,'Record Inserted Successfully')

except mysql.connector.Error as error:
        print('Record failed to insert into Table {}'.format(error))

finally:
        if conne.is_connected():
            cursor.close()
            conne.close()
            print('MySQL is closed')




