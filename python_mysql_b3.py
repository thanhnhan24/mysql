import mysql.connector
from datetime import date
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nhan2286301149",
    database="b3_kiemtra"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM raw_data")
myresult = mycursor.fetchall()



def fruit_id_converter():
    arr = []
    for x in myresult:
        if (x[1] in arr) == False:
            arr.append(x[1])
        else:
            pass
    for x in arr:
        # mycursor.execute(f"INSERT INTO fruit_id_table(fruit_id, fruit_name) VALUES ('{arr.index(x)+1}','{x}')")
        return arr
        mydb.commit()

def scientific_id_converter():
    arr = []
    for x in myresult:
        if (x[2] in arr) == False:
            arr.append(x[2])
        else:
            pass
    for x in arr:
        # mycursor.execute(f"INSERT INTO scientific_id_table(scientific_id, scientific_name) VALUES ({arr.index(x)+1},'{x}')")
        return arr
        mydb.commit()


def color_id_converter():
    arr = []
    for x in myresult:
        if (x[3] in arr) == False:
            arr.append(x[3])
        else:
            pass
    for x in arr:
        # mycursor.execute(f"INSERT INTO color_id_table(color_id, color_label) VALUES ({arr.index(x)+1},'{x}')")
        return arr
        mydb.commit()

def taste_id_converter():
    arr = []
    for x in myresult:
        if (x[4] in arr) == False:
            arr.append(x[4])
        else:
            pass
    for x in arr:
        # mycursor.execute(f"INSERT INTO taste_id_table(taste_id, taste_label) VALUES ({arr.index(x)+1},'{x}')")
        return arr
        mydb.commit()

def finale_submission():
    fname = fruit_id_converter()
    sname = scientific_id_converter()
    cname = color_id_converter()
    tname = taste_id_converter()
    for x in myresult:
        print(f"INSERT INTO finale(FID, fruit_id, scientific_id, color_id, taste_id) values ('{myresult.index(x)+1}','{fname.index(x[1])+1}','{sname.index(x[2])+1}','{cname.index(x[3])+1}','{tname.index(x[4])+1}');")
    print(mycursor.fetchall())
    mydb.commit

finale_submission()
mydb.close()