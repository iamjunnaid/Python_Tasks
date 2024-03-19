'''
Connect to your database server and print its version.
Write SQL query to get the database server version.
Connect to the database and use cursor.execute() to execute this query.
Next, use cursor.fetchone() to fetch the record.

'''

import mysql.connector

def database_connection():
    conne = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'hospital')

    return conne

def connection_close(conne):
    if conne:
        conne.close()

def database_version():
    try:
        conne = database_connection()
        cursor = conne.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print('The current MySQL version is: ',db_version)
        connection_close(conne)

    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)


print('Database Version')
database_version()

