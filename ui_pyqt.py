# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.build = QtWidgets.QPushButton(self.centralwidget)
        self.build.setGeometry(QtCore.QRect(230, 490, 131, 41))
        self.build.setObjectName("build")
        self.install = QtWidgets.QPushButton(self.centralwidget)
        self.install.setGeometry(QtCore.QRect(240, 0, 101, 31))
        self.install.setObjectName("install")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(170, 220, 271, 231))
        self.text.setText("")
        self.text.setObjectName("text")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 110, 132, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_image = QtWidgets.QPushButton(self.layoutWidget)
        self.add_image.setObjectName("add_image")
        self.verticalLayout.addWidget(self.add_image)
        self.remove_image = QtWidgets.QPushButton(self.layoutWidget)
        self.remove_image.setObjectName("remove_image")
        self.verticalLayout.addWidget(self.remove_image)
        self.add_mode = QtWidgets.QPushButton(self.layoutWidget)
        self.add_mode.setObjectName("add_mode")
        self.verticalLayout.addWidget(self.add_mode)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(110, 120, 77, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_layer = QtWidgets.QPushButton(self.layoutWidget1)
        self.add_layer.setObjectName("add_layer")
        self.verticalLayout_2.addWidget(self.add_layer)
        self.remove_layer = QtWidgets.QPushButton(self.layoutWidget1)
        self.remove_layer.setObjectName("remove_layer")
        self.verticalLayout_2.addWidget(self.remove_layer)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(420, 100, 121, 102))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enter_text = QtWidgets.QTextEdit(self.widget)
        self.enter_text.setObjectName("enter_text")
        self.verticalLayout_3.addWidget(self.enter_text)
        self.enter = QtWidgets.QPushButton(self.widget)
        self.enter.setObjectName("enter")
        self.verticalLayout_3.addWidget(self.enter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
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
        self.build.setText(_translate("MainWindow", "Build"))
        self.install.setText(_translate("MainWindow", "Install script"))
        self.add_image.setText(_translate("MainWindow", "Add image to layer"))
        self.remove_image.setText(_translate("MainWindow", "Remove image from layer"))
        self.add_mode.setText(_translate("MainWindow", "Add mode"))
        self.add_layer.setText(_translate("MainWindow", "Add layer"))
        self.remove_layer.setText(_translate("MainWindow", "Remove layer"))
        self.enter.setText(_translate("MainWindow", "Enter"))
