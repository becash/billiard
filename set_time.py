import time
from PySide import QtGui
from PySide.QtCore import *
from PySide.QtGui import *

from functions import  *
from time_set_class import Ui_Dialog


class DialogSetTime(QDialog, Ui_Dialog):
    logging.info('-----DialogSetTime-----')
    def __init__(self,id,mainWindow):
        super(DialogSetTime, self).__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.maindindow = mainWindow
        self.setWindowTitle("Dialog.")
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.signals()
        self.id =id
        self.setVariables()



    def signals(self):

        #conectam  signalele
        self.pushButton015.clicked.connect(lambda:self.buttonClick(900))
        self.pushButton030.clicked.connect(lambda:self.buttonClick(1800))
        self.pushButton045.clicked.connect(lambda:self.buttonClick(2700))
        self.pushButton060.clicked.connect(lambda:self.buttonClick(3600))
        self.pushButton120.clicked.connect(lambda:self.buttonClick(7200))
        self.pushButton999.clicked.connect(lambda:self.buttonClick(None))
        self.pushButtonClear.clicked.connect(self.clearTime)
        self.pushButtonOK.clicked.connect(self.saveTime)


    def buttonClick(self,arg):
        logging.info('-----DialogSetTime-----')
        if not arg:
            self.addToTime = 100000#  o cifra mare,  tipa nelimitat

###########################

            self.saveTime()
        else:
            self.remain= self.remain + arg
            self.addToTime = self.addToTime + arg
            self.timeRemain.setText(time.strftime("%H:%M", time.gmtime(self.remain)))
        if self.addToTime<99000 :
            finishTime = int(time.time()+ self.addToTime)
            summa =0
            while finishTime > time.time():
                pretulMinutei = self.tableDetails[8+getPeriodByTime(finishTime)]
                summa+=pretulMinutei
                finishTime-=60
            self.priceTotal.setText('~'+str(summa))

    def clearTime(self):
            self.remain= 0
            self.addToTime = 0
            self.timeRemain.setText(time.strftime("%H:%M", time.gmtime(0)))
            self.priceTotal.setText("0")




    def setVariables(self):
        logging.info('-----setVariables-----')
        self.orderDetails =query("SELECT * FROM orders WHERE (stoptime is NULL or stoptime >  "+ str(time.time()) +" ) AND table_id='"+ (str(self.id)[0][0])[0][0]+"'" )
        if len(self.orderDetails):
            self.timeStart = self.orderDetails[0][3]
            self.timeEnd =   self.orderDetails[0][4]
            self.perMinute1=  self.orderDetails[0][9]
            self.perMinute2=  self.orderDetails[0][10]
            self.perMinute3=  self.orderDetails[0][11]
        else:
            self.tableDetails =query("SELECT * FROM tables WHERE id="+ str(self.id))[0]
            self.timeStart = time.time()
            self.timeEnd = 0
            self.perMinute1= self.tableDetails[8]
            self.perMinute2= self.tableDetails[9]
            self.perMinute3= self.tableDetails[10]

        self.timePrice1.setText(str(self.perMinute1))
        self.timePrice2.setText(str(self.perMinute2))
        self.timePrice3.setText(str(self.perMinute3))
        if self.timeEnd:
            self.remain = self.timeEnd - time.time()
            self.priceTotal.setText("= "+str(int((self.timeEnd - self.timeStart)/60)*self.perMinute ))
        else:
            self.remain = 0
            self.priceTotal.setText("=0")
        self.timeRemain.setText(time.strftime("%H:%M", time.gmtime(self.remain)))
        self.addToTime =0
        self.timePrice1.setText(str(self.perMinute1))
        self.timePrice2.setText(str(self.perMinute2))
        self.timePrice3.setText(str(self.perMinute3))


    def saveTime(self):
        logging.info('-----saveTime-----')
        if self.addToTime :
            tableDetails= query("SELECT uuid FROM orders WHERE (stoptime is NULL or stoptime >  "+ str(time.time()) +" )  AND table_id='"+ str(self.id)+"' ORDER BY row_id  DESC LIMIT 1")
            if len(tableDetails):
                query("UPDATE orders SET stoptime=stoptime+"+ str(self.addToTime )+ " WHERE row_id ="+tableDetails[8])
                row_id = tableDetails[8]
            else:
                # logging.info(self.userInfo)
                if self.maindindow.receivePayments:
                    summ="0" ## nu este achitat
                else:
                    summ="9" # achitat

                if self.maindindow.tribarSyncChech:
                    sync="0" ## nu este achitat
                else:
                    sync="1" # achitat



                row_id =query("INSERT INTO `orders` (`uuid`, `table_id`,  `at`, `stoptime`,  `price1`,`price2`,`price3`, `payed`, `operator`, `state`,`sync`)"+
                      " VALUES ('"+getNewSID() +"', '"+ str(self.id)  +"',  '"+ str(time.time()) +"', '" +str(time.time()+ self.addToTime)+
                              "', '"+ self.timePrice1.text() +"', '"+ self.timePrice2.text() +"', '"+ self.timePrice3.text() +"', '"+summ+"', '"+self.maindindow.userInfo[0]+"', 0, '"+sync+"');")

                ##punem pretul, total pentru joaca
                order = query("SELECT * FROM orders  WHERE row_id=" + str(row_id))[0]
                # print(order)

                query("UPDATE orders SET summ_brutto=" + str(getSummForGame(order)) + " WHERE row_id=" + str(row_id))

            if self.addToTime ==100000:
                 query("UPDATE orders SET stoptime = NULL WHERE row_id ="+str(row_id ))

            self.accept()
