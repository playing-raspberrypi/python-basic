
import mysql.connector

# open connection
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "roottoor", database = "pythondb")

# create cursor
cur = conn.cursor()

try:
    # delete record
    cur.execute("update Employee set dept_id = 201 where id = 103")
    
    # commit transaction
    conn.commit()

except:
    conn.rollback()

    print("Error!")

# close connection
conn.close()






























