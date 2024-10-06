import mysql.connector
from datetime import date
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nhan2286301149",
    database="buoi3"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM robot_maintain")
myresult = mycursor.fetchall()

for x in myresult:
    arr = x[2].split(',')
    for y in arr:
        if y.find('/') == -1 :
            mycursor2 = mydb.cursor()
            local = y.split('-')
            dout = date(int(local[0]),int(local[1]), int(local[2]))
            mycursor2.execute(f"insert into robot_maintain_after(rbot_id, rbot_name, maintain_date) values ('{x[0]}','{x[1]}','{dout}')")
        else:
            local = y.split('/')
            dout = date(int(local[2]),int(local[1]), int(local[0]))
            mycursor2.execute(f"insert into robot_maintain_after(rbot_id, rbot_name, maintain_date) values ('{x[0]}','{x[1]}','{dout}')")

mydb.commit()
mydb.close()

