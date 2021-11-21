
import mysql.connector

# open connection
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "roottoor", database = "pythondb")

# create cursor
cur = conn.cursor()

try:
    # select records
    cur.execute("select * from Employee")
    # cur.execute("select name, id, salary from Employee")

    # fetch records
    records = cur.fetchall()
    # records = cur.fetchone()

    for record in records:
        print(record)

    print("------------------------------------------------")

    for record in records:
        print(str(record[0]) + " " + str(record[1]) + " " + str(record[2]))

    print("------------------------------------------------")

    # select records
    # cur.execute("select * from Employee")
    cur.execute("select name, id, salary from Employee")

    # fetch records
    # records = cur.fetchall()
    records = cur.fetchone()

    for record in records:
        print(record)

except:
    conn.rollback()

    print("Error!")

# close connection
conn.close()






























