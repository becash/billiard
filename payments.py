from PySide.QtCore import *
from PySide.QtGui import *
from report_payments_class import Ui_Dialog

from classes_becash import *


class DialogPayTable(QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogPayTable, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.completamSelectul()
        self.tableWidget.cellDoubleClicked.connect(self.saveCellChange)
        self.bClose.clicked.connect(self.accept)

    def completamSelectul(self):
        sql = "SELECT p.id,o.row_id,u.name,p.sum,t.salon,t.name,o.at,o.stoptime,c.owner,o.disc_percent,p.cash_reg,pt.name  \
                FROM payments p\
                LEFT JOIN orders o ON p.parent_order = o.uuid \
                LEFT JOIN tables t ON o.table_id = t.id \
                LEFT JOIN users u ON o.operator = u.uuid \
                LEFT JOIN cards c ON o.disc_card = c.id\
                LEFT JOIN payments_types pt ON p.payment_typ = pt.id\
                "
        records = query(sql)

        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,50)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,50)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.setColumnWidth(6,120)
        self.tableWidget.setColumnWidth(7,120)
        self.tableWidget.setColumnWidth(8,50)
        self.tableWidget.setColumnWidth(9,120)
        self.tableWidget.setColumnWidth(10,50)
        self.tableWidget.setColumnWidth(11,50)
        self.tableWidget.setColumnWidth(12,90)

        row =0
        if records:
            for record in records:
                # print(record)
                logging.info(record)
                self.tableSetTextRight(self.tableWidget,row,0,record[0])  #id
                self.tableSetTextRight(self.tableWidget,row,1,record[1])  #order
                self.tableSetTextLeft(self.tableWidget,row,2,record[2])#opetarr
                self.tableSetTextRight(self.tableWidget,row,3,record[3])#summa
                self.tableSetTextLeft(self.tableWidget,row,4,salons[record[4]])#sala
                self.tableSetTextLeft(self.tableWidget, row, 5, record[5])  # masa
                self.tableSetTextRight(self.tableWidget,row,6,time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(record[6])))  ##start
                self.tableSetTextRight(self.tableWidget,row,7,time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(record[7])))  ##finish
                self.tableSetTextRight(self.tableWidget,row,8,    str((record[7]-record[6])/60) ) #minute
                self.tableSetTextLeft(self.tableWidget, row, 9, record[8])  # qwner
                self.tableSetTextRight(self.tableWidget, row, 10, record[9])  # %
                self.tableSetTextRight(self.tableWidget, row, 11, record[10])  # cash register
                self.tableSetTextLeft(self.tableWidget, row, 12, record[11])  # cash
                row =row +1
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
        dialog.lineEdit.setText(str(userData[0][4]))
        dialog.userLevel.setCurrentIndex(int(userData[0][5]))
        dialog.checkBox.setChecked(int(userData[0][6]))
        dialog.controlerOFF.setText(str(userData[0][7]))
        dialog.controlerON.setText(str(userData[0][8]))

        if dialog.exec_():
            self.completamSelectul()
        #self.sqlSaveByID(arg.row(),arg.column(),arg.text())


    def deleteUser(self):
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

    def tableSetTextLeft(self,tabela,rind,coloana,text):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignLeft)
        tabela.setItem(rind, coloana, item)
        tabela.item(rind, coloana).setText(str(text))


    def tableSetTextRight(self,tabela,rind,coloana,text):
        item = QTableWidgetItem()
        item.setTextAlignment(Qt.AlignRight)
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
        self.bCancel.clicked.connect(self.reject)
        self.bDelete.clicked.connect(self.validateNewUserForm)


    def validateNewUserForm(self):

        if len(str(self.userNameLine.text())) > 1 and len(str(query("SELECT * FROM tables WHERE name='"+ self.userNameLine.text()+"'"))):
            if len(str(self.uuid.text())):
                query("UPDATE tables SET name='"+ self.userNameLine.text()+ "', salon='"+
                      str(self.userLevel.currentIndex())+ "', `order`='"+self.prescurtarea_2.text() + "', price='"+
                      self.lineEdit.text()+ "',enable='"+ str(int(self.checkBox.isChecked())) +"', `com_off`='"+
                      self.controlerOFF.text()+"', `com_on`='"+self.controlerON.text()+"'  WHERE uuid='"+ str(self.uuid.text()) +"'")
                self.accept()
            else:
                query("INSERT INTO tables VALUES (NULL ,'"+getNewSID() + "','"+ self.userNameLine.text()+ "','"+
                      self.prescurtarea_2.text()+ "','"+self.lineEdit.text() + "','"+
                      str(self.userLevel.currentIndex())+ "','"+ str(int(self.checkBox.isChecked())) +"','"+self.controlerOFF.text()+"','"+self.controlerON.text()+"')")
                self.accept()
        else:
            logging.info("verificati forma")


