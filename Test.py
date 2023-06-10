from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import *
import os
import sys

class Ui_MainWindow(object):

    audio_vol = 0.2

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 525)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.Btn_Toggle_2 = QtWidgets.QPushButton(self.frame_top)
        self.Btn_Toggle_2.setGeometry(QtCore.QRect(900, 10, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle_2.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle_2.setSizePolicy(sizePolicy)
        self.Btn_Toggle_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(120, 0, 0);\n"
"    border: 0px solid;\n"
"    border-radius:15px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}")
        self.Btn_Toggle_2.setObjectName("Btn_Toggle_2")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_page_1.setFont(font)
        self.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_page_2.setFont(font)
        self.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setStyleSheet("")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget = QtWidgets.QWidget(self.page_1)
        self.widget.setStyleSheet("background-image: url(:/Img/png3.jpg);")
        self.widget.setObjectName("widget")
        self.widget_Page_1 = QtWidgets.QWidget(self.widget)
        self.widget_Page_1.setGeometry(QtCore.QRect(70, 10, 821, 391))
        self.widget_Page_1.setObjectName("widget_Page_1")
        self.label_4 = QtWidgets.QLabel(self.widget_Page_1)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setLineWidth(2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(self.widget_Page_1)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 311, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 20px;")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_5 = QtWidgets.QLabel(self.widget_Page_1)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setLineWidth(2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_Page_1)
        self.label_6.setGeometry(QtCore.QRect(180, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.label_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_6.setLineWidth(2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_Page_1)
        self.label_7.setGeometry(QtCore.QRect(460, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setLineWidth(2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_Page_1)
        self.listWidget_2.setGeometry(QtCore.QRect(460, 80, 311, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 20px;")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.label_8 = QtWidgets.QLabel(self.widget_Page_1)
        self.label_8.setGeometry(QtCore.QRect(910, 40, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.label_8.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_8.setLineWidth(2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.widget_Page_1)
        self.label_12.setGeometry(QtCore.QRect(540, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_12.setFont(font)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.label_12.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_12.setLineWidth(2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_Page_2 = QtWidgets.QWidget(self.page_2)
        self.widget_Page_2.setObjectName("widget_Page_2")
        self.Volume_US = QtWidgets.QSlider(self.widget_Page_2)
        self.Volume_US.setGeometry(QtCore.QRect(90, 60, 20, 370))
        self.Volume_US.setOrientation(QtCore.Qt.Vertical)
        self.Volume_US.setObjectName("Volume_US")
        self.Volume_GP = QtWidgets.QSlider(self.widget_Page_2)
        self.Volume_GP.setGeometry(QtCore.QRect(260, 60, 20, 370))
        self.Volume_GP.setOrientation(QtCore.Qt.Vertical)
        self.Volume_GP.setObjectName("Volume_GP")
        self.Name_Vol_US = QtWidgets.QLabel(self.widget_Page_2)
        self.Name_Vol_US.setGeometry(QtCore.QRect(200, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Name_Vol_US.setFont(font)
        self.Name_Vol_US.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Name_Vol_US.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_Vol_US.setObjectName("Name_Vol_US")
        self.Name_Vol_GP = QtWidgets.QLabel(self.widget_Page_2)
        self.Name_Vol_GP.setGeometry(QtCore.QRect(30, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Name_Vol_GP.setFont(font)
        self.Name_Vol_GP.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Name_Vol_GP.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_Vol_GP.setObjectName("Name_Vol_GP")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.widget_Page_2)
        self.calendarWidget.setGeometry(QtCore.QRect(450, 20, 381, 191))
        self.calendarWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendarWidget.setStyleSheet("color: rgb(10, 137, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(88, 88, 88);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(139, 139, 209);\n"
"border-radius: 20px;")
        self.calendarWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.calendarWidget.setNavigationBarVisible(False)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.Command_list = QtWidgets.QLabel(self.widget_Page_2)
        self.Command_list.setGeometry(QtCore.QRect(446, 222, 391, 211))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Command_list.setFont(font)
        self.Command_list.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 20px;")
        self.Command_list.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Command_list.setObjectName("Command_list")
        self.Num_US = QtWidgets.QLabel(self.widget_Page_2)
        self.Num_US.setGeometry(QtCore.QRect(50, 230, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Num_US.setFont(font)
        self.Num_US.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Num_US.setAlignment(QtCore.Qt.AlignCenter)
        self.Num_US.setObjectName("Num_US")
        self.Num_GP = QtWidgets.QLabel(self.widget_Page_2)
        self.Num_GP.setGeometry(QtCore.QRect(280, 230, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Num_GP.setFont(font)
        self.Num_GP.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Num_GP.setAlignment(QtCore.Qt.AlignCenter)
        self.Num_GP.setObjectName("Num_GP")
        self.verticalLayout_6.addWidget(self.widget_Page_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_Page_3 = QtWidgets.QWidget(self.page_3)
        self.widget_Page_3.setObjectName("widget_Page_3")
        self.Name_Person = QtWidgets.QLabel(self.widget_Page_3)
        self.Name_Person.setGeometry(QtCore.QRect(40, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name_Person.setFont(font)
        self.Name_Person.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Name_Person.setAlignment(QtCore.Qt.AlignCenter)
        self.Name_Person.setObjectName("Name_Person")
        self.Quete_1 = QtWidgets.QLabel(self.widget_Page_3)
        self.Quete_1.setGeometry(QtCore.QRect(40, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Quete_1.setFont(font)
        self.Quete_1.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Quete_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Quete_1.setObjectName("Quete_1")
        self.Quete_2 = QtWidgets.QLabel(self.widget_Page_3)
        self.Quete_2.setGeometry(QtCore.QRect(40, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Quete_2.setFont(font)
        self.Quete_2.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Quete_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Quete_2.setObjectName("Quete_2")
        self.Road = QtWidgets.QLabel(self.widget_Page_3)
        self.Road.setGeometry(QtCore.QRect(40, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.Road.setFont(font)
        self.Road.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Road.setAlignment(QtCore.Qt.AlignCenter)
        self.Road.setObjectName("Road")
        self.Accept_Name = QtWidgets.QPushButton(self.widget_Page_3)
        self.Accept_Name.setGeometry(QtCore.QRect(370, 35, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Accept_Name.setFont(font)
        self.Accept_Name.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(59, 59, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"    font: 75 10pt \"Unispace\";")
        self.Accept_Name.setObjectName("Accept_Name")
        self.Accept_Quete = QtWidgets.QPushButton(self.widget_Page_3)
        self.Accept_Quete.setGeometry(QtCore.QRect(370, 95, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Accept_Quete.setFont(font)
        self.Accept_Quete.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(59, 59, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"    font: 75 10pt \"Unispace\";")
        self.Accept_Quete.setObjectName("Accept_Quete")
        self.Accept_Quete_2 = QtWidgets.QPushButton(self.widget_Page_3)
        self.Accept_Quete_2.setGeometry(QtCore.QRect(370, 155, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Accept_Quete_2.setFont(font)
        self.Accept_Quete_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(59, 59, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"    font: 75 12pt \"Unispace\";")
        self.Accept_Quete_2.setObjectName("Accept_Quete_2")
        self.Accept_Road = QtWidgets.QPushButton(self.widget_Page_3)
        self.Accept_Road.setGeometry(QtCore.QRect(370, 215, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Accept_Road.setFont(font)
        self.Accept_Road.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgba(0,0,0,0);\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(59, 59, 88);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 85, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"    font: 75 10pt \"Unispace\";")
        self.Accept_Road.setObjectName("Accept_Road")
        self.Name_text = QtWidgets.QLineEdit(self.widget_Page_3)
        self.Name_text.setGeometry(QtCore.QRect(200, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Name_text.setFont(font)
        self.Name_text.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Name_text.setObjectName("Name_text")
        self.Quete_text = QtWidgets.QLineEdit(self.widget_Page_3)
        self.Quete_text.setGeometry(QtCore.QRect(200, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Quete_text.setFont(font)
        self.Quete_text.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Quete_text.setObjectName("Quete_text")
        self.Quete_2_text = QtWidgets.QLineEdit(self.widget_Page_3)
        self.Quete_2_text.setGeometry(QtCore.QRect(200, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Quete_2_text.setFont(font)
        self.Quete_2_text.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Quete_2_text.setObjectName("Quete_2_text")
        self.Road_text = QtWidgets.QLineEdit(self.widget_Page_3)
        self.Road_text.setGeometry(QtCore.QRect(200, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Road_text.setFont(font)
        self.Road_text.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 59, 88);\n"
"border-radius: 10px;")
        self.Road_text.setObjectName("Road_text")
        self.verticalLayout_8.addWidget(self.widget_Page_3)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Toggle.setText(_translate("MainWindow", "TOGGLE"))
        self.Btn_Toggle_2.setText(_translate("MainWindow", "Exit"))
        self.btn_page_1.setText(_translate("MainWindow", "Функции"))
        self.btn_page_2.setText(_translate("MainWindow", "Управление"))
        self.btn_page_3.setText(_translate("MainWindow", "Настройки"))
        self.label_4.setText(_translate("MainWindow", "Функции"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Выключение УС"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Перезагрузка УС"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Выключение ГА"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "YouTube"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "VK"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "След. песня"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "Пред. песня"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "Закрыть браузер"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "Закрыть вкладку"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "Изменение громкости"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "Прочитать заметку"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "Измен, разм, изображ,"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "Цитата"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "УС - усстройство(а)"))
        self.label_6.setText(_translate("MainWindow", "ГА - голосоввой асистент"))
        self.label_7.setText(_translate("MainWindow", "Команды"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Стоп, полное выключение, полное отключение"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "Рестарт, перезагрузка"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "Выключись, отбой, хватит, отключение"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "Ютюб, открой ютюб, видео , youtube"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "Музыка, включи музыку, вк"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "Перелистни музыку, следующая, перелистни"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("MainWindow", "Верни, назад, прошлую"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("MainWindow", "Закрой ютюб/вк/браузер, закрой"))
        item = self.listWidget_2.item(9)
        item.setText(_translate("MainWindow", "Закрой вкладку, убери лишнее, удали мусор"))
        item = self.listWidget_2.item(10)
        item.setText(_translate("MainWindow", "Громкость(x), звук(x), измени звук(x)/громкость(x)"))
        item = self.listWidget_2.item(11)
        item.setText(_translate("MainWindow", "Дневник(x), заметка(x), запись(x)"))
        item = self.listWidget_2.item(12)
        item.setText(_translate("MainWindow", "Измени(ть) размер изображения"))
        item = self.listWidget_2.item(13)
        item.setText(_translate("MainWindow", "Цитата(x)"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "x - любое число в команде"))
        self.Name_Vol_US.setText(_translate("MainWindow", "Громкость ГП"))
        self.Name_Vol_GP.setText(_translate("MainWindow", "Громкость УС"))
        self.Command_list.setText(_translate("MainWindow", "Text"))
        self.Num_US.setText(_translate("MainWindow", "0"))
        self.Num_GP.setText(_translate("MainWindow", "0"))
        self.Name_Person.setText(_translate("MainWindow", "Ваше имя"))
        self.Quete_1.setText(_translate("MainWindow", "Ваша цитата"))
        self.Quete_2.setText(_translate("MainWindow", "Ваша цитата 2"))
        self.Road.setText(_translate("MainWindow", "Путь к вашему приложению"))
        self.Accept_Name.setText(_translate("MainWindow", "Добавить"))
        self.Accept_Quete.setText(_translate("MainWindow", "Добавить"))
        self.Accept_Quete_2.setText(_translate("MainWindow", "Добавить"))
        self.Accept_Road.setText(_translate("MainWindow", "Добавить"))

        self.Volume_US.setMinimum(0)
        self.Volume_US.setMaximum(100)
        self.Volume_US.setValue(0)
        self.Volume_US.setTickPosition(QSlider.TicksBelow)
        self.Volume_US.setTickInterval(10)
        self.Volume_US.valueChanged[int].connect(self.Volume_US_Controller)
        self.Volume_GP.setMinimum(1)
        self.Volume_GP.setMaximum(100)
        self.Volume_GP.setValue(0)
        self.Volume_GP.setTickPosition(QSlider.TicksBelow)
        self.Volume_GP.setTickInterval(10)
        self.Volume_GP.valueChanged[int].connect(self.Volume_GP_Controller)

    def Exit(self):
        self.close()

    def Volume_US_Controller(self, value):
        os.system(f'nircmd.exe setsysvolume 0')
        os.system(f'nircmd.exe changesysvolume +{value*655}')

    def Volume_GP_Controller(self, value):
        audio_vol = value/100
        return audio_vol

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


class UIFunctions(MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

