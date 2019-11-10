# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication


class Ui_longin(object):
    def setupUi(self, longin):
        longin.setObjectName("longin")
        longin.resize(222, 223)
        self.centralwidget = QtWidgets.QWidget(longin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 201, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 201, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 201, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 140, 201, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        longin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(longin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 222, 26))
        self.menubar.setObjectName("menubar")
        longin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(longin)
        self.statusbar.setObjectName("statusbar")
        longin.setStatusBar(self.statusbar)

        self.retranslateUi(longin)
        QtCore.QMetaObject.connectSlotsByName(longin)

    def retranslateUi(self, longin):
        _translate = QtCore.QCoreApplication.translate
        longin.setWindowTitle(_translate("longin", "登录"))
        self.label.setText(_translate("longin", "用户名（admin）"))
        self.label_2.setText(_translate("longin", "密码（666666）"))
        self.pushButton.setText(_translate("longin", "登录"))
        self.pushButton_2.setText(_translate("longin", "退出"))

    def onclick(self):
        if self.lineEdit.text() == 'admin':
            if self.lineEdit_2.text() == '666666':
                MainWindow.close()
            else:
                self.lineEdit_2.setText('密码错误请重新输入')
        else:
            self.lineEdit.setText('用户名错误请重新输入')


if __name__ == '__main__':
    App = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_longin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(App.exec_())
