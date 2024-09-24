import pandas as pd
import mysql.connector

# Kết nối tới cơ sở dữ liệu MySQL
mydb = mysql.connector.connect(
    host="localhost",      # Địa chỉ máy chủ MySQL, có thể thay đổi tùy theo môi trường của bạn
    user="sqluser",        # Tên người dùng MySQL
    password="password",   # Mật khẩu MySQL
    database="mydatabase"  # Tên cơ sở dữ liệu để chèn dữ liệu
)

# Tạo đối tượng con trỏ để tương tác với MySQL
cursor = mydb.cursor()

def insert2table():
    # Đọc tệp CSV bằng pandas
    df = pd.read_csv('data//csv//banana_quality.csv')

    # Tạo câu lệnh SQL INSERT để chèn từng hàng
    sql = "INSERT INTO banana (Size, Weight, Sweetness, Softness, HarvestTime, Ripeness, Acidity, Quality, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Chèn từng hàng dữ liệu từ dataframe vào MySQL
    for index, row in df.iterrows():
        cursor.execute(sql, tuple(row))

    # Xác nhận thay đổi
    mydb.commit()

    print(cursor.rowcount, "hàng đã được chèn thành công.")

insert2table()
# Đóng kết nối
cursor.close()
mydb.close()
