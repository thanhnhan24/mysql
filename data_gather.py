import mysql.connector
from datetime import datetime, date
def get_data_by_id(db_config, table_name, record_id):
    try:
        # Kết nối đến cơ sở dữ liệu
        connection = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )

        cursor = connection.cursor()

        # Truy vấn dữ liệu theo id
        query = f"SELECT * FROM {table_name} WHERE id = %s"
        cursor.execute(query, (record_id,))

        # Lấy kết quả
        result = cursor.fetchone()
        
        # Kiểm tra và in kết quả
        if result:
            date_str = str(result[4]).replace('atetime.date(','').replace(')','').split(',')
            form = f"""
                ID          : {result[-1]}
                Size        : {result[0]}
                Weight      : {result[1]}
                Sweetness   : {result[2]}
                Softness    : {result[3]}
                HarvestTime : {date_str}
                Ripeness    : {result[5]}
                Acidity     : {result[6]}
                Quality     : {result[7]}
"""
            print(form)
        else:
            print(f"Không tìm thấy bản ghi với id = {record_id}")

    except mysql.connector.Error as err:
        print(f"Lỗi: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Cấu hình kết nối cơ sở dữ liệu
db_config = {
    'host':"localhost",      # Địa chỉ máy chủ MySQL, có thể thay đổi tùy theo môi trường của bạn
    'user':"sqluser",        # Tên người dùng MySQL
    'password':"password",   # Mật khẩu MySQL
    'database':"mydatabase"  # Tên cơ sở dữ liệu để chèn dữ liệu
}

# Gọi hàm để truy xuất dữ liệu theo id
get_data_by_id(db_config, 'banana', 1)
