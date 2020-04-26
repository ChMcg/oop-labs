# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lab_03(object):
    def setupUi(self, lab_03):
        lab_03.setObjectName("lab_03")
        lab_03.resize(400, 300)
        self.btn = QtWidgets.QPushButton(lab_03)
        self.btn.setGeometry(QtCore.QRect(240, 250, 80, 25))
        self.btn.setObjectName("btn")
        self.input = QtWidgets.QLineEdit(lab_03)
        self.input.setGeometry(QtCore.QRect(90, 50, 281, 25))
        self.input.setObjectName("input")
        self.one = QtWidgets.QLabel(lab_03)
        self.one.setGeometry(QtCore.QRect(160, 160, 211, 21))
        self.one.setText("")
        self.one.setObjectName("one")
        self.two = QtWidgets.QLabel(lab_03)
        self.two.setGeometry(QtCore.QRect(160, 190, 211, 21))
        self.two.setText("")
        self.two.setObjectName("two")
        self.info = QtWidgets.QLabel(lab_03)
        self.info.setGeometry(QtCore.QRect(90, 100, 281, 51))
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info.setWordWrap(True)
        self.info.setObjectName("info")
        self.label = QtWidgets.QLabel(lab_03)
        self.label.setGeometry(QtCore.QRect(20, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(lab_03)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 54, 21))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(lab_03)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 54, 21))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(lab_03)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 54, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(lab_03)
        self.label_5.setGeometry(QtCore.QRect(80, 40, 301, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.btn.raise_()
        self.input.raise_()
        self.one.raise_()
        self.two.raise_()
        self.info.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(lab_03)
        QtCore.QMetaObject.connectSlotsByName(lab_03)

    def retranslateUi(self, lab_03):
        _translate = QtCore.QCoreApplication.translate
        lab_03.setWindowTitle(_translate("lab_03", "lab_03"))
        self.btn.setText(_translate("lab_03", "Вычислить"))
        self.input.setPlaceholderText(_translate("lab_03", "Введите многочлен в векторной форме"))
        self.label.setText(_translate("lab_03", "V ="))
        self.label_2.setText(_translate("lab_03", "x_1:"))
        self.label_3.setText(_translate("lab_03", "x_2:"))
        self.label_4.setText(_translate("lab_03", "f(x) ="))
        self.label_5.setText(_translate("lab_03", "(                                                                      )"))


