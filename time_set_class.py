# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time_set_class.ui'
#
# Created: Thu Feb  9 22:36:07 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(428, 328)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(350, 100))
        Dialog.setMaximumSize(QtCore.QSize(450, 1000))
        Dialog.setStyleSheet("QPushButton{\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius: 10%;\n"
"border-color: rgb(0, 0, 0);\n"
"border:1px solid\n"
"}")
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timePrice1 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.timePrice1.setFont(font)
        self.timePrice1.setReadOnly(True)
        self.timePrice1.setObjectName("timePrice1")
        self.verticalLayout.addWidget(self.timePrice1)
        self.timePrice2 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.timePrice2.setFont(font)
        self.timePrice2.setReadOnly(True)
        self.timePrice2.setObjectName("timePrice2")
        self.verticalLayout.addWidget(self.timePrice2)
        self.timePrice3 = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.timePrice3.setFont(font)
        self.timePrice3.setText("")
        self.timePrice3.setReadOnly(True)
        self.timePrice3.setObjectName("timePrice3")
        self.verticalLayout.addWidget(self.timePrice3)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.pushButton015 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton015.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton015.setFont(font)
        self.pushButton015.setObjectName("pushButton015")
        self.gridLayout.addWidget(self.pushButton015, 5, 0, 1, 1)
        self.pushButton030 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton030.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton030.setFont(font)
        self.pushButton030.setObjectName("pushButton030")
        self.gridLayout.addWidget(self.pushButton030, 5, 1, 1, 1)
        self.pushButton045 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton045.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton045.setFont(font)
        self.pushButton045.setObjectName("pushButton045")
        self.gridLayout.addWidget(self.pushButton045, 5, 2, 1, 1)
        self.l = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.l.setFont(font)
        self.l.setObjectName("l")
        self.gridLayout.addWidget(self.l, 1, 0, 1, 1)
        self.pushButtonOK = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonOK.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonOK.setFont(font)
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.gridLayout.addWidget(self.pushButtonOK, 0, 0, 1, 1)
        self.l_3 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.l_3.setFont(font)
        self.l_3.setObjectName("l_3")
        self.gridLayout.addWidget(self.l_3, 1, 2, 1, 1)
        self.pushButton999 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton999.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton999.setFont(font)
        self.pushButton999.setObjectName("pushButton999")
        self.gridLayout.addWidget(self.pushButton999, 4, 0, 1, 1)
        self.pushButtonCancel = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.gridLayout.addWidget(self.pushButtonCancel, 0, 1, 1, 1)
        self.pushButton060 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton060.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton060.setFont(font)
        self.pushButton060.setObjectName("pushButton060")
        self.gridLayout.addWidget(self.pushButton060, 4, 1, 1, 1)
        self.l_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.l_2.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.l_2.setFont(font)
        self.l_2.setObjectName("l_2")
        self.gridLayout.addWidget(self.l_2, 1, 1, 1, 1)
        self.pushButton120 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton120.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton120.setFont(font)
        self.pushButton120.setObjectName("pushButton120")
        self.gridLayout.addWidget(self.pushButton120, 4, 2, 1, 1)
        self.pushButtonClear = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButtonClear.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout.addWidget(self.pushButtonClear, 0, 2, 1, 1)
        self.priceTotal = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.priceTotal.setFont(font)
        self.priceTotal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.priceTotal.setReadOnly(True)
        self.priceTotal.setObjectName("priceTotal")
        self.gridLayout.addWidget(self.priceTotal, 2, 2, 1, 1)
        self.timeRemain = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.timeRemain.setFont(font)
        self.timeRemain.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.timeRemain.setReadOnly(True)
        self.timeRemain.setObjectName("timeRemain")
        self.gridLayout.addWidget(self.timeRemain, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButtonOK, self.pushButton030)
        Dialog.setTabOrder(self.pushButton030, self.pushButton045)
        Dialog.setTabOrder(self.pushButton045, self.pushButton015)
        Dialog.setTabOrder(self.pushButton015, self.pushButton999)
        Dialog.setTabOrder(self.pushButton999, self.pushButtonCancel)
        Dialog.setTabOrder(self.pushButtonCancel, self.pushButton060)
        Dialog.setTabOrder(self.pushButton060, self.pushButton120)
        Dialog.setTabOrder(self.pushButton120, self.pushButtonClear)
        Dialog.setTabOrder(self.pushButtonClear, self.priceTotal)
        Dialog.setTabOrder(self.priceTotal, self.timeRemain)
        Dialog.setTabOrder(self.timeRemain, self.timePrice1)
        Dialog.setTabOrder(self.timePrice1, self.timePrice2)
        Dialog.setTabOrder(self.timePrice2, self.timePrice3)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Set time", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton015.setText(QtGui.QApplication.translate("Dialog", "15 mins", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton030.setText(QtGui.QApplication.translate("Dialog", "30 mins", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton045.setText(QtGui.QApplication.translate("Dialog", "45 mins", None, QtGui.QApplication.UnicodeUTF8))
        self.l.setText(QtGui.QApplication.translate("Dialog", "Remain", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOK.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.l_3.setText(QtGui.QApplication.translate("Dialog", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton999.setText(QtGui.QApplication.translate("Dialog", "Free time", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton060.setText(QtGui.QApplication.translate("Dialog", "1 hour", None, QtGui.QApplication.UnicodeUTF8))
        self.l_2.setText(QtGui.QApplication.translate("Dialog", "Per minute", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton120.setText(QtGui.QApplication.translate("Dialog", "2 hour", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClear.setText(QtGui.QApplication.translate("Dialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))

