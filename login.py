import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

import main
import service
from UI.login_ui import Ui_Form

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class LoginWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon(QIcon(os.path.join(BASE_DIR, 'resources/icons/app.png')))
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_exit.clicked.connect(QApplication.quit)
        self.lineEdit_pwd.returnPressed.connect(self.open_main)  # 按回车登录
        self.pushButton_login.clicked.connect(self.open_main)  # 按登录按钮登录

    def open_main(self):
        service.userName = self.lineEdit_user.text()
        self.userPwd = self.lineEdit_pwd.text()
        if service.userName != "" and self.userPwd != "":
            result = service.query_db("select * from tb_user where userName = %s and userPwd = %s",
                                      service.userName, self.userPwd)
            if len(result) > 0:
                # print("你好")
                self.m = main.MainWindow()
                self.m.show()
                self.close()
            else:
                self.lineEdit_user.setText("")
                self.lineEdit_pwd.setText("")
                QMessageBox.warning(None, '警告', '请输入正确的用户名和密码！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入用户名和密码！', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec())
