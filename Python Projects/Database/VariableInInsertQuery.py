'''
Use Python Variables in a MySQL Insert Query
Sometimes you need to insert a Python variable value into a table's column. For example, in the user signup form user enter his/her details. 
You can take those values in Python variables and insert them into a table.

We can insert Python variables into the table using the prepared statement and parameterized query.
Using a parameterized query, we can pass Python variables as a query parameter in which placeholders (%s) used for parameters.

'''

import mysql.connector

def insert_variable_query(id, name, price, purchase_date):
    try:
        conne = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'first_database'
        )
        cursor = conne.cursor()
        mysql_insert_query = '''INSERT INTO LAPTOP(Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)'''
        record = (id, name, price,purchase_date)
        cursor.execute(mysql_insert_query,record)
        conne.commit()
        print('Record Inserted Successfully')

    except mysql.connector.Error as error:
        print('Record failed to insert into Table {}'.format(error))

    finally:
        if conne.is_connected():
            cursor.close()
            conne.close()
            print('MySQL is closed')

insert_variable_query(2,'Dell Xpire',1299,'2024-03-11')
insert_variable_query(3,'Apple Macbook Air',2199,'2024-03-15')


