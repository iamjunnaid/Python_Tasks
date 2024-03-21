'''
Get a list of doctors from a given hospital
Note: Implement the functionality to fetch all the doctors as per the given Hospital Id. You must display the hospital name of a 
doctor.

Hint:

Define the parameterized select query to get the hospital name as per the given hospital id.
Next, use the cursor.execute() to execute this query and store the hospital name in a variable.
Define the parameterized select query to fetch all doctors from the doctor table as per the given hospital id.
Next, use the cursor.execute() to execute the query.
Next, get all records using cursor.fetchall()
Iterate those records and print each column. Also, display the hospital name we fetched in the first query in each doctor's entry

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

def hospital_name(hospital_id):
    try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_hospital_query = """SELECT * FROM hospital where Hospital_id = %s"""
        cursor.execute(mysql_hospital_query,(hospital_id,))
        records = cursor.fetchone()
        print('Printing Hospital Records:',records)
        connection_close(conne)
        return records[1]

    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)

def get_doctors(hospital_id):
    try:
        hospital_na = hospital_name(hospital_id)
        conne = database_connection()
        cursor = conne.cursor()
        mysql_doctor_query = """SELECT * FROM doctor where hospital_id = %s"""
        cursor.execute(mysql_doctor_query,(hospital_id,))
        records = cursor.fetchall()
        print('Printing Doctors who works in',hospital_na)
        for row in records:
            print('Doctor Id:',row[0])
            print('Doctor Name:',row[1])
            print('Hospital Id:',row[2])
            print('Hospital Name:',hospital_na)
            print('Joining Date:',row[3])
            print('Speciality:',row[4])
            print('Salary: ',row[5])
            print("Experience:", row[6], "\n")
        connection_close(conne)

    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)


print("Question 4:  Get List of doctors of a given Hospital Id\n")
get_doctors(2)