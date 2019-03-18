# -*- coding: utf-8 -*-
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtCore import QRect


#程序功能
#将选中文件夹下的ncm音乐转换为mp3或flac格式

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        #主程序框的大小
        self.resize(600, 400)

        #文字
        self.myText = QtWidgets.QLabel(self)
        #label文字框的大小
        self.myText.setGeometry(QRect(100.0, 100.0, 1000.0, 40.0))
        self.myText.setText("路径为：")
        # 定义字体
        self.myText.setFont(QFont("", 14, QFont.Bold))

        #按钮
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setGeometry(QRect(250.0, 200.0, 80.0, 40.0))
        self.myButton.setObjectName("btn")
        self.myButton.setText("选择文件夹")
        # msg函数绑定点击事件
        self.myButton.clicked.connect(self.msg)


    def msg(self):
        str = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        self.myText.setText("路径为：" + str)
        os.system(os.getcwd()+'/main.exe '+ str)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())