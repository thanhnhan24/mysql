import mysql.connector
from PIL import Image
import os

# Hàm kết nối đến MySQL
def connect_to_mysql():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nhan2286301149",
    database="tieuluan"
    )

# Hàm chèn ảnh vào bảng 'images'
def insert_image(cursor, file_name, image_data, width, height):
    sql = """
        INSERT INTO images (filename, image_data, width, height) 
        VALUES (%s, %s, %s, %s)
    """
    val = (file_name, image_data, width, height)
    cursor.execute(sql, val)

# Hàm đọc và chèn toàn bộ dataset YOLOv8 vào MySQL
def import_dataset_to_mysql(dataset_path):
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Duyệt qua thư mục chứa dataset
    for file_name in os.listdir(dataset_path):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):  # Chỉ lấy file ảnh
            file_path = os.path.join(dataset_path, file_name)
            
            # Mở và xử lý file ảnh
            with open(file_path, 'rb') as file:
                binary_data = file.read()  # Đọc dữ liệu nhị phân của ảnh

            # Lấy kích thước của ảnh
            image = Image.open(file_path)
            width, height = image.size
            
            # Chèn dữ liệu ảnh vào MySQL
            insert_image(cursor, file_name, binary_data, width, height)
            print(f"Đã chèn {file_name} vào MySQL.")

    # Commit thay đổi và đóng kết nối
    conn.commit()
    cursor.close()
    conn.close()
    print("Hoàn thành việc import dataset vào MySQL.")

# Thư mục chứa dataset YOLOv8 (chứa các file ảnh)
dataset_path = "C://Users//Thanh Nhan//Desktop//train//images"

# Thực hiện import dataset
import_dataset_to_mysql(dataset_path)
