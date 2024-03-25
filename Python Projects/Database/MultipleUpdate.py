''''
Use a Python variable in MySQL Update query

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

def update_laptop_price(id,price):
    try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_update_price = '''UPDATE laptop set price =%s where id =%s'''
        input_data = (price,id)
        cursor.execute(mysql_update_price,input_data)
        conne.commit()
        print('The price',price,'has been updated successfully')
        connection_close(conne)

    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)

update_laptop_price(3,2499)
update_laptop_price(5,1499)



