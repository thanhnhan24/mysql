import mysql.connector

# Hàm kết nối đến MySQL
def connect_to_mysql():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nhan2286301149",
    database="tieuluan"
    )

# Hàm chèn nhãn (label) vào bảng labels
def insert_label(label, student_name):
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Kiểm tra xem nhãn đã tồn tại trong bảng hay chưa
    check_sql = "SELECT id FROM labels WHERE label = %s AND student_name = %s"
    cursor.execute(check_sql, (label, student_name))
    result = cursor.fetchone()

    if result:
        print(f"Nhãn '{label}' với tên sinh viên '{student_name}' đã tồn tại.")
    else:
        # Nếu nhãn chưa tồn tại, thêm mới
        insert_sql = "INSERT INTO labels (label, student_name) VALUES (%s, %s)"
        cursor.execute(insert_sql, (label, student_name))
        conn.commit()  # Lưu thay đổi
        print(f"Đã chèn nhãn '{label}' với tên sinh viên '{student_name}' vào bảng.")

    cursor.close()
    conn.close()

# Sử dụng hàm để chèn nhãn vào bảng
label = ['bachtuong', 'huynhtho', 'khanhvy', 'ngocphu', 'nhuquan', 'pntt', 'pvy', 'thanhnhu']  # Ví dụ nhãn
student_name = ['bach tuong', 'huynh tho', 'khan vy', 'ngoc phu', 'nhu quan', 'phan ngo tuan tu', 'phuong vy', 'thanh nhu']  # Tên sinh viên

for x, y in zip(label, student_name):
    insert_label(x, y)