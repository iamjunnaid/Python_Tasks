'''
Insert Image and File as a BLOB data into MySQL Table

'''

import mysql.connector

def database_connection():
    conne = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'employee')
    return conne

def connection_close(conne,cursor):
    if conne:
        conne.close()
    if cursor:
            cursor.close()

def Convert2Binary(filename):
     with open(filename, 'rb') as file:
          binaryData = file.read()
          return binaryData
     
def insert_Blob(id, name, photo, biodatafile):
     try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_infor_query = '''Insert into information (id, name, photo, bio_data) VALUES (%s,%s,%s,%s)'''
        employee_photo = Convert2Binary(photo)
        employee_biodata = Convert2Binary(biodatafile)
        record = (id, name, employee_photo,employee_biodata)
        cursor.execute(mysql_infor_query,record)
        cursor.commit()
        print('Updated the Information: ')
        connection_close(conne,cursor)
          
     except(Exception,mysql.connector.Error) as error:
        print('There is an error ',error)


insert_Blob(1, "Eric", "D:\Coding\Python Projects\Database\Eric_Photo.jpg",
           "D:\Coding\Python Projects\Database\eric_biodata.txt")
          