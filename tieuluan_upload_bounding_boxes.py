import mysql.connector
import os

# Hàm kết nối đến MySQL
def connect_to_mysql():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nhan2286301149",
    database="tieuluan"
    )

# Hàm lấy ID của nhãn từ bảng labels dựa vào tên nhãn
def get_label_id(cursor, label_name):
    cursor.execute("SELECT id FROM labels WHERE label = %s", (label_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        # Nếu nhãn chưa tồn tại, thêm nhãn mới
        cursor.execute("INSERT INTO labels (label) VALUES (%s)", (label_name,))
        return cursor.lastrowid

# Hàm lấy ID của ảnh từ bảng images dựa vào tên file
def get_image_id(cursor, file_name):
    cursor.execute("SELECT id FROM images WHERE filename = %s", (file_name,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

# Hàm chèn bounding box vào bảng bounding_boxes
def insert_bounding_box(cursor, image_id, label_id, x_center, y_center, width, height):
    sql = """
        INSERT INTO bounding_boxes (image_id, label_id, x_center, y_center, width, height)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    val = (image_id, label_id, x_center, y_center, width, height)
    cursor.execute(sql, val)

# Hàm đọc và chèn dữ liệu bounding boxes từ file YOLO vào MySQL
def import_bounding_boxes(dataset_path, labels_map):
    conn = connect_to_mysql()
    cursor = conn.cursor()

    # Duyệt qua thư mục chứa các file nhãn YOLO
    for file_name in os.listdir(dataset_path):
        if file_name.endswith(".txt"):  # Chỉ lấy file .txt (YOLO format)
            image_name = file_name.replace(".txt", ".jpg")  # Giả sử ảnh có cùng tên với file nhãn .txt
            image_id = get_image_id(cursor, image_name)

            if image_id is None:
                print(f"Không tìm thấy ảnh tương ứng với file nhãn: {file_name}")
                continue

            # Đọc file nhãn
            file_path = os.path.join(dataset_path, file_name)
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()  # Mỗi dòng là: <class_id> <x_center> <y_center> <width> <height>
                    if len(parts) != 5:
                        continue  # Bỏ qua nếu format không đúng

                    class_id = int(parts[0])
                    x_center = float(parts[1])
                    y_center = float(parts[2])
                    width = float(parts[3])
                    height = float(parts[4])

                    # Lấy tên nhãn từ class_id (sử dụng labels_map đã được cung cấp)
                    if class_id in labels_map:
                        label_name = labels_map[class_id]
                        label_id = get_label_id(cursor, label_name)
                        
                        # Chèn bounding box vào MySQL
                        insert_bounding_box(cursor, image_id, label_id, x_center, y_center, width, height)
                        print(f"Đã chèn bounding box cho ảnh {image_name} với nhãn {label_name}.")
                    else:
                        print(f"Không tìm thấy nhãn cho class_id: {class_id}")

    # Commit thay đổi và đóng kết nối
    conn.commit()
    cursor.close()
    conn.close()
    print("Hoàn thành việc import bounding boxes vào MySQL.")

# Bản đồ giữa class_id và tên nhãn (labels_map)
# Bạn cần thay thế labels_map này dựa trên dataset YOLOv8 của bạn
labels_map = {
    0:'bachtuong',
    1:'huynhtho',
    2:'khanhvy',
    3:'ngocphu',
    4:'nhuquan',
    5:'pntt',
    6:'pvy',
    7:'thanhnhu'
    # Thêm các nhãn khác nếu cần
}

# Thư mục chứa file nhãn YOLO (chứa các file .txt)
dataset_path = "C://Users//Thanh Nhan//Desktop//train//labels"

# Thực hiện import bounding boxes
import_bounding_boxes(dataset_path, labels_map)
