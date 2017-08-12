# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_change_class.ui'
#
# Created: Thu Feb  9 22:36:10 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1089, 689)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 1071, 671))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(650, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(10000, 6000))
        self.groupBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 401, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewButton = QtGui.QPushButton(self.layoutWidget)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.printButton = QtGui.QPushButton(self.layoutWidget)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout_2.addWidget(self.printButton)
        self.clearButton = QtGui.QPushButton(self.layoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_2.addWidget(self.clearButton)
        self.bClose = QtGui.QPushButton(self.layoutWidget)
        self.bClose.setObjectName("bClose")
        self.horizontalLayout_2.addWidget(self.bClose)
        self.layoutWidget1 = QtGui.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(870, 10, 184, 48))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayoutDate = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayoutDate.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutDate.setObjectName("gridLayoutDate")
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayoutDate.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayoutDate.addWidget(self.label_2, 1, 0, 1, 1)
        self.reportPreview = QtWebKit.QWebView(self.groupBox)
        self.reportPreview.setGeometry(QtCore.QRect(10, 70, 1051, 591))
        self.reportPreview.setUrl(QtCore.QUrl("about:blank"))
        self.reportPreview.setObjectName("reportPreview")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.bClose, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Shift report", None, QtGui.QApplication.UnicodeUTF8))
        self.previewButton.setText(QtGui.QApplication.translate("Dialog", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.printButton.setText(QtGui.QApplication.translate("Dialog", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("Dialog", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.bClose.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "From:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "To:", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
