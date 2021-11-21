
import mysql.connector

# open connection
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "roottoor", database = "pythondb")

# create cursor
cur = conn.cursor()

try:
    # create new table
    cur.execute("create table Employee(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")
    
    # alter table
    cur.execute("alter table Employee add branch_name varchar(20) not null")

except:
    # rollback transaction
    conn.rollback()

    print("Error!")

# close connection
conn.close()










































