'''
Create Employee Information Table
'''

import mysql.connector
try:

    conne = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Sqlpassword',
    database = 'employee')

    mysql_Create_Table = """CREATE TABLE Information(
                    Id int(11) NOT NULL,
                    Name varchar(250) NOT NULL,
                    Photo BLOB NOT NULL,
                    Bio_DATA BLOB NOT NULL,
                    PRIMARY KEY(Id))"""

    cursor = conne.cursor()
    exec = cursor.execute(mysql_Create_Table)
    print(' Information Table Created Successfully')

except mysql.connector.Error as error:
        print('Information Table failed to created {}'.format(error))

finally:
        if conne.is_connected():
            cursor.close()
            conne.close()
            print('MySQL is closed')