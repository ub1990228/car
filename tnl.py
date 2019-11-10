# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tnl.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import urllib.request
from bs4 import BeautifulSoup
import os
from PIL import Image


# 获取汽车图片方法类
class ReTbmm():
    def Retbmm(self):
        # 爬虫开始时间
        start = time.time()
        # 用于返回当前工作目录
        self.cdir = os.getcwd()
        # 爬取的网站：https://www.autohome.com.cn/spec/32890/?pvareaid=2023562
        # 车身外观
        url1 = 'https://car.autohome.com.cn/pic/series-s32890/385-1.html#pvareaid=2042222'
        # 中控方向盘
        url2 = 'https://car.autohome.com.cn/pic/series-s32890/385-10.html#pvareaid=2042220'
        # 车厢座椅
        url3 = 'https://car.autohome.com.cn/pic/series-s32890/385-3.html#pvareaid=2042220'
        # 其它细节
        url4 = 'https://car.autohome.com.cn/pic/series-s32890/385-12.html#pvareaid=2042220'
        self.getImg('车身外观', url1)
        self.getImg('中控方向盘', url2)
        self.getImg('车厢座椅', url3)
        self.getImg('其它细节', url4)
        end = time.time()
        # 输出运行时间
        print('run time:' + str(end - start))

    # 下载图片方法
    def getImg(self, name, urls):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
        headers = {'User_Agent': user_agent}
        # 访问连接
        request = urllib.request.Request(urls, headers=headers)
        # 获取数据
        response = urllib.request.urlopen(request)
        # 解析数据
        bsObj = BeautifulSoup(response, 'html.parser')
        # 查找所有img标记
        t1 = bsObj.find_all('img')
        for t2 in t1:
            t3 = t2.get('src')
            print(t3)
        # 创建图片路径
        path = self.cdir + '/carimages/' + str(name)
        # 读取路径
        if not os.path.exists(path):
            # 根据路径创建图片文件夹
            os.makedirs(path)
        # 每次调用初始化图片序列号
        n = 0
        # 循环图片集合
        for img in t1:
            # 每次图片序号加1
            n = n + 1
            # 获取图片路径
            link = img.get('src')
            # 判断图片路径是否存在
            if link:
                # 拼接图片链接
                s = 'http:' + str(link)
                # 分离文件扩展名
                i = link[link.rfind('.'):]
                try:
                    # 访问图片链接
                    request = urllib.request.Request(s)
                    # 获取返回事件
                    response = urllib.request.urlopen(request)
                    # 读取返回内容
                    imgData = response.read()
                    # 创建文件
                    pathfile = path + r'/' + str(n) + i
                    # 打开文件
                    with open(pathfile, 'wb') as f:
                        # 图片写入文件
                        f.write(imgData)
                        print('thread' + name + 'write:' + pathfile)
                finally:
                    print(str(name) + ' thread write false:' + s)


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 900)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 181, 800))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.treeView = QTreeWidget(self.scrollAreaWidgetContents)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 181, 761))
        self.treeView.setObjectName("treeView")
        self.treeView.setHeaderLabel('爬虫爬出的结果')
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(200, 70, 1000, 800))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "阿斯顿·马丁 汽车图片"))
        self.root = QTreeWidgetItem(self.treeView)
        self.root.setText(0, 'V8 Vantage 2018款 4.0T V8')
        self.pushButton.clicked.connect(self.btnstate)

    # 搜索方法
    def btnstate(self):
        # 开始搜索隐藏按钮
        self.pushButton.setVisible(False)
        # 实例化爬虫类
        ui = ReTbmm()
        # 开启爬虫方法
        ui.Retbmm()
        # 显示已完成按钮
        self.pushButton.setVisible(True)
        # 设置文件路径，为了树形结构做准备
        self.path = cdir + '/carimages'
        # 查找路径下的所有文件名称
        dirs = os.listdir(self.path)
        # 循环文件名称
        for dir in dirs:
            # 添加文件名称到树形结构
            QTreeWidgetItem(self.root).setText(0, dir)
        self.treeView.clicked.connect(self.onTreeClicked)

    # 树形结构点击后在这里处理
    def onTreeClicked(self, Qmodelidx):
        # 点击获得树形结构
        items = self.treeView.currentItem()
        # 判断单击的节点
        if items.text(0) == 'V8 Vantage 2018款 4.0T V8':
            # 单击的主节点在这里出来
            # 删除节点root下的子节点
            self.root.takeChild()
            # 获取路径下的所有文件
            dirs = os.listdir(self.path)
            # 循环文件
            for dir in dirs:
                # 设置子节点
                QTreeWidgetItem(self.root).setText(0, dir)
            # 注册点击事件
            self.treeView.clicked.connect(self.onTreeclicked)
            pass
        else:
            # 每次循环删除管理器的组件
            while self.gridLayout.count():
                # 获取第一个组件
                item = self.gridLayout.takeAt(0)
                # 删除组件
                widget = item.widget()
                widget.deleteLater()
            # 每次点击树形结构把图片集合清空
            filenames = []
            # 根据路径查找文件夹下的所有文件
            for filename in os.listdir(cdir + '/carimages/' + items.text(0)):
                # 把名称添加到集合中
                filenames.append(filename)
            # 行数标记
            i = -1
            # 根据图片的数量进行循环
            for n in range(len(filenames)):
                # x确认每行显示的个数0，1，2每行3个
                x = n % 3
                # 当x为0的时候设置换行，行数+1
                if (x == 0):
                    i += 1
                # 创建布局
                self.widget = QWidget()
                # 设置布局大小
                self.widget.setGeometry(QtCore.QRect(110, 40, 350, 300))
                # 给布局命名
                self.widget.setObjectName('widget' + str(n))
                # 创建控件用于显示图片的Qlabel,设置控件在QWidget中
                self.label = QLabel(self.widget)
                # 设置大小
                self.label.setGeometry(QtCore.QRect(0, 0, 350, 300))
                # 设置要显示的图片
                self.label.setPixmap(QPixmap(self.path + '/' + items.text(0) + '/' + filenames[n]))
                # 图片显示方式，让图片适应Qlabel的大小
                self.label.setScaledContents(True)
                # 给图片控件命名
                self.label.setObjectName('label' + str(n))
                # 创建按钮，用于点击后放大图片，设置按钮在QWidget中
                self.commandLinkButton = QCommandLinkButton(self.widget)
                # 设置按钮位置
                self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 111, 41))
                # 给按钮组命名
                self.commandLinkButton.setText(filenames[n])
                # 设置按钮上显示的文字
                self.commandLinkButton.setObjectName('commandLinkButton' + str(n))
                # 注册信号槽使用的lambda传递参数给方法
                self.commandLinkButton.clicked.connect(lambda: self.wichbtn(self.path + '/' + items.text(0) + '/'))
                # 把动态添加的widget布局添加到gridlayout中，i，x分别代表行数及每行的个数
                self.gridLayout.addWidget(self.widget, i, x)
            self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
            self.verticalLayout.addWidget(self.scrollArea_2)
            self.scrollAreaWidgetContents_2.setMaximumWidth(800)
            self.scrollAreaWidgetContents_2.setMinimumHeight(i * 300)

        # 信号槽点击显示大图功能
        def wichbtn(self, tppath):
            # 获取信号源点击的按钮
            sender = self.gridLayout.sender()
            # 使用电脑中的看图工具打开图片
            img = Image.open(tppath + sender.text())
            img.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    cdir = os.getcwd()
    ex = Ui_Form()
    ex.setupUi(MainWindow1)
    MainWindow1.show()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    sys.exit(App.exec_())
