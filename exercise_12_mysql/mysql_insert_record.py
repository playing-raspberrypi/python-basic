
import mysql.connector

# open connection
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "roottoor", database = "pythondb")

# create cursor
cur = conn.cursor()

try:
    query = "insert into Employee(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"
    record = ("John", 110, 25000.00, 201, "Newyork")
    records = [("David", 103, 25000.00, 201, "Port of spain"), ("Nick", 104, 90000.00, 201, "Newyork")]

    # insert record
    cur.execute(query, record)

    # insert records
    cur.executemany(query, records)

    # commit transaction
    conn.commit()

except:
    # rollback transaction
    conn.rollback()

    print("Error!")

# close connection
conn.close()






























