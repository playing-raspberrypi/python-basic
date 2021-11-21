
import mysql.connector

# open connection
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "roottoor")

# create cursor
cur = conn.cursor()

try:
    # create new database
    # cur.execute("create database pythondb")

    # drop database by name
    # cur.execute("drop database PythonDB2")

  	# get in cursor db list
    cur.execute("show databases")

except:
    # rollback transaction
    conn.rollback()

    print("Error!")

for x in cur:
	print(x)

# close connection
conn.close()

































