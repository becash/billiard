# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_class.ui'
#
# Created: Thu Feb  9 22:36:06 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(688, 501)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 681, 491))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(300, 300))
        self.widget.setMaximumSize(QtCore.QSize(1600, 800))
        self.widget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.widget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtGui.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 656, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableUUID = QtGui.QLineEdit(self.gridLayoutWidget)
        self.tableUUID.setObjectName("tableUUID")
        self.gridLayout.addWidget(self.tableUUID, 4, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 15, 0, 1, 1)
        self.emailReceiver = QtGui.QLineEdit(self.gridLayoutWidget)
        self.emailReceiver.setObjectName("emailReceiver")
        self.gridLayout.addWidget(self.emailReceiver, 21, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 17, 0, 1, 1)
        self.kkmNomerNalogovoiGruppi = QtGui.QLineEdit(self.gridLayoutWidget)
        self.kkmNomerNalogovoiGruppi.setObjectName("kkmNomerNalogovoiGruppi")
        self.gridLayout.addWidget(self.kkmNomerNalogovoiGruppi, 24, 2, 1, 1)
        self.rollPrinterExemplars = QtGui.QLineEdit(self.gridLayoutWidget)
        self.rollPrinterExemplars.setObjectName("rollPrinterExemplars")
        self.gridLayout.addWidget(self.rollPrinterExemplars, 17, 2, 1, 1)
        self.label_20 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_20.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 9, 0, 1, 1)
        self.kkmProductName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.kkmProductName.setObjectName("kkmProductName")
        self.gridLayout.addWidget(self.kkmProductName, 23, 2, 1, 1)
        self.checkMessage = QtGui.QLineEdit(self.gridLayoutWidget)
        self.checkMessage.setObjectName("checkMessage")
        self.gridLayout.addWidget(self.checkMessage, 18, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_14.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 20, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_22.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 18, 0, 1, 1)
        self.fiscalcode = QtGui.QLineEdit(self.gridLayoutWidget)
        self.fiscalcode.setObjectName("fiscalcode")
        self.gridLayout.addWidget(self.fiscalcode, 9, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_21.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 10, 0, 1, 1)
        self.adress = QtGui.QLineEdit(self.gridLayoutWidget)
        self.adress.setObjectName("adress")
        self.gridLayout.addWidget(self.adress, 10, 2, 1, 1)
        self.productUUID = QtGui.QLineEdit(self.gridLayoutWidget)
        self.productUUID.setObjectName("productUUID")
        self.gridLayout.addWidget(self.productUUID, 3, 2, 1, 1)
        self.companyName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.companyName.setObjectName("companyName")
        self.gridLayout.addWidget(self.companyName, 8, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_11.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 16, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_17.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 23, 0, 1, 1)
        self.rollPrinterName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.rollPrinterName.setObjectName("rollPrinterName")
        self.gridLayout.addWidget(self.rollPrinterName, 16, 2, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_13.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 19, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_15.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 21, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_16.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 22, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_18.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 24, 0, 1, 1)
        self.kkmNomerSectii = QtGui.QLineEdit(self.gridLayoutWidget)
        self.kkmNomerSectii.setObjectName("kkmNomerSectii")
        self.gridLayout.addWidget(self.kkmNomerSectii, 25, 2, 1, 1)
        self.emailSenderPass = QtGui.QLineEdit(self.gridLayoutWidget)
        self.emailSenderPass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.emailSenderPass.setEchoMode(QtGui.QLineEdit.Password)
        self.emailSenderPass.setObjectName("emailSenderPass")
        self.gridLayout.addWidget(self.emailSenderPass, 20, 2, 1, 1)
        self.saveDays = QtGui.QLineEdit(self.gridLayoutWidget)
        self.saveDays.setAcceptDrops(False)
        self.saveDays.setToolTip("")
        self.saveDays.setStatusTip("")
        self.saveDays.setWhatsThis("")
        self.saveDays.setAccessibleName("")
        self.saveDays.setInputMask("")
        self.saveDays.setMaxLength(4)
        self.saveDays.setObjectName("saveDays")
        self.gridLayout.addWidget(self.saveDays, 5, 2, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.linePeriod1 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.linePeriod1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.linePeriod1.setInputMask("")
        self.linePeriod1.setMaxLength(2)
        self.linePeriod1.setObjectName("linePeriod1")
        self.horizontalLayout.addWidget(self.linePeriod1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.linePeriod2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.linePeriod2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.linePeriod2.setInputMask("")
        self.linePeriod2.setMaxLength(2)
        self.linePeriod2.setObjectName("linePeriod2")
        self.horizontalLayout.addWidget(self.linePeriod2)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.linePeriod3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.linePeriod3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.linePeriod3.setInputMask("")
        self.linePeriod3.setMaxLength(2)
        self.linePeriod3.setObjectName("linePeriod3")
        self.horizontalLayout.addWidget(self.linePeriod3)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout, 15, 2, 1, 1)
        self.emailSenderName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.emailSenderName.setObjectName("emailSenderName")
        self.gridLayout.addWidget(self.emailSenderName, 19, 2, 1, 1)
        self.kkmPath_FileName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.kkmPath_FileName.setObjectName("kkmPath_FileName")
        self.gridLayout.addWidget(self.kkmPath_FileName, 22, 2, 1, 1)
        self.label_19 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_19.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 25, 0, 1, 1)
        self.kkmZreport = QtGui.QCheckBox(self.gridLayoutWidget)
        self.kkmZreport.setObjectName("kkmZreport")
        self.gridLayout.addWidget(self.kkmZreport, 22, 3, 1, 1)
        self.crearOldOrders = QtGui.QPushButton(self.gridLayoutWidget)
        self.crearOldOrders.setObjectName("crearOldOrders")
        self.gridLayout.addWidget(self.crearOldOrders, 15, 3, 1, 1)
        self.autoclearStart = QtGui.QCheckBox(self.gridLayoutWidget)
        self.autoclearStart.setObjectName("autoclearStart")
        self.gridLayout.addWidget(self.autoclearStart, 16, 3, 1, 1)
        self.shiftFunctions = QtGui.QCheckBox(self.gridLayoutWidget)
        self.shiftFunctions.setObjectName("shiftFunctions")
        self.gridLayout.addWidget(self.shiftFunctions, 9, 3, 1, 1)
        self.receivePayments = QtGui.QCheckBox(self.gridLayoutWidget)
        self.receivePayments.setObjectName("receivePayments")
        self.gridLayout.addWidget(self.receivePayments, 5, 3, 1, 1)
        self.triobarSyncCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.triobarSyncCheck.setObjectName("triobarSyncCheck")
        self.gridLayout.addWidget(self.triobarSyncCheck, 4, 3, 1, 1)
        self.triobarSyncShifts = QtGui.QCheckBox(self.gridLayoutWidget)
        self.triobarSyncShifts.setObjectName("triobarSyncShifts")
        self.gridLayout.addWidget(self.triobarSyncShifts, 3, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.dbClear = QtGui.QCheckBox(self.gridLayoutWidget)
        self.dbClear.setObjectName("dbClear")
        self.gridLayout.addWidget(self.dbClear, 25, 3, 1, 1)
        self.extendedShiftReportPrint = QtGui.QCheckBox(self.gridLayoutWidget)
        self.extendedShiftReportPrint.setObjectName("extendedShiftReportPrint")
        self.gridLayout.addWidget(self.extendedShiftReportPrint, 18, 3, 1, 1)
        self.extendedShiftReportMail = QtGui.QCheckBox(self.gridLayoutWidget)
        self.extendedShiftReportMail.setObjectName("extendedShiftReportMail")
        self.gridLayout.addWidget(self.extendedShiftReportMail, 19, 3, 1, 1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.widget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bSave = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.bSave.setObjectName("bSave")
        self.verticalLayout.addWidget(self.bSave)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.productUUID, self.tableUUID)
        Dialog.setTabOrder(self.tableUUID, self.saveDays)
        Dialog.setTabOrder(self.saveDays, self.companyName)
        Dialog.setTabOrder(self.companyName, self.fiscalcode)
        Dialog.setTabOrder(self.fiscalcode, self.adress)
        Dialog.setTabOrder(self.adress, self.linePeriod1)
        Dialog.setTabOrder(self.linePeriod1, self.linePeriod2)
        Dialog.setTabOrder(self.linePeriod2, self.linePeriod3)
        Dialog.setTabOrder(self.linePeriod3, self.rollPrinterName)
        Dialog.setTabOrder(self.rollPrinterName, self.rollPrinterExemplars)
        Dialog.setTabOrder(self.rollPrinterExemplars, self.checkMessage)
        Dialog.setTabOrder(self.checkMessage, self.emailSenderName)
        Dialog.setTabOrder(self.emailSenderName, self.emailSenderPass)
        Dialog.setTabOrder(self.emailSenderPass, self.emailReceiver)
        Dialog.setTabOrder(self.emailReceiver, self.kkmPath_FileName)
        Dialog.setTabOrder(self.kkmPath_FileName, self.kkmProductName)
        Dialog.setTabOrder(self.kkmProductName, self.kkmNomerNalogovoiGruppi)
        Dialog.setTabOrder(self.kkmNomerNalogovoiGruppi, self.kkmNomerSectii)
        Dialog.setTabOrder(self.kkmNomerSectii, self.bSave)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Time periods", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Roll printer exemplars", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog", "Fiscal code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "Gmail sender Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Dialog", "Check message", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Dialog", "Adress", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Roll Printer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Save Order (Days)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog", "KKM Product name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "Gmail sender EMAIL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog", "Rport receiver EMAIL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog", "KKM path&filename", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog", "KKM номер налоговой группы", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Triobar Table (TableNo)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Company name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Per 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Per 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Per 3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog", "KKM номер секции", None, QtGui.QApplication.UnicodeUTF8))
        self.kkmZreport.setText(QtGui.QApplication.translate("Dialog", "KKM Z report on shift close", None, QtGui.QApplication.UnicodeUTF8))
        self.crearOldOrders.setText(QtGui.QApplication.translate("Dialog", "Clear old orders", None, QtGui.QApplication.UnicodeUTF8))
        self.autoclearStart.setText(QtGui.QApplication.translate("Dialog", "Clear older order, on application start", None, QtGui.QApplication.UnicodeUTF8))
        self.shiftFunctions.setText(QtGui.QApplication.translate("Dialog", "Enable  Shifts Function", None, QtGui.QApplication.UnicodeUTF8))
        self.receivePayments.setText(QtGui.QApplication.translate("Dialog", "Accept  payments", None, QtGui.QApplication.UnicodeUTF8))
        self.triobarSyncCheck.setText(QtGui.QApplication.translate("Dialog", "Triobar Sync Check", None, QtGui.QApplication.UnicodeUTF8))
        self.triobarSyncShifts.setText(QtGui.QApplication.translate("Dialog", "Triobar Sync Shifts", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Triobar Product  UUID", None, QtGui.QApplication.UnicodeUTF8))
        self.dbClear.setText(QtGui.QApplication.translate("Dialog", "new DB", None, QtGui.QApplication.UnicodeUTF8))
        self.extendedShiftReportPrint.setText(QtGui.QApplication.translate("Dialog", "Extended Shift report to printer", None, QtGui.QApplication.UnicodeUTF8))
        self.extendedShiftReportMail.setText(QtGui.QApplication.translate("Dialog", "Extendet Shift report to mail", None, QtGui.QApplication.UnicodeUTF8))
        self.bSave.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

