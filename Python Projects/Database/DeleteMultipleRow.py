'''
Delete Multiple Rows from a MySQL Table
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

def delete_row(id1,id2):
    try:
        #For id1
        conne = database_connection()
        cursor = conne.cursor()
        mysql_select_query1 = '''SELECT * FROM LAPTOP where id = %s'''
        cursor.execute(mysql_select_query1,(id1,))
        record1 = cursor.fetchone()
        print(record1)

        mysql_delete_query1 = '''DELETE FROM LAPTOP where id = %s'''
        cursor.execute(mysql_delete_query1,(id1,))
        conne.commit()
        print('Number of rows deleted',cursor.rowcount)

        cursor.execute(mysql_select_query1,(id1,))
        records1 = cursor.fetchall()
        if len(records1) == 0:
            print('Record is deleted Succesfully')
        

        #For id2
        mysql_select_query2 = '''SELECT * FROM LAPTOP where id = %s'''
        cursor.execute(mysql_select_query2,(id2,))
        record2 = cursor.fetchone()
        print(record2)

        mysql_delete_query2 = '''DELETE FROM LAPTOP where id = %s'''
        cursor.execute(mysql_delete_query2,(id2,))
        conne.commit()
        print('Number of rows deleted',cursor.rowcount)

        cursor.execute(mysql_select_query2,(id2,))
        records2 = cursor.fetchall()
        if len(records2) == 0:
            print('Record is deleted Succesfully')
        connection_close(conne)


    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)

delete_row(9,10)
