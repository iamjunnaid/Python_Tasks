'''
Fetch Hospital and Doctor Information using hospital Id and doctor Id
Implement the functionality to read the details of a given doctor from the doctor table and Hospital from the hospital table. i.e., 
read records from Hospital and Doctor Table as per given hospital Id and Doctor Id.

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

def get_hospital_detail(hospital_id):
    try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_hospital_query = """SELECT * FROM hospital where Hospital_id = %s"""
        cursor.execute(mysql_hospital_query,(hospital_id,))
        records = cursor.fetchall()
        print('Printing Hospital Records')
        for row in records:
            print('Hospital Id:',row[0])
            print('Hospital Name:',row[1])
            print('Bed Count:',row[2])
        connection_close(conne)

    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)


def get_doctor_detail(doctor_id):
    try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_doctor_query = """SELECT * FROM doctor where Doctor_id = %s"""
        cursor.execute(mysql_doctor_query,(doctor_id,))
        records = cursor.fetchall()
        print('Printing Doctor Records')
        for row in records:
            print('Doctor Id:',row[0])
            print('Doctor Name:',row[1])
            print('Hospital Id:',row[2])
            print('Joining Date:',row[3])
            print('Speciality:',row[4])
            print('Salary: ',row[5])
        connection_close(conne)

    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)


get_hospital_detail(4)
get_doctor_detail(105)