'''
Create, manage and use a Connection pool with MySQL

'''

from mysql.connector import pooling
try:
    conne_pooling = pooling.MySQLConnectionPool(
        pool_name='hospital_pool',
        pool_size= 5,
        pool_reset_session=True,
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'hospital')
    
    print('Printing Pool Properties:')
    print('Pool name is: ',conne_pooling.pool_name)
    print('Pool size is: ',conne_pooling.pool_size)

    conne_object = conne_pooling.get_connection()
    if conne_object.is_connected():
        db_information: conne_object.get_server_info()
        cursor = conne_object.cursor()
        cursor.execute('select database();')
        record = cursor.fetchone()
        print('You are connected to - ',record)


except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)

finally:
    # closing database connection.
    if conne_object.is_connected():
        cursor.close()
        conne_object.close()
        print("MySQL connection is closed")