import mysql.connector

conne = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Sqlpassword',
    database = 'first_database'
)

mysql_insert_query = """INSERT INTO LAPTOP(
                Id, Name, Price, Purchase_date) VALUES
                (15, 'Lenovo Thinkpad',1500,'2024-03-14')"""

curs = conne.cursor()
exec = curs.execute(mysql_insert_query)
conne.commit()
print(curs.rowcount,"Record Successfully inserted")

