'''
Update doctor experience in years
The value of the experience column for each doctor is null. 
Implement the functionality to update the experience of a given doctor in years.

'''

import mysql.connector
from datetime import datetime

def database_connection():
    conne = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'hospital')
    return conne

def connection_close(conne,cursor):
    if conne:
        conne.close()
    if cursor:
            cursor.close()


def doctor_joining(doctor_id):
    try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_doctor_query = '''SELECT Joining_Date FROM DOCTOR where Doctor_id = %s'''
        cursor.execute(mysql_doctor_query,(doctor_id,))
        records = cursor.fetchone()
        print('Printing Current Doctor Details: ',records)
        connection_close(conne,cursor)
        return records

    except(Exception,mysql.connector.Error) as error:
        print('There is an error ',error)

def update_doctor_experience(doctor_id):
    try:
        joining_date = doctor_joining(doctor_id)
        conne = database_connection()
        cursor = conne.cursor()
        if joining_date:
            joining_date = joining_date[0]
            experience = (datetime.now().date() - joining_date).days/365
            mysql_doctor_query = """UPDATE doctor SET experience=%s where doctor_id = %s"""
            cursor.execute(mysql_doctor_query,(experience,doctor_id,))
            conne.commit()
            print('Experience has been updated')
        else:
            print("Joining date not found for the doctor.")
            connection_close(conne,cursor)

    except(Exception,mysql.connector.Error) as error:
        print('There is an error ',error)

update_doctor_experience(103)
update_doctor_experience(104)
update_doctor_experience(105)
update_doctor_experience(106)
update_doctor_experience(107)
update_doctor_experience(108)
