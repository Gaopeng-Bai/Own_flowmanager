# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flowmanager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(918, 681)
        MainWindow.setWindowOpacity(0.98)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(115, 210, 22);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ip_adderss = QtWidgets.QLineEdit(self.groupBox)
        self.ip_adderss.setObjectName("ip_adderss")
        self.gridLayout.addWidget(self.ip_adderss, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.port = QtWidgets.QLineEdit(self.groupBox)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Connect_server = QtWidgets.QPushButton(self.groupBox)
        self.Connect_server.setObjectName("Connect_server")
        self.gridLayout.addWidget(self.Connect_server, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 4, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 6, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.showframe = QtWidgets.QGridLayout()
        self.showframe.setObjectName("showframe")
        self.switch_desc_num_4 = QtWidgets.QLabel(self.centralwidget)
        self.switch_desc_num_4.setObjectName("switch_desc_num_4")
        self.showframe.addWidget(self.switch_desc_num_4, 2, 1, 1, 1)
        self.switch_desc_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.switch_desc_3.setObjectName("switch_desc_3")
        self.showframe.addWidget(self.switch_desc_3, 3, 1, 1, 1)
        self.switch_desc_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.switch_desc_2.setObjectName("switch_desc_2")
        self.showframe.addWidget(self.switch_desc_2, 1, 1, 1, 1)
        self.switch_desc_num = QtWidgets.QLabel(self.centralwidget)
        self.switch_desc_num.setObjectName("switch_desc_num")
        self.showframe.addWidget(self.switch_desc_num, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.showframe.addItem(spacerItem6, 1, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.showframe.addItem(spacerItem7, 1, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.showframe.addItem(spacerItem8, 1, 3, 1, 1)
        self.switch_desc_num_2 = QtWidgets.QLabel(self.centralwidget)
        self.switch_desc_num_2.setObjectName("switch_desc_num_2")
        self.showframe.addWidget(self.switch_desc_num_2, 2, 5, 1, 1)
        self.switch_desc = QtWidgets.QTextBrowser(self.centralwidget)
        self.switch_desc.setObjectName("switch_desc")
        self.showframe.addWidget(self.switch_desc, 1, 5, 1, 1)
        self.switch_desc_num_3 = QtWidgets.QLabel(self.centralwidget)
        self.switch_desc_num_3.setObjectName("switch_desc_num_3")
        self.showframe.addWidget(self.switch_desc_num_3, 0, 5, 1, 1)
        self.switch_desc_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.switch_desc_4.setObjectName("switch_desc_4")
        self.showframe.addWidget(self.switch_desc_4, 3, 5, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.showframe.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.showframe.addItem(spacerItem10, 1, 2, 1, 1)
        self.horizontalLayout.addLayout(self.showframe)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Ryu Server"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.label.setText(_translate("MainWindow", "IP Address"))
        self.Connect_server.setText(_translate("MainWindow", "Connect"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.switch_desc_num_4.setText(_translate("MainWindow", "Switch Desc"))
        self.switch_desc_num.setText(_translate("MainWindow", "Switch Desc"))
        self.switch_desc_num_2.setText(_translate("MainWindow", "Switch Desc"))
        self.switch_desc_num_3.setText(_translate("MainWindow", "Switch Desc"))
