'''
Delete a Single Row from a MySQL table

'''

import mysql.connector

def database_connection():
    conne = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Sqlpassword',
    database = 'first_database')

    return conne

def connection_close(conne):
    if conne:
        conne.close()

def delete_row(id):
    try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_select_query = '''SELECT * FROM LAPTOP where id = %s'''
        cursor.execute(mysql_select_query,(id,))
        record = cursor.fetchone()
        print(record)

        mysql_delete_query = '''DELETE FROM LAPTOP where id = %s'''
        cursor.execute(mysql_delete_query,(id,))
        conne.commit()
        print('Number of rows deleted',cursor.rowcount)

        cursor.execute(mysql_select_query,(id,))
        records = cursor.fetchall()
        if len(records) == 0:
            print('Record is deleted Succesfully')
        connection_close(conne)


    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)

delete_row(7)
delete_row(15)
