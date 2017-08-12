from PySide.QtGui import *

from functions import *
from settings_class import Ui_Dialog


class DialogSettings(QDialog, Ui_Dialog):
    def __init__(self):
        super(DialogSettings, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('images/circle_red.png'))
        self.bSave.clicked.connect(self.saveSettings)
        self.saveDays.setInputMask("0000")
        self.crearOldOrders.clicked.connect(clearOldOrders)
        self.completamSetarile()

    def completamSetarile(self):
        programSettings = query("SELECT * FROM settings")
        for sett in programSettings:
            # logging.info(sett)
            if sett[0] == 10:
                self.productUUID.setText(sett[2])
            if sett[0] == 20:
                self.tableUUID.setText(sett[2])
            if sett[0] == 30:
                self.companyName.setText(sett[2])
            if sett[0] == 31:
                self.fiscalcode.setText(sett[2])
            if sett[0] == 32:
                self.adress.setText(sett[2])
            if sett[0] == 33:
                self.checkMessage.setText(sett[2])
            if sett[0] == 34:
                self.emailSenderName.setText(sett[2])
            if sett[0] == 35:
                self.emailSenderPass.setText(sett[2])
            if sett[0] == 36:
                self.emailReceiver.setText(sett[2])
            if sett[0] == 40:
                self.saveDays.setText(sett[2])
            if sett[0] == 50:
                self.autoclearStart.setChecked(int(sett[2]))
            if sett[0] == 51:
                self.rollPrinterName.setText(sett[2])
            if sett[0] == 52:
                self.rollPrinterExemplars.setText(sett[2])
            if sett[0] == 53:
                self.kkmProductName.setText(sett[2])
            if sett[0] == 54:
                self.kkmPath_FileName.setText(sett[2])
            if sett[0] == 55:
                self.kkmNomerNalogovoiGruppi.setText(sett[2])
            if sett[0] == 56:
                self.kkmNomerSectii.setText(sett[2])
            if sett[0] == 57:
                self.kkmZreport.setChecked(int(sett[2]))

            if sett[0] == 61:
                self.triobarSyncShifts.setChecked(int(sett[2]))
            if sett[0] == 62:
                self.triobarSyncCheck.setChecked(int(sett[2]))
            if sett[0] == 65:
                self.shiftFunctions.setChecked(int(sett[2]))

            if sett[0] == 66:
                self.receivePayments.setChecked(int(sett[2]))
            if sett[0] == 67:
                self.dbClear.setChecked(int(sett[2]))

            if sett[0] == 70:
                self.linePeriod1.setText(sett[2])
            if sett[0] == 80:
                self.linePeriod2.setText(sett[2])
            if sett[0] == 90:
                self.linePeriod3.setText(sett[2])
            if sett[0] == 94:
                self.extendedShiftReportPrint.setChecked(int(sett[2]))
            if sett[0] == 95:
                self.extendedShiftReportMail.setChecked(int(sett[2]))

    def saveSettings(self):
        if (int(settingsConfig.value("FirebirdSettings/EnableFirebird"))):
            try:
                queryFirebird('SELECT "UUID" FROM "Products" WHERE "UUID"= \'' + self.productUUID.text() + '\'')[0]
            except:
                QMessageBox.warning(self, appName, "Product Triobar UUID not exist!")
                return

        query("UPDATE settings SET value='" + self.productUUID.text() + "' WHERE  id='10'")

        if (int(settingsConfig.value("FirebirdSettings/EnableFirebird"))):
            try:
                queryFirebird('SELECT "UUID" FROM "Tables" WHERE "TableNo"= \'' + self.tableUUID.text() + '\'')[0]
            except:
                QMessageBox.warning(self, appName, "Table Triobar (TableNo) not exist!")
                return

        query("UPDATE settings SET value='" + self.tableUUID.text() + "' WHERE  id='20'")
        query("UPDATE settings SET value='" + self.companyName.text() + "' WHERE  id='30'")
        query("UPDATE settings SET value='" + self.fiscalcode.text() + "' WHERE  id='31'")
        query("UPDATE settings SET value='" + self.adress.text() + "' WHERE  id='32'")
        query("UPDATE settings SET value='" + self.checkMessage.text() + "' WHERE  id='33'")
        query("UPDATE settings SET value='" + self.emailSenderName.text() + "' WHERE  id='34'")
        query("UPDATE settings SET value='" + self.emailSenderPass.text() + "' WHERE  id='35'")
        query("UPDATE settings SET value='" + self.emailReceiver.text() + "' WHERE  id='36'")
        query("UPDATE settings SET value='" + self.saveDays.text() + "' WHERE  id='40'")
        query("UPDATE settings SET value='" + str(int(self.autoclearStart.isChecked())) + "' WHERE  id='50'")
        query("UPDATE settings SET value='" + self.rollPrinterName.text() + "' WHERE  id='51'")
        query("UPDATE settings SET value='" + self.rollPrinterExemplars.text() + "' WHERE  id='52'")
        query("UPDATE settings SET value='" + self.kkmProductName.text() + "' WHERE  id='53'")
        query("UPDATE settings SET value='" + self.kkmPath_FileName.text() + "' WHERE  id='54'")
        query("UPDATE settings SET value='" + self.kkmNomerNalogovoiGruppi.text() + "' WHERE  id='55'")
        query("UPDATE settings SET value='" + self.kkmNomerSectii.text() + "' WHERE  id='56'")
        query("UPDATE settings SET value='" + str(int(self.kkmZreport.isChecked())) + "' WHERE  id='57'")

        query("UPDATE settings SET value='" + str(int(self.triobarSyncShifts.isChecked())) + "' WHERE  id='61'")
        query("UPDATE settings SET value='" + str(int(self.triobarSyncCheck.isChecked())) + "' WHERE  id='62'")
        query("UPDATE settings SET value='" + str(int(self.shiftFunctions.isChecked())) + "' WHERE  id='65'")
        query("UPDATE settings SET value='" + str(int(self.receivePayments.isChecked())) + "' WHERE  id='66'")
        query("UPDATE settings SET value='" + str(int(self.dbClear.isChecked())) + "' WHERE  id='67'")

        query("UPDATE settings SET value='" + self.linePeriod1.text() + "' WHERE  id='70'")
        query("UPDATE settings SET value='" + self.linePeriod2.text() + "' WHERE  id='80'")
        query("UPDATE settings SET value='" + self.linePeriod3.text() + "' WHERE  id='90'")
        query("UPDATE settings SET value='" + str(int(self.extendedShiftReportPrint.isChecked())) + "' WHERE  id='94'")
        query("UPDATE settings SET value='" + str(int(self.extendedShiftReportMail.isChecked())) + "' WHERE  id='95'")
        QMessageBox.warning(self, appName, "Restart application to apply changes")
        self.accept()
