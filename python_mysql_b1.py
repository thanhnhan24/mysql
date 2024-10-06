import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nhan2286301149",
    database="buoi3"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM robot")
myresult = mycursor.fetchall()


for x in myresult:
    local_task = x[2].split(',')
    for y in local_task:
        y = y.strip()
        mycursor2 = mydb.cursor()
        mycursor2.execute(f"INSERT INTO robot_after(rbot_id, rbot_name, task) VALUES ('{x[0]}','{x[1]}','{y}')")
        mycursor2.fetchall()
        print(mycursor2)
    

mydb.commit()
mydb.close()