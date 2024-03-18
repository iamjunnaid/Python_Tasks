'''
Create Hospital Table and Doctor Table
'''

import mysql.connector
try:

    conne = mysql.connector.connect(
        host = 'localhost',
        username = 'root',
        password = 'Sqlpassword',
        database = 'hospital'
    )
    cursor = conne.cursor()
    mysql_Create_Hospital_Table = """CREATE TABLE Hospital(
                        Hospital_Id INT UNSIGNED NOT NULL, 
                        Hospital_Name TEXT NOT NULL, 
                        Bed_Count INT, 
                        PRIMARY KEY (Hospital_Id))"""
    mysql_Create_Doctor_Table = """CREATE TABLE Doctor(
                        Doctor_Id INT UNSIGNED NOT NULL,
                        Doctor_Name TEXT NOT NULL, 
                        Hospital_Id INT NOT NULL, 
                        Joining_Date DATE NOT NULL, 
                        Speciality TEXT NULL, 
                        Salary INT NULL, 
                        Experience INT NULL, 
                        PRIMARY KEY (Doctor_Id))"""

    mysql_insert_hospital_query = '''INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) VALUES (%s, %s, %s)'''
    record_hospital =[(1, 'Mayo Clinic', 200),
                    (2, 'Cleveland Clinic', 400), 
                    (3, 'Johns Hopkins', 1000), 
                    (4, 'UCLA Medical Center', 1500)]

    mysql_insert_doctor_query = '''INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s,%s, %s, %s)'''
    record_doctor = [(101, 'David', 1, '2005-2-10', 'Pediatric', 40000, None), 
                    (102, 'Michael', 1, '2018-07-23', 'Oncologist', 20000, None), 
                    (103, 'Susan', 2, '2016-05-19', 'Garnacologist', 25000, None), 
                    (104, 'Robert', 2, '2017-12-28', 'Pediatric ', 28000, None), 
                    (105, 'Linda', 3, '2004-06-04', 'Garnacologist', 42000, None), 
                    (106, 'William', 3, '2012-09-11', 'Dermatologist', 30000, None), 
                    (107, 'Richard', 4, '2014-08-21', 'Garnacologist', 32000, None), 
                    (108, 'Karen', 4, '2011-10-17', 'Radiologist', 30000, None)]


    exec_table_hospital = cursor.execute(mysql_Create_Hospital_Table)
    exec_table_doctor = cursor.execute(mysql_Create_Doctor_Table)
    exec = cursor.executemany(mysql_insert_hospital_query,record_hospital)
    exec_doctor = cursor.executemany(mysql_insert_doctor_query,record_doctor)
    conne.commit()
    print(cursor.rowcount,'Record Inserted Successfully')

except mysql.connector.Error as error:
        print('Record failed to insert into Table {}'.format(error))

finally:
        if conne.is_connected():
            cursor.close()
            conne.close()
            print('MySQL is closed')