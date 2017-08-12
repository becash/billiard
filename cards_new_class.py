# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cards_new_class.ui'
#
# Created: Thu Feb  9 22:36:11 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 236)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(332, 200))
        Dialog.setMaximumSize(QtCore.QSize(332, 355))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 158, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bOk = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.bOk.setObjectName("bOk")
        self.horizontalLayout.addWidget(self.bOk)
        self.bCancel = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.bCancel.setObjectName("bCancel")
        self.horizontalLayout.addWidget(self.bCancel)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 311, 191))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 271, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.prescurtarea = QtGui.QLabel(self.gridLayoutWidget)
        self.prescurtarea.setMargin(10)
        self.prescurtarea.setObjectName("prescurtarea")
        self.gridLayout.addWidget(self.prescurtarea, 2, 0, 1, 1)
        self.fullname = QtGui.QLabel(self.gridLayoutWidget)
        self.fullname.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fullname.setMargin(10)
        self.fullname.setObjectName("fullname")
        self.gridLayout.addWidget(self.fullname, 1, 0, 1, 1)
        self.discount = QtGui.QLineEdit(self.gridLayoutWidget)
        self.discount.setObjectName("discount")
        self.gridLayout.addWidget(self.discount, 2, 1, 1, 1)
        self.active = QtGui.QCheckBox(self.gridLayoutWidget)
        self.active.setObjectName("active")
        self.gridLayout.addWidget(self.active, 3, 1, 1, 1)
        self.onwerNameLine = QtGui.QLineEdit(self.gridLayoutWidget)
        self.onwerNameLine.setObjectName("onwerNameLine")
        self.gridLayout.addWidget(self.onwerNameLine, 0, 1, 1, 1)
        self.cardNumber = QtGui.QLineEdit(self.gridLayoutWidget)
        self.cardNumber.setObjectName("cardNumber")
        self.gridLayout.addWidget(self.cardNumber, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.bCancel, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.onwerNameLine, self.cardNumber)
        Dialog.setTabOrder(self.cardNumber, self.discount)
        Dialog.setTabOrder(self.discount, self.active)
        Dialog.setTabOrder(self.active, self.bOk)
        Dialog.setTabOrder(self.bOk, self.bCancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Card edit", None, QtGui.QApplication.UnicodeUTF8))
        self.bOk.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.bCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Card data", None, QtGui.QApplication.UnicodeUTF8))
        self.prescurtarea.setText(QtGui.QApplication.translate("Dialog", "Discount %", None, QtGui.QApplication.UnicodeUTF8))
        self.fullname.setText(QtGui.QApplication.translate("Dialog", "Card number", None, QtGui.QApplication.UnicodeUTF8))
        self.active.setText(QtGui.QApplication.translate("Dialog", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "    Owner", None, QtGui.QApplication.UnicodeUTF8))

