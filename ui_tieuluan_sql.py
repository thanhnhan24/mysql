# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tieuluan_sqlIXQHQG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import mysql.connector, sys, os, io
from PIL import Image, ImageQt
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import threading


class Ui_MainWindow(object):
    def __init__(self):
        self.log = []
        self.connection = None
        self.current_id = None
        self.processed_files = set()
        self.model1 = None
        self.model2 = None
        self.label_id = None
        self.img_height = None
        self.img_width = None
        self.x_center = None
        self.y_center = None
        self.box_width = None
        self.box_height = None
        pass
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 890)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 961, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 111))
        self.label_2.setPixmap(QPixmap(u"C://Users//Thanh Nhan//Pictures//Logo_Trường_Đại_học_Công_nghệ_Thành_phố_Hồ_Chí_Minh.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 50, 961, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 90, 961, 41))
        self.label_4.setFont(font1)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(810, 130, 281, 241))
        font2 = QFont()
        font2.setPointSize(10)
        self.groupBox.setFont(font2)
        self.mysql_host = QTextEdit(self.groupBox)
        self.mysql_host.setObjectName(u"mysql_host")
        self.mysql_host.setGeometry(QRect(10, 30, 261, 31))
        self.mysql_user = QTextEdit(self.groupBox)
        self.mysql_user.setObjectName(u"mysql_user")
        self.mysql_user.setGeometry(QRect(10, 70, 261, 31))
        self.mysql_password = QTextEdit(self.groupBox)
        self.mysql_password.setObjectName(u"mysql_password")
        self.mysql_password.setGeometry(QRect(10, 110, 261, 31))
        self.myql_database = QTextEdit(self.groupBox)
        self.myql_database.setObjectName(u"myql_database")
        self.myql_database.setGeometry(QRect(10, 150, 261, 31))
        self.mysql_config_btn = QPushButton(self.groupBox)
        self.mysql_config_btn.setObjectName(u"mysql_config_btn")
        self.mysql_config_btn.setGeometry(QRect(10, 190, 261, 41))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(30, 600, 1061, 231))
        self.groupBox_2.setFont(font2)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 361, 151))
        self.input_terminal = QPlainTextEdit(self.groupBox_2)
        self.input_terminal.setObjectName(u"input_terminal")
        self.input_terminal.setGeometry(QRect(390, 20, 531, 191))
        self.tracking = QPushButton(self.groupBox_2)
        self.tracking.setObjectName(u"tracking")
        self.tracking.setGeometry(QRect(930, 20, 121, 41))
        self.detect = QPushButton(self.groupBox_2)
        self.detect.setObjectName(u"detect")
        self.detect.setGeometry(QRect(930, 70, 121, 41))
        self.add2db = QPushButton(self.groupBox_2)
        self.add2db.setObjectName(u"add2db")
        self.add2db.setGeometry(QRect(930, 120, 121, 41))
        self.rm2db = QPushButton(self.groupBox_2)
        self.rm2db.setObjectName(u"rm2db")
        self.rm2db.setGeometry(QRect(930, 170, 121, 41))
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 140, 801, 461))
        self.terminal_tab = QWidget()
        self.terminal_tab.setObjectName(u"terminal_tab")
        self.output_terminal = QListView(self.terminal_tab)
        self.output_terminal.setObjectName(u"output_terminal")
        self.output_terminal.setGeometry(QRect(10, 10, 781, 421))
        self.tabWidget.addTab(self.terminal_tab, "")
        self.img_tab = QWidget()
        self.img_tab.setObjectName(u"img_tab")
        self.img_output = QLabel(self.img_tab)
        self.img_output.setObjectName(u"img_output")
        self.img_output.setGeometry(QRect(10, 0, 471, 421))
        self.img_data = QListView(self.img_tab)
        self.img_data.setObjectName(u"img_data")
        self.img_data.setGeometry(QRect(490, 0, 301, 421))
        self.tabWidget.addTab(self.img_tab, "")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(810, 380, 281, 181))
        self.groupBox_3.setFont(font2)
        self.model_n = QRadioButton(self.groupBox_3)
        self.model_n.setObjectName(u"model_n")
        self.model_n.setGeometry(QRect(10, 30, 261, 20))
        self.model_s = QRadioButton(self.groupBox_3)
        self.model_s.setObjectName(u"model_s")
        self.model_s.setGeometry(QRect(10, 60, 261, 20))
        self.model_x = QRadioButton(self.groupBox_3)
        self.model_x.setObjectName(u"model_x")
        self.model_x.setGeometry(QRect(10, 90, 261, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1109, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00ea t\u00e0i ti\u1ec3u lu\u1eadn: H\u1ec7 c\u01a1 s\u1edf d\u1eef li\u1ec7u qu\u1ea3n l\u00ed d\u1eef li\u1ec7u khu\u00f4n m\u1eb7t h\u1ecdc sinh", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sinh vi\u00ean: Nguy\u1ec5n Thanh Nh\u00e2n       MSSV: 2286301149       Chuy\u00ean ng\u00e0nh: Robot v\u00e0 Tr\u00ed tu\u1ec7 nh\u00e2n t\u1ea1o", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"M\u00f4n h\u1ecdc: C\u01a1 s\u1edf d\u1eef li\u1ec7u trong AI v\u00e0 Robot", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"C\u1ea5u h\u00ecnh CSDL", None))
        self.mysql_host.setPlaceholderText(QCoreApplication.translate("MainWindow", u"host", None))
        self.mysql_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"user", None))
        self.mysql_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.myql_database.setPlaceholderText(QCoreApplication.translate("MainWindow", u"database", None))
        self.mysql_config_btn.setText(QCoreApplication.translate("MainWindow", u"N\u1ea1p c\u1ea5u h\u00ecnh", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Thao t\u00e1c tr\u00ean d\u1eef li\u1ec7u h\u00ecnh \u1ea3nh", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Truy xu\u1ea5t \u0111\u01a1n: id1\n"
"Truy xu\u1ea5t h\u00e0ng lo\u1ea1t: id1:id2\n"
"Chu\u1ea9n \u0111o\u00e1n \u0111\u01a1n: <path.jpg/png>\n"
"Chu\u1ea9n \u0111o\u00e1n h\u00e0ng lo\u1ea1t: <path to dir>\n"
"Th\u00eam d\u1eef li\u1ec7u sau chu\u1ea9n \u0111o\u00e1n: <path.png/jpg>\n"
"X\u00f3a d\u1eef li\u1ec7u: id1", None))
        self.tracking.setText(QCoreApplication.translate("MainWindow", u"Truy xu\u1ea5t", None))
        self.detect.setText(QCoreApplication.translate("MainWindow", u"Chu\u1ea9n \u0111o\u00e1n", None))
        self.add2db.setText(QCoreApplication.translate("MainWindow", u"Th\u00eam", None))
        self.rm2db.setText(QCoreApplication.translate("MainWindow", u"X\u00f3a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.terminal_tab), QCoreApplication.translate("MainWindow", u"terminal output", None))
        self.img_output.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.img_tab), QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"C\u1ea5u h\u00ecnh m\u00f4 h\u00ecnh", None))
        self.model_n.setText(QCoreApplication.translate("MainWindow", u"YOLOv8n", None))
        self.model_s.setText(QCoreApplication.translate("MainWindow", u"YOLOv8s", None))
        self.model_x.setText(QCoreApplication.translate("MainWindow", u"YOLOv8x", None))
    # retranslateUi

        self.mysql_config_btn.clicked.connect(self.connect_to_db)
        self.tracking.clicked.connect(self.get_input)
        self.detect.clicked.connect(self.get_input)
        self.output_terminal.clicked.connect(self.choose_img)
        self.add2db.clicked.connect(self.add_process)
        self.rm2db.clicked.connect(self.delete)

    def connect_to_db(self):
        host = self.mysql_host.toPlainText()
        if host == "":
            host = 'localhost'
            self.mysql_host.setPlainText(host)
        user = self.mysql_user.toPlainText()
        if user == "":
            user = 'root'
            self.mysql_user.setPlainText(user)
        password = self.mysql_password.toPlainText()
        if password == "":
            password = 'Nhan2286301149'
            self.mysql_password.setPlainText('**************')
        database = self.myql_database.toPlainText()
        if database == '':
            database = 'tieuluan'
            self.myql_database.setPlainText(database)
            

        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if connection.is_connected():
                self.display_message("Kết nối thành công!")
                self.connection = connection
        except mysql.connector.Error as err:
            self.display_message(f"Lỗi kết nối: {err}")
        except ValueError:
            self.display_message("Vui lòng nhập dữ liệu")
        
    def display_message(self, message):
        self.model1 = QStringListModel()
        self.log.append(message)
        self.model1.setStringList(self.log)
        self.output_terminal.setModel(self.model1)

    def display_info(self, img_width, img_height, bounding_boxes):
        conn = self.connection
        cursor = conn.cursor()
        info_list = []
        # Thêm thông tin chiều rộng và chiều cao vào danh sách
        info_list.append(f"Width: {img_width}")
        info_list.append(f"Height: {img_height}")

        # Thêm thông tin của từng bounding box vào danh sách
        if bounding_boxes:
            info_list.append("\nBounding Boxes:\n")
            for box in bounding_boxes:
                x_center, y_center, box_width, box_height, label = box
                cursor.execute("SELECT * FROM labels WHERE label = %s", (label,))
                data = cursor.fetchone()
                id, label, student_name = data
                info_list.append(f"Label: {label},\nStudent name: {student_name},\nCenter: ({x_center}, {y_center}),\nWidth: {box_width},\nHeight: {box_height}")

        # Cập nhật vào QListView
        self.model2 = QStringListModel()
        self.model2.setStringList(info_list)
        self.img_data.setModel(self.model2)

    def get_input(self):
        raw = self.input_terminal.toPlainText()
        raw = raw.replace('"','')
        if not os.path.exists(raw):
            if raw.isnumeric():
                self.display_message(f"You enter single id: {raw}")
                try:
                    image_data, img_width, img_height, bounding_boxes = self.get_image_and_boxes(int(raw))
                    if image_data is None or bounding_boxes is None:
                        self.display_message("Không tìm thấy dữ liệu hình ảnh hoặc bounding boxes.")
                        return

                    # Hiển thị thông tin hình ảnh
                    self.display_info(img_width, img_height, bounding_boxes)

                    qt_image = self.display_image_with_boxes(image_data, img_width, img_height, bounding_boxes)
                    if qt_image is not None:
                        pixmap = QPixmap.fromImage(qt_image)
                        self.img_output.setPixmap(pixmap)
                except Exception as e:
                    self.display_message(f"Đã xảy ra lỗi khi lấy dữ liệu hình ảnh: {str(e)}")
            else:
                try:
                    # Xử lý trường hợp nhập nhiều ID
                    raw = raw.split(':')
                    id_start = int(raw[0])
                    id_end = int(raw[1])
                    self.display_message(f"You enter multiple id from {id_start} to {id_end}")

                    # Thiết lập current_id lần đầu tiên
                    if self.current_id is None:
                        self.current_id = id_start  # Thiết lập ID bắt đầu

                    # Kiểm tra nếu current_id vượt quá id_end
                    if self.current_id > id_end:
                        self.display_message("Đã truy xuất hết các ID.")
                        self.current_id = None  # Đặt lại current_id
                        return
                    
                    try:
                        image_data, img_width, img_height, bounding_boxes = self.get_image_and_boxes(self.current_id)
                        if image_data is None or bounding_boxes is None:
                            self.display_message("Không tìm thấy dữ liệu hình ảnh hoặc bounding boxes.")
                            return

                        # Hiển thị thông tin hình ảnh
                        self.display_info(img_width, img_height, bounding_boxes)

                        qt_image = self.display_image_with_boxes(image_data, img_width, img_height, bounding_boxes)
                        if qt_image is not None:
                            pixmap = QPixmap.fromImage(qt_image)
                            self.img_output.setPixmap(pixmap)
                    except Exception as e:
                        self.display_message(f"Đã xảy ra lỗi khi lấy dữ liệu hình ảnh: {str(e)}")
                    self.current_id += 1  # Tăng current_id lên 1
                except ValueError:
                    self.display_message("Sai định dạng dữ liệu")
        elif os.path.isdir(raw):
            self.display_message('You enter directory')
            self.tabWidget.setCurrentIndex(0)
            for file in os.listdir(raw):
                file_path = os.path.join(raw, file)
                if file_path not in self.processed_files:
                    try:
                        self.detect_task(file_path)
                        self.processed_files.add(file_path)
                        self.display_message(f"Tiến hành chuẩn đoán\nFile: {file_path}\n")
                    except Exception as e:
                        self.display_message(f"Lỗi khi chuẩn đoán hàng loạt: {e}")
            self.display_message("Kết thúc chuẩn đoán hàng loạt")
        elif os.path.isfile(raw):
            _, extension = os.path.splitext(raw)
            img_extension = ['.jpg','.png','.jpeg','.bmp']
            if extension.lower() in img_extension:
                self.display_message('You enter an image')
                self.detect_task(raw)
            else:
                self.display_message('Invalid extension')

    def get_image_and_boxes(self, image_id):
        conn = self.connection
        cursor = conn.cursor()

        try:
            # Truy vấn ảnh từ bảng images
            cursor.execute("SELECT image_data, width, height FROM images WHERE id = %s", (image_id,))
            image_result = cursor.fetchone()

            if image_result:
                image_data, img_width, img_height = image_result

                # Kiểm tra kích thước của image_data
                if image_data is None or len(image_data) == 0:
                    self.display_message("Dữ liệu hình ảnh không hợp lệ.")
                    return None, None, None

                # Truy vấn bounding boxes từ bảng bounding_boxes
                cursor.execute("""SELECT b.x_center, b.y_center, b.width, b.height, l.label 
                                FROM bounding_boxes b 
                                JOIN labels l ON b.label_id = l.id
                                WHERE b.image_id = %s""", (image_id,))
                bounding_boxes = cursor.fetchall()
            else:
                self.display_message(f"Không tìm thấy ảnh với image_id: {image_id}")
                return None, None, None
        except Exception as e:
            self.display_message(f"Lỗi truy vấn cơ sở dữ liệu: {str(e)}")
            return None, None, None
        finally:
            cursor.close()

        return image_data, img_width, img_height, bounding_boxes

    def display_image_with_boxes(self, image_data, img_width, img_height, bounding_boxes):
        try:
            # Chuyển dữ liệu ảnh nhị phân thành đối tượng ảnh
            image = Image.open(io.BytesIO(image_data))
        except Exception as e:
            self.display_message(f"Lỗi khi mở hình ảnh: {str(e)}")
            return None

        # Tạo figure và axes để vẽ bounding boxes
        fig, ax = plt.subplots(1)
        ax.imshow(image)

        # Duyệt qua các bounding box và vẽ lên ảnh
        for box in bounding_boxes:
            x_center, y_center, box_width, box_height, label = box

            # Chuyển đổi từ YOLO format sang tọa độ ảnh gốc
            x_min = (x_center - box_width / 2) * img_width
            y_min = (y_center - box_height / 2) * img_height
            box_width_px = box_width * img_width
            box_height_px = box_height * img_height

            # Vẽ hình chữ nhật bounding box
            rect = patches.Rectangle((x_min, y_min), box_width_px, box_height_px, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            # Vẽ nhãn (label) tại góc trên bên trái bounding box
            plt.text(x_min, y_min - 10, label, color='white', fontsize=12, bbox=dict(facecolor='red', alpha=0.5))

        # Ẩn trục
        plt.axis('off')

        # Lưu ảnh vào buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
        plt.close(fig)
        buf.seek(0)

        # Chuyển đổi buffer sang QImage
        qimage = QImage()
        qimage.loadFromData(buf.getvalue())

        return qimage
    
    def model_init(self):
        model_path = ""
        if self.model_n.isChecked():
            model_path = "F://Code//Python//YOLO_SFT24//model//model_n8//content//runs//detect//train//weights//best.pt"
        elif self.model_s.isChecked():
            model_path = "F://Code//Python//YOLO_SFT24//model//models//content//runs//detect//train//weights//best.pt"
        elif self.model_x.isChecked(): 
            model_path = "F://Code//Python//YOLO_SFT24//model//modelx//content//runs//detect//train2//weights//best.pt"
        try:
            model = YOLO(model_path)
            return model
        except SyntaxError:
            self.display_message("Lỗi trong khi khởi tạo model")


    def detect_task(self, path):
        # Tạo một thread để thực hiện quá trình phát hiện
        thread = threading.Thread(target=self.process_image, args=(path,))
        thread.start()  # Bắt đầu thread

    def process_image(self, path):
        img = cv2.imread(path)
        model = self.model_init()
        results = model(img)

        # Lấy kích thước ảnh
        self.img_height, self.img_width, _ = img.shape

        # Danh sách lưu trữ bounding boxes dưới dạng YOLO format
        bounding_boxes = []

        for result in results[0].boxes:
            # Tọa độ góc trên trái (x1, y1) và góc dưới phải (x2, y2)
            x1, y1, x2, y2 = result.xyxy[0]

            # Nhãn (label) của đối tượng
            self.label_id = int(result.cls[0])  # Lấy id của nhãn (class)
            label_name = model.names[self.label_id]  # Lấy tên nhãn từ model.names

            # Tính toán YOLO format: x_center, y_center, box_width, box_height (chuẩn hóa theo kích thước ảnh)
            self.x_center = float((x1 + x2) / 2 / self.img_width)
            self.y_center = float((y1 + y2) / 2 / self.img_height)
            self.box_width = float((x2 - x1) / self.img_width)
            self.box_height = float((y2 - y1) / self.img_height)

            # Thêm bounding box và nhãn vào danh sách theo định dạng YOLO
            bounding_boxes.append((self.x_center, self.y_center, self.box_width, self.box_height, label_name))

            # Vẽ bounding box lên ảnh
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  # Vẽ bounding box
            font_scale = 0.5
            font_thickness = 1
            text_size, _ = cv2.getTextSize(label_name, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)
            text_width, text_height = text_size
            cv2.rectangle(img, (int(x1), int(y1) - text_height - 4), (int(x1) + text_width, int(y1)), (0, 255, 0), -1)
            cv2.putText(img, label_name, (int(x1), int(y1) - 2), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), font_thickness)

        # Hiển thị ảnh trong QLabel
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channels = img_rgb.shape
        bytes_per_line = channels * width
        q_image = QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        
        # Cập nhật QLabel trên giao diện người dùng (cần đảm bảo thread an toàn)
        self.update_image(pixmap)
        
        # Gọi hàm display_info với bounding_boxes đã chuyển đổi (dạng YOLO format)
        self.display_info(self.img_width, self.img_height, bounding_boxes)

    def update_image(self, pixmap):
        """Cập nhật QLabel với hình ảnh đã xử lý."""
        # Đảm bảo cập nhật giao diện từ thread chính
        if self.img_output is not None:
            self.img_output.setPixmap(pixmap)
            self.img_output.setScaledContents(True)


    def choose_img(self, index):
        item = str(self.model1.data(index))
        item = item.strip()
        item = item[27:]
        self.tabWidget.setCurrentIndex(1)
        if os.path.isfile(item):
            _, extension = os.path.splitext(item)
            img_extension = ['.jpg','.png','.jpeg','.bmp']
            if extension.lower() in img_extension:
                self.display_message(f'Hiển thị dữ liệu chuẩn đoán file: {item}')
                self.detect_task(item)

    def add_process(self, index):
        if index:
            item = str(self.model1.data(index))
            item = item.strip()
            item = item[27:]
        else:
            item = self.input_terminal.toPlainText()
            item = item.replace('"','')
        directory, filename = os.path.split(item)
        conn = self.connection
        cursor = conn.cursor()
        with open(item, 'rb') as file:
            binary = file.read()
            self.insert_image(cursor, filename, binary, self.img_width, self.img_height)
            self.display_message("Đã thêm dữ liệu vào bảng images")
            image_id = self.get_image_id(cursor, filename)
            if image_id is None:
                self.display_message(f"Không tìm thấy hình ảnh cho {item}, không thể thêm bounding box.")
                return
            self.insert_bounding_box(cursor, image_id, self.label_id+1, self.x_center, self.y_center, self.box_width, self.box_height)
            self.display_message("Đã thêm dữ liệu vào bảng bounding_boxes")
            self.display_message(f"Id truy xuất: {image_id}")
        pass
        conn.commit()
        cursor.close()
    
    def insert_image(self,cursor, file_name, image_data, width, height):
        sql = """
            INSERT INTO images (filename, image_data, width, height) 
            VALUES (%s, %s, %s, %s)
        """
        val = (file_name, image_data, width, height)
        cursor.execute(sql, val)

    def get_image_id(self, cursor, file_name):
        cursor.execute("SELECT id FROM images WHERE filename = %s", (file_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def insert_bounding_box(self,cursor, image_id, label_id, x_center, y_center, width, height):
        sql = """
            INSERT INTO bounding_boxes (image_id, label_id, x_center, y_center, width, height)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (image_id, label_id, x_center, y_center, width, height)
        cursor.execute(sql, val)

    def delete(self):
        id = int(self.input_terminal.toPlainText())
        conn = self.connection
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM bounding_boxes
            WHERE image_id = %s
""", (id,))
        cursor.execute("""
            DELETE FROM images
            WHERE id = %s
""", (id,))
        self.display_message(f"Tiến hành xóa id: {id}")
        conn.commit()
        cursor.close()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
