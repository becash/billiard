from PySide.QtCore import *
from PySide.QtGui import *
from table_class import Ui_Dialog

from classes_becash import *


class DialogTable(QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogTable, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.order =' ORDER by `order`,`salon`'
        self.completamSelectul()
        self.tableWidget.cellDoubleClicked.connect(self.saveCellChange)

        #conectam  signalele
        # self.connect(self.select_, SIGNAL("currentIndexChanged(QString)"), self.selectChange)
        self.connect(self.bCancel, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(self.bDelete, SIGNAL("clicked()"), self.deleteUser)
        self.connect(self.bInsert, SIGNAL("clicked()"), self.dialogOpen)

    def completamSelectul(self):
        sql = "SELECT * FROM tables "+self.order
        records = query(sql)
        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,70)
        self.tableWidget.setColumnWidth(2,70)
        self.tableWidget.setColumnWidth(3,70)
        self.tableWidget.setColumnWidth(4,70)
        self.tableWidget.setColumnWidth(5,70)
        self.tableWidget.setColumnWidth(6,70)
        self.tableWidget.setColumnWidth(7,70)
        row =0
        if records:
            for record in records:
                self.tableWidget.blockSignals(True)
                self.tableSetText(self.tableWidget,row,0,record[2])
                self.tableSetText(self.tableWidget,row,1,salons[int(record[4])])
                self.tableSetText(self.tableWidget,row,2,record[3])
                self.tableSetText(self.tableWidget,row,3,record[5])
                self.tableSetText(self.tableWidget,row,4,record[8])
                self.tableSetText(self.tableWidget,row,5,record[9])
                self.tableSetText(self.tableWidget,row,6,record[10])
                self.tableWidget.blockSignals(False)
                row =row +1
        #self.tableWidget.itemChanged.connect(self.saveCellChange)
        return


    def setData(self, index, value):
        #print ("um clasul principal", index.row(), index.column(), value)
        self.sqlSaveByID(index.row(),index.column(),value)

    def saveCellChange(self,arg):
        dialog = Dialog2()
        userData =query("SELECT * FROM tables "+self.order+" LIMIT "+ str(self.tableWidget.currentRow()) +",1")
        #logging.info(userData)
        dialog.uuid.setText(str(userData[0][1]))
        dialog.userNameLine.setText(str(userData[0][2]))
        dialog.prescurtarea_2.setText(str(userData[0][3]))
        dialog.userLevel.setCurrentIndex(int(userData[0][4]))
        dialog.checkBox.setChecked(int(userData[0][5]))
        dialog.controlerOFF.setText(str(userData[0][6]))
        dialog.controlerON.setText(str(userData[0][7]))
        dialog.controlerName.setText(str(userData[0][11]))
        dialog.controlerUrl.setText(str(userData[0][12]))

        dialog.price1.setText(str(userData[0][8]))
        dialog.price2.setText(str(userData[0][9]))
        dialog.price3.setText(str(userData[0][10]))

        if dialog.exec_():
            self.completamSelectul()
        #self.sqlSaveByID(arg.row(),arg.column(),arg.text())


    def deleteUser(self):
        quit_msg = "Are you sure?"
        reply = QtGui.QMessageBox.question(self, 'Confirm', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            rowUuid =query("SELECT uuid FROM tables "+self.order+" LIMIT "+ str(self.tableWidget.currentRow()) +",1")
            query("DELETE FROM tables WHERE uuid = '"+ rowUuid[0][0] +"'")
            self.completamSelectul()




    def sqlSaveByID(self,row,cell,value):
        cellName =query("SELECT column_name FROM information_schema.columns WHERE table_name='tables'; ")[cell+1][0]
        rowUuid =query("SELECT uuid FROM users "+self.order+" LIMIT "+ str(row) +",1")
        query("UPDATE tables SET "+ str(cellName) + " = '"+ str(value)+"' WHERE uuid='"+ rowUuid[0][0] +"'")

        self.tableWidget.blockSignals(True)
        self.tableSetText(self.tableWidget,row,cell,value)
        self.tableWidget.blockSignals(False)

    def tableSetText(self,tabela,rind,coloana,text):
        item = QTableWidgetItem()
        tabela.setItem(rind, coloana, item)
        tabela.item(rind, coloana).setText(str(text))

################## Creare user nou
    def dialogOpen(self):
        dialog = Dialog2()
        if dialog.exec_():
            self.completamSelectul()

#######################################  DIALOGUL __NEW USER
from table_new_class import Ui_Dialog
class Dialog2(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.setupUi(self)
        self.userLevel.addItems(salons)
        self.connect(self.bCancel, SIGNAL("clicked()"), self, SLOT("reject()"))
        self.bDelete.clicked.connect(self.validateNewUserForm)


    def validateNewUserForm(self):
        if len(str(self.userNameLine.text())) > 1 and len(str(query("SELECT * FROM tables WHERE name='"+ self.userNameLine.text()+"'"))):
            if len(str(self.uuid.text())):
                query("UPDATE tables SET name='"+ self.userNameLine.text()+ "', salon='"+
                      str(self.userLevel.currentIndex())+ "', `order`='"+self.prescurtarea_2.text() +
                      "', price1='"+ self.price1.text()+ "', price2='"+self.price2.text()+ "', price3='"+self.price3.text()+
                      "',enable='"+ str(int(self.checkBox.isChecked())) +"', `com_off`='"+
                      self.controlerOFF.text()+"', `com_on`='"+self.controlerON.text()+
                      "', `controler`='"+self.controlerName.text()+"', `channel`='"+self.controlerUrl.text()+"'  WHERE uuid='"+ str(self.uuid.text()) +"'")
                QtGui.QMessageBox.warning(self, appName, "Restart application to apply changes")
                self.accept()
            else:
                query("INSERT INTO tables VALUES (NULL ,'"+getNewSID() + "','"+ self.userNameLine.text()+ "','"+self.prescurtarea_2.text()+
                      str(self.userLevel.currentIndex())+ "','"+ str(int(self.checkBox.isChecked())) +
                      "','"+self.controlerOFF.text()+"','"+self.controlerON.text()+"','"+self.price1.text()+"','"+self.price2.text()+"','"+self.price3.text()+"','"+
                      "','"+self.controlerName.text()+"','"+self.controlerUrl.text()+"')")
                QtGui.QMessageBox.warning(self, appName, "Restart application to apply changes")
                self.accept()
        else:
            logging.info("verificati forma")


