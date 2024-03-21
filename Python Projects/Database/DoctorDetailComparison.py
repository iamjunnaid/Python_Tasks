'''
Get the list Of doctors as per the given specialty and salary
Note: Fetch all doctors whose salary higher than the input amount and specialty is the same as the input specialty.

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


def get_specialist_doctors_list(speciality, salary):
    try:
        conne = database_connection()
        cursor = conne.cursor()
        mysql_doctor_query = '''SELECT * FROM DOCTOR where Speciality=%s and Salary > %s'''
        cursor.execute(mysql_doctor_query,(speciality,salary,))
        records = cursor.fetchall()
        print('Record is getting analyzed', records)
        print('Doctors whose speciality is',speciality,'and Salary is more than',salary )
        for row in records:
            print("Doctor Id: ", row[0])
            print("Doctor Name:", row[1])
            print("Hospital Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        connection_close(conne)

    except(Exception, mysql.connector.Error) as error:
        print('There is an Error',error)

print("Question 3: Get Doctors as per given Speciality\n")
get_specialist_doctors_list("Garnacologist", 30000)
