from PySide.QtCore import *
from PySide.QtGui import *
from classes_becash import *
from report_order_class import Ui_Dialog

class DialogOrders(QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogOrders, self).__init__()
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.setupUi(self)
        self.order =' ORDER by `row_id` DESC'
        self.completamSelectul()
        # self.tableWidget.cellDoubleClicked.connect(self.saveCellChange)
        self.bClose.clicked.connect(self.accept)
        self.bChangeStatus.clicked.connect(self.changeStatus)

    def changeStatus(self):

        if int(self.tableWidget.item(self.tableWidget.currentRow(),15).text()  ):
            QtGui.QMessageBox.warning(self, appName, "Already synced!, Cannot change state")
            return

        quit_msg = "Change status of order "+ self.tableWidget.item(self.tableWidget.currentRow(),0).text()  +" ?"
        reply = QtGui.QMessageBox.question(self, 'Confirm', quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            if self.tableWidget.item(self.tableWidget.currentRow(),16).text()=='Valid':
                query("UPDATE orders SET state=66, sync=1,stoptime="+str(int(time.time()))+" WHERE row_id="+ self.tableWidget.item(self.tableWidget.currentRow(),0).text())
                self.tableWidget.setItem(self.tableWidget.currentRow(),16,QtGui.QTableWidgetItem('Err'))
            else:
                query("UPDATE orders SET state=0, sync=0 WHERE row_id="+ self.tableWidget.item(self.tableWidget.currentRow(),0).text())
                self.tableWidget.setItem(self.tableWidget.currentRow(),7,QtGui.QTableWidgetItem('Valid'))


    def completamSelectul(self):
        records = query("SELECT *,operator as operatorUUID,(SELECT name FROM users WHERE uuid=operatorUUID),(SELECT name FROM tables WHERE id=orders.table_id) AS tableName FROM orders WHERE stoptime IS NOT NULL "+self.order)

        shift1  =(0, "----", int(time.time()),"",0,"")

        self.tableWidget.setRowCount(len(records)+1000)
        row =0
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,70)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,120)
        self.tableWidget.setColumnWidth(5,120)
        self.tableWidget.setColumnWidth(6,50)
        self.tableWidget.setColumnWidth(7,50)
        self.tableWidget.setColumnWidth(8,50)
        self.tableWidget.setColumnWidth(9,50)
        self.tableWidget.setColumnWidth(10,50)
        self.tableWidget.setColumnWidth(11,50)
        self.tableWidget.setColumnWidth(12,70)
        self.tableWidget.setColumnWidth(13,70)
        self.tableWidget.setColumnWidth(14,70)
        self.tableWidget.setColumnWidth(15,70)
        self.tableWidget.setColumnWidth(16,70)


        if records:
            for record in records:

                ####adaugam  rind  cu  SHIFT  daca este nevoie
                if record[3] < shift1[2]:
                    if shift1[2] !=int(time.time()):
                        mesaj = "Closed"
                        user = shift1[5]
                    else:
                        mesaj = "Curent"
                        user =""
                    shift1 = query("SELECT *,(SELECT name FROM users WHERE uuid=shift.user) AS operatorName FROM shift WHERE att < "+  str(shift1[2]) +" ORDER BY id DESC LIMIT 1")
                    if len(shift1):
                        shift1 = shift1[0]
                    else:
                        shift1 = (0, "----", 0, "", 0, "")
                    self.tableSetTextLeft(self.tableWidget,row,0,mesaj)  # NUmele la operator
                    self.tableSetTextLeft(self.tableWidget,row,1,user)  # NUmele la operator
                    self.tableSetTextRight(self.tableWidget, row, 4, time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(shift1[2])))  ##data  inceputului  jocului
                    row += 1

                # print(record)
                #colonitsele cu ordere
                self.tableSetTextRight(self.tableWidget,row,0,record[7])  # ID
                self.tableSetTextLeft(self.tableWidget,row,1,record[0])  #uuid
                self.tableSetTextLeft(self.tableWidget,row,2,record[19])  #table
                self.tableSetTextLeft(self.tableWidget, row, 3, record[18])  # NUmele la operator
                self.tableSetTextRight(self.tableWidget,row,4,time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(record[3])))     ##data  inceputului  jocului
                self.tableSetTextRight(self.tableWidget,row,5,time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(record[3])))     ##data  sfirshitului  jocului
                self.tableSetTextLeft(self.tableWidget, row, 6, record[5])##payed
                self.tableSetTextLeft(self.tableWidget, row, 7, record[9])##price1
                self.tableSetTextLeft(self.tableWidget, row, 8, record[10])##price2
                self.tableSetTextLeft(self.tableWidget, row, 9, record[11])##price3
                self.tableSetTextRight(self.tableWidget,row,10,record[12])      ##summa  brutto
                self.tableSetTextLeft(self.tableWidget, row, 11, record[13])#card
                self.tableSetTextLeft(self.tableWidget, row, 12, record[14])#percent
                self.tableSetTextLeft(self.tableWidget,row,13,record[15])   #discoutul
                self.tableSetTextLeft(self.tableWidget,row,14,record[16])   #spre actitare
                self.tableSetTextLeft(self.tableWidget,row,15,record[8])   #sincronizarea

                if record[15]==0:                                  ###valid  sau nevalid
                    self.tableSetTextLeft(self.tableWidget,row,16,'Valid')
                else:
                    self.tableSetTextLeft(self.tableWidget,row,16,'Err')
                row +=1
        self.tableWidget.setRowCount(row)
        return


    def setData(self, index, value):
        #print ("um clasul principal", index.row(), index.column(), value)
        self.sqlSaveByID(index.row(),index.column(),value)

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
