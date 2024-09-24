# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYHSTmS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import mysql.connector

db_config = {
    'host':"localhost",      # Địa chỉ máy chủ MySQL, có thể thay đổi tùy theo môi trường của bạn
    'user':"sqluser",        # Tên người dùng MySQL
    'password':"password",   # Mật khẩu MySQL
    'database':"mydatabase"  # Tên cơ sở dữ liệu để chèn dữ liệu
}
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(541, 622)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 261, 51))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 70, 501, 101))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 100, 481, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.id_text = QTextEdit(self.horizontalLayoutWidget)
        self.id_text.setObjectName(u"id_text")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.id_text.setFont(font1)

        self.horizontalLayout.addWidget(self.id_text)

        self.get_button = QPushButton(self.horizontalLayoutWidget)
        self.get_button.setObjectName(u"get_button")
        font2 = QFont()
        font2.setPointSize(12)
        self.get_button.setFont(font2)

        self.horizontalLayout.addWidget(self.get_button)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 180, 501, 331))
        self.outdata = QPlainTextEdit(self.groupBox_2)
        self.outdata.setObjectName(u"outdata")
        self.outdata.setEnabled(True)
        self.outdata.setGeometry(QRect(10, 20, 481, 301))
        self.outdata.setReadOnly(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"MYSQL DATABASE", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Enter Banana's ID:", None))
        self.id_text.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.get_button.setText(QCoreApplication.translate("Dialog", u"Crawl", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"OUTPUT DATA", None))
    # retranslateUi

class ConsoleMainWindow(QMainWindow):
    def __init__(self):
        super(ConsoleMainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.get_button.clicked.connect(self.get_data_by_id)
    def get_data_by_id(self):
        table_name = 'banana'
        record_id = self.ui.id_text.toPlainText()
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
                self.ui.outdata.setPlainText(form)
            else:
                self.ui.outdata.setPlainText(f"Không tìm thấy bản ghi với id = {record_id}")

        except mysql.connector.Error as err:
            self.ui.outdata.setPlainText(f"Lỗi: {err}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

if __name__ == '__main__':
    # Cấu hình kết nối cơ sở dữ liệu

    app = QApplication(sys.argv)
    mainwin = ConsoleMainWindow()
    mainwin.show()
    sys.exit(app.exec_())
