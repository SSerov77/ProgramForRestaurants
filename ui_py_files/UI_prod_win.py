# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proect_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 600)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setMinimumSize(QtCore.QSize(0, 10))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setFlat(False)
        self.back.setObjectName("back")
        self.horizontalLayout_2.addWidget(self.back)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.line_find = QtWidgets.QLineEdit(Dialog)
        self.line_find.setText("")
        self.line_find.setObjectName("line_find")
        self.horizontalLayout_2.addWidget(self.line_find)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.find = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.find.setFont(font)
        self.find.setObjectName("find")
        self.horizontalLayout.addWidget(self.find)
        self.upload = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.upload.setFont(font)
        self.upload.setObjectName("upload")
        self.horizontalLayout.addWidget(self.upload)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.apend = QtWidgets.QPushButton(Dialog)
        self.apend.setMinimumSize(QtCore.QSize(155, 0))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.apend.setFont(font)
        self.apend.setObjectName("apend")
        self.horizontalLayout_6.addWidget(self.apend)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Поставки продуктов"))
        self.back.setText(_translate("Dialog", "<-"))
        self.label_4.setText(_translate("Dialog", "Поиск:"))
        self.find.setText(_translate("Dialog", "Найти"))
        self.upload.setText(_translate("Dialog", "Выгрузить"))
        self.apend.setText(_translate("Dialog", "Добавить"))
