










import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Sachin12",database="boy")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE details (name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255), gender VARCHAR(255))")
sql = "INSERT INTO details (name, age, email, password, gender) VALUES(%s, %s, %s, %s, %s)"
val = [("John", 23, "varunrajput202@gmail.com", "sakshi", "male"),
       ("ankit", 24, "rinkurajput202@gmail.com", "sonam", "male"),]
mycursor.executemany(sql, val)
mydb.commit()





'''
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Sachin12",database="boy")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE sams (name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255), gender VARCHAR(255))")
sql = "INSERT INTO sams (name, age, email, password, gender) VALUES (%s, %s, %s, %s, %s)"
val = ("John", "23", "varunrajput202@gmail.com", "Sakshi", "Male")
mycursor.execute(sql, val)
mydb.commit()

'''




'''
import mysql.connector
name = input('Enter the name :')
age = int(input('Enter the age :'))
email = input('Enter the email :')
password = input('Enter the password :')
gender = input('Enter the gender :')
mydb = mysql.connector.connect(host="localhost",user="root",password="Sachin12",database="dm")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255), gender VARCHAR(255))")
mycursor.execute("INSERT INTO students values('"+ name +"','"+ str(age) +"','"+ str(email) +"','"+ password +"','"+ gender +"')")
mydb.commit()
mydb.close()
'''

