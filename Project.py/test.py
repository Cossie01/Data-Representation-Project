#checking if its connected. 
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password"
)

print(mydb)