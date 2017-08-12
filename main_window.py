#!/usr/bin/env python

import sys
from PySide import QtGui
from classes_becash import FlowLayout ,WorkerThread
from functions import *

try:
    import objgraph
    objgraph.show_most_common_types()
except:
    pass
    import gc
############CLASELE LUI BECASH
from set_time import DialogSetTime
from pay import DialogPay
from orders import DialogOrders
from payments import DialogPayTable
from shift import DialogShiftTable
from change import DialogChange
from login import DialogLogin
from user import DialogUser
from cards import DialogCards
from table import DialogTable
from settings import DialogSettings
import printer
from cash_register import *




class MainWindow(QtGui.QMainWindow):
    sequenceNumber = 1
    windowList = []

    def __init__(self, fileName=None):
        super(MainWindow, self).__init__()
        self.init()

    def checkReqiurements(self):

        logging.info('-----checkReqiurements-----')

    ### MYSQL  comnectarea
        try:
            query("SHOW DATABASES")
        except mysql.Error:
            QtGui.QMessageBox.warning(self, appName, "MYSQL Database connection ERROR.")
            logging.warning("MYSQL Database connection ERROR.")
            sys.exit(98)
        ### Firebird  comnectarea
        if(int(settingsConfig.value("FirebirdSettings/EnableFirebird"))):
            try:
                queryFirebird('SELECT  * FROM "Orders"')
            except:
                logging.warning("FIREBIRD Database connection ERROR.200")
                QtGui.QMessageBox.warning(self, appName, "FIREBIRD Database connection ERROR.")
                sys.exit(98)



    def about(self):
        logging.info('-----about-----')

        QtGui.QMessageBox.about(self, "About "+appName,
                "<h1><b>Trio Billiard</b></h1><hr/> \
                Made by Trio Soft SRL<br/>\
                <a href='http://www.suav.biz/triobilliard'>Powered by SuavStudio (www.suav.biz)</a><br/>\
                <a href='http://www.triobar.md'>www.triobar.md</a><br/>\
                +(373)79424150<br/>\
                © 2015 Moldova, Chisinau<br/>")


    #####initializarea
    def init(self):
        logging.info('-----init MainwINDOW-----')
        self.setWindowIcon(QtGui.QIcon('images/circle_red.png'))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(appName+"  "+query("SELECT value FROM settings WHERE id=30")[0][0])
        self.tribarSyncShifts=int(query("SELECT value FROM settings WHERE id=61")[0][0])
        self.tribarSyncChech=int(query("SELECT value FROM settings WHERE id=62")[0][0])
        self.shiftFunctional=int(query("SELECT value FROM settings WHERE id=65")[0][0])
        self.receivePayments=int(query("SELECT value FROM settings WHERE id=66")[0][0])
        self.loggedIn = 0
        self.statusBarError = None
        # self.lightErrorDisplay = 1
        self.shiftCanClose = False
        self.userInfo =''
        self.statusBarErrorSet =''
        self.statusBar().setStyleSheet("QStatusBar{padding-left:8px;background:rgba(44, 62, 80,255);color:white; font-size:14px}")
        self.sallonOnly =None
        self.checkReqiurements()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
        self.isUntitled = True

                ###THREADING
        self.workerThread = WorkerThread(self)
        self.connect(self.workerThread, QtCore.SIGNAL("threadDone(QString)"), self.threadDone, QtCore.Qt.DirectConnection)

        self.flowLayout = None
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.statusUsername = QtGui.QLabel()

        self.createStatusBar()
        self.renderTables()
        #sheduller -- timer 1 secunda
        self.tryii =0
        self.lightCheck=1
        if self.loginAct.triggered.emit():
            self.resize(800,600)
            self.center()
            if int(query("SELECT value FROM settings WHERE id=50")[0][0]):
                clearOldOrders()
            timer = QtCore.QTimer(self)
            timer.timeout.connect(self.secondTimer)
            timer.setInterval(1000) ##  TIMERUL,  in mod  norlam trebuie sa fie 1000
            timer.start()
        try:
            self.getMemory()
        except:
            pass


    def getMemory(self):

        logging.info('---getMemory-----')
        objgraph.show_growth(limit=10)   # Start counting
        # logging.info(objgraph.count('QAction', objgraph.get_leaking_objects()))



    def processData(self):
        logging.info('-----precessData-----')
        self.workerThread.start()


    def threadDone(self, returnStatus):
        logging.info('-----threadDone-----')
        ##########  valrole care le returneaza TUREAD
        if returnStatus=="ok":
            self.statusBarErrorSet = None
        else:
            self.statusBarErrorSet="controler"


    def statusBarErrorSetFunc(self,err=False):
        logging.info('-----statusBarErrorSetFunc-----')
        if err==False:
                self.statusBar().showMessage("Ready")

        elif err=="controler":
                self.statusBar().showMessage("Warning! Light power management not working")

        elif err=="urlCcontrolerErr":
                self.statusBar().showMessage("Error: CONTROLER-"+ settingsConfig.value("URLcontroler/controlerUSR_WIfi_io_83") +" Not respond!! ")






    def center(self):
        logging.info('-----center-----')

        # logging.info("centering")
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):
        logging.info('-----clodeEvent-----')
        self.loginAct.triggered.emit()
        event.ignore()
                    #####pornit test  ca sa stingem toate luminile
        #        logging.info(self.workerThread.lightAll(0))
        #        time.sleep(2)       
        #        logging.info("Am ieshit din program")
        #        sys.exit(88)
        
            

    def secondTimer(self):
        logging.info('-----secondTimer-----')

        self.tryii = self.tryii +1
        self.statusbarTimer.setText(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(time.time())))
        #timerele peste  anumite intervale
        if not self.tryii % 4:
            ####pornim threading
            self.processData()
            self.statusBarErrorSetFunc(self.statusBarErrorSet)


        if not self.tryii % 20:
            self.checkReqiurements()

        if not self.tryii % 60:
            self.checkCurrentPeriod()
            gc.collect()


        if not self.tryii % 5:  ##### in mod mormal pune 7
            self.renderTables()
            try:
                self.getMemory()
            except:
                pass

    def renderTables(self):
        self.shiftCanCloseTemp = True
        logging.info('-----renderTables-----')
        flowLayout = FlowLayout()
        flowLayout.setSpacing(0)
        if int(settingsConfig.value("ComportSettings/EnableComport")):
            self.bytesToControler =' '  #   BITI care ii trimetem in comtroler
        if int(settingsConfig.value("URLcontroler/EnableURL")) or int(settingsConfig.value("USRprotocol/Enable"))  :
            self.bytesUrlChanels =[]

        tabs =query("SELECT * FROM tables WHERE enable =1 ORDER by `order`,`salon`")
        for tab in tabs:
            logging.info(tab)
            frRAME=self.rendOneTab(tab)
            if self.sallonOnly==None or self.sallonOnly==tab[4]:
                flowLayout.addWidget(frRAME)
         #cimpul principal
        tablesWin = QtGui.QWidget()
        tablesWin.setMinimumSize(970,600)
        tablesWin.setAutoFillBackground(True)
        p = tablesWin.palette()
        p.setColor(tablesWin.backgroundRole(), QtGui.QColor(44, 62, 80))
        tablesWin.setPalette(p)
        tablesWin.setLayout(flowLayout)
        self.setCentralWidget(tablesWin)
        self.shiftCanClose = self.shiftCanCloseTemp


        if int(settingsConfig.value("ComportSettings/EnableComport")):
            self.workerThread.bytesToControler = self.bytesToControler
        if int(settingsConfig.value("URLcontroler/EnableURL")) or int(settingsConfig.value("USRprotocol/Enable")):
            logging.info(self.bytesUrlChanels)
            self.workerThread.bytesUrlChanels = self.bytesUrlChanels


    ###decenam FIECARE MASA
    def rendOneTab(self,tabINfo):
        logging.info('-----renderOneTab-----')

        tabText ='<div style="font-size: 30px;margin:auto">'+str(tabINfo[2])+'</div><br/>--------------------------<div style="font-size:12px;margin:auto">'
        #logging.info(tabINfo)
        tableTab = QtGui.QWidget()
        verticalLayout = QtGui.QVBoxLayout(tableTab)
        verticalLayout.setContentsMargins(30, 30, 30, 30)
        label = QtGui.QLabel(tableTab)
        verticalLayout.addWidget(label)
        horizontalLayout = QtGui.QHBoxLayout()
        verticalLayout.addLayout(horizontalLayout)

        tableTab.setMinimumSize(200,300) ###era 230
        font = QtGui.QFont()
        font.setPointSize(14)

        if self.receivePayments:
            tabState =  query("SELECT * FROM orders WHERE state=0 AND ( (stoptime is NULL or stoptime >  "+ str(time.time()) +" ) OR  payed < 8 )  AND table_id='"+ str(tabINfo[0])+"'")
        else:
            tabState =  query("SELECT * FROM orders WHERE state=0 AND ( stoptime is NULL or stoptime >  "+ str(time.time()) +" )  AND table_id='"+ str(tabINfo[0])+"'")

        con_off=tabINfo[6]
        con_on=tabINfo[7]
        controllerTip = tabINfo[11]
        controllerChannel = tabINfo[12]

        stylesheet = 'border-radius: 10%/*;margin-top: 60px;margin-left: 35px;margin-right: 35px;*/'
        if len(tabState):
            tabText += "Order: "+ str(tabState[0][7]) + "<br/>"
            ##daca e ocupata, ( roshie )
            if tabState[0][4] == None or (tabState[0][4] -time.time()) > 0:
                tabText += "Playing<br/>Gone: " +str(time.strftime("%H:%M:%S", time.gmtime( time.time() - tabState[0][3])))+'<br/>'
                ##dam comanda aprindem lumina la masa
                if int(settingsConfig.value("ComportSettings/EnableComport")):
                    self.bytesToControler += con_on+" "
                if int(settingsConfig.value("URLcontroler/EnableURL")) or int(settingsConfig.value("USRprotocol/Enable")):
                    self.bytesUrlChanels.insert(0,[controllerTip,controllerChannel,1])

            ###daca e setata pe timp anume
                if tabState[0][4]:
                    self.shiftCanCloseTemp = False
                    # logging.info(tabState)
                    tabText +="Remain: " +str(time.strftime("%H:%M:%S", time.gmtime(tabState[0][4] -time.time())))+'<br/>'
                    if self.loggedIn and tabState[0][5]<8  and self.receivePayments:
                        actionPay = QtGui.QPushButton(tableTab)
                        actionPay.setText("&Pay")
                        actionPay.setFont(font)
                        actionPay.clicked.connect(lambda :self.payForGame(tabState[0][7],0))
                        horizontalLayout.addWidget(actionPay)

            ###daca e setata pentru nelimitat
                else:
                    self.shiftCanCloseTemp = False
                    tabText +="Remain: Unlimited <br/>"
                    if self.loggedIn:
                        actionFinishGame = QtGui.QPushButton(tableTab)
                        actionFinishGame.setText("&Finish")
                        actionFinishGame.setFont(font)
                        actionFinishGame.clicked.connect(lambda :self.payForGame(tabState[0][7],1,timeStart=tabState[0][3]))
                        horizontalLayout.addWidget(actionFinishGame)
                tableTab.setStyleSheet("background-color: rgb(231, 76, 60);" +stylesheet)


            ##daca  masa la masa a expirat timpul,  shi inca nu e platita
            elif tabState[0][4] -time.time() < 0 :
                self.shiftCanCloseTemp = False
                tabText += "Expired<br/><br/><br/>"
                tableTab.setStyleSheet("background-color: rgb(241, 196, 15);"+stylesheet)
                if self.loggedIn and self.receivePayments:
                    actionPay = QtGui.QPushButton(tableTab)
                    actionPay.setText("&Pay")
                    actionPay.setFont(font)
                    actionPay.clicked.connect(lambda :self.payForGame(tabState[0][7],0))
                    horizontalLayout.addWidget(actionPay)


                if int(settingsConfig.value("ComportSettings/EnableComport")):
                    self.bytesToControler += con_off + " "
                if int(settingsConfig.value("URLcontroler/EnableURL")) or int(settingsConfig.value("USRprotocol/Enable")):
                    self.bytesUrlChanels.insert(0,[controllerTip,controllerChannel,0])

            else:
                logging.info("ERORR :Masa care un intra in nici o categorie"+str(tabState))

            summForGam = getSummForGame(tabState[0])
            tabText += "Game cost: "+ str(summForGam) + "<br/>"
            if self.receivePayments:
                avansuri = query("SELECT sum FROM payments  WHERE parent_order='"+tabState[0][0] +"'")
                avans=0
                for i in avansuri:
                    avans+=i[0]
                discount = round(float(summForGam) * float(tabState[0][14] / 100), 2)
                tabText += "Discount : " + str(discount) + "<br/>"
                tabText += "Payments: "+ str(avans)  + "<br/>"

                tabText += "Balance : " + str(   round(  summForGam - float(avans)-discount ,2)    ) + "<br/>"


            if (time.time()-tabState[0][3] )<60:
                actionCancelGame = QtGui.QPushButton(tableTab)
                actionCancelGame.setText("&Cancel")
                actionCancelGame.setFont(font)
                actionCancelGame.clicked.connect(lambda :self.cancelGame(tabState[0][7]))
                horizontalLayout.addWidget(actionCancelGame)

        ##daca masa e libera
        else:
            tabText += "Free<br/><br/><br/><br/><br/><br/>"
            tableTab.setStyleSheet("background-color: rgb(149, 165, 166);"+stylesheet)
            if self.loggedIn:
                actionSetTime = QtGui.QPushButton(tableTab)
                actionSetTime.setText("&Set time")
                actionSetTime.setFont(font)
                actionSetTime.clicked.connect(lambda : self.setTime(tabINfo[0]))
                horizontalLayout.addWidget(actionSetTime)
            if int(settingsConfig.value("ComportSettings/EnableComport")):
                self.bytesToControler += con_off+" "
            if int(settingsConfig.value("URLcontroler/EnableURL")) or int(settingsConfig.value("USRprotocol/Enable")):
                self.bytesUrlChanels.insert(0, [controllerTip, controllerChannel, 0])

        if not self.loggedIn:
            actionLogIn = QtGui.QPushButton(tableTab)
            actionLogIn.setText("&Log in")
            actionLogIn.setFont(font)
            actionLogIn.clicked.connect(self.loginForm)
            horizontalLayout.addWidget(actionLogIn)
        label.setText(tabText+"</div>")
        return tableTab


    def cancelGame(self,tabInfo):

        logging.info('-----cancelGame-----')

    # logging.info(tabInfo)
        query("DELETE FROM orders WHERE row_id="+str(tabInfo))

    def payForGame(self,id,close,timeStart=None):
        logging.info('-----payForGame-----')
        if close :
            timeRounded = round(int(int(time.time())-timeStart)/60)*60+timeStart
            if timeRounded==timeStart:
                    timeRounded=60+timeStart
            query("UPDATE orders SET stoptime="+ str(timeRounded)+ " WHERE row_id="+str(id))

            ##punem pretul, total pentru joaca
            order = query("SELECT * FROM orders  WHERE row_id=" + str(id))[0]
            query("UPDATE orders SET summ_brutto=" + str(getSummForGame(order)) + " WHERE row_id=" + str(id))

        if self.receivePayments:
            dialog = DialogPay(id,self)
            if dialog.exec_():
                logging.info('Dialogul  Acitare  sa inchis')
                self.renderTables()


    def setTime(self,id):
        logging.info('-----setTime-----')
        dialog = DialogSetTime(id,self)
        if dialog.exec_():
            logging.info('Dialogul La SETTIME  sa inchis')
            self.renderTables()

    def checkCurrentPeriod(self):

        logging.info('-----checkCurentperiod-----')
        global curentTimePeriod
        curentTimePeriod= getCurentPeriod()


    def createActions(self):
        logging.info('-----createActions-----')
        self.loginAct = QtGui.QAction("Log IN", self, statusTip="Login Form",  triggered=self.loginForm)
        self.logoffAct = QtGui.QAction("Log OFF", self, statusTip="Logout",enabled=False,  triggered=self.logOut)
        if self.shiftFunctional:
            self.closeShiftButton = QtGui.QAction("Shift..", self, statusTip="Close shift", triggered=self.closeShiftQ)

        self.closeAct = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"&Close", self, shortcut="Ctrl+W",            statusTip="Close this window", triggered=self.close)
        self.exitAct = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"E&xit", self, shortcut="Ctrl+Q",            statusTip="Exit the application",            triggered=QtGui.qApp.closeAllWindows)

        self.dataOrders = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"&Orders", self, triggered=self.dataOrdersTable)
        self.dataCards = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"&Cards", self, triggered=self.dataCardsTable)
        if self.receivePayments:
            self.reportPayments = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"&Payments", self, triggered=self.reportPaymentsTable)
        if self.shiftFunctional:
            self.reportShift = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"&Shifts", self, triggered=self.reportShiftTable)
            self.reportChange = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"&Shift Report", self, triggered=self.reportChangeTable)

        self.aboutAct = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'),"&About", self,statusTip="Show the application's About box",triggered=self.about)

        #################SETTINGS
        self.userAct = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'), "&User Settings",self,statusTip="User Administration",triggered=self.editUserOpen)
        self.tableAct = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'), "&Table Settings",self, statusTip="Table Administration",triggered=self.editTableOpen)
        self.settingsAct = QtGui.QAction(QtGui.QIcon('images/circle_mini.png'), "&Program Settings",self, statusTip="Program settings",triggered=self.editSettingsOpen)

        # self.textEdit.copyAvailable.connect(self.cutAct.setEnabled)
        # self.textEdit.copyAvailable.connect(self.copyAct.setEnabled)

    def createMenus(self):
        logging.info('-----createMenus-----')

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.loginAct)
        self.fileMenu.addAction(self.logoffAct)
        if self.shiftFunctional:
            self.fileMenu.addAction(self.closeShiftButton)

        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.closeAct)
        self.fileMenu.addAction(self.exitAct)

        self.dataMenu = self.menuBar().addMenu("&Data")
        self.dataMenu.addAction(self.dataCards)
        self.dataMenu.addAction(self.dataOrders)
        if self.receivePayments:
            self.dataMenu.addAction(self.reportPayments)
        if self.shiftFunctional:
            self.dataMenu.addAction(self.reportShift)

        if self.shiftFunctional:
            self.repMenu = self.menuBar().addMenu("&Reports")
            self.repMenu.addAction(self.reportChange)

        self.menuBar().addSeparator()

        self.settMenu = self.menuBar().addMenu("&Settings")
        self.settMenu.addAction(self.userAct)
        self.settMenu.addAction(self.tableAct)
        self.settMenu.addAction(self.settingsAct)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.menuBar().hide()

    def createToolBars(self):
        logging.info('-----checkToolBars-----')

        self.fileToolBar = self.addToolBar("Login")
        self.fileToolBar.setStyleSheet("font-size:18px")
        self.fileToolBar.addAction(self.loginAct)
        self.fileToolBar.addAction(self.logoffAct)
        if self.shiftFunctional:
            self.fileToolBar.addAction(self.closeShiftButton)
        # self.fileToolBar.addAction(self.saveAct)

        self.editToolBar = self.addToolBar("Sallons")
        self.editToolBar.setStyleSheet("font-size:18px")

        #taburile   tastele pentru saloane
        sql = "SELECT DISTINCT salon FROM tables ORDER by salon ASC "
        records = query(sql)
        logging.info(records)
        if records:
            # logging.info(record)
            sallon = QtGui.QAction("&All" ,self,triggered=lambda :self.renderSaloon(None))
            sallon.setCheckable(True)
            if self.sallonOnly ==None:
                sallon.setChecked(True)
            self.editToolBar.addAction(sallon)
            self.editToolBar.addSeparator()

            for record in records:
                if record[0]==0:
                    sallon = QtGui.QAction("&Salon 1" ,self,triggered=lambda :self.renderSaloon(0))
                if record[0]==1:
                    sallon = QtGui.QAction("&Salon 2" ,self,triggered=lambda :self.renderSaloon(1))
                if record[0]==2:
                    sallon = QtGui.QAction("&Salon 3" ,self,triggered=lambda :self.renderSaloon(2))
                if record[0]==3:
                    sallon = QtGui.QAction("&Salon 4" ,self,triggered=lambda :self.renderSaloon(3))
                if record[0]==4:
                    sallon = QtGui.QAction("&Salon 5" ,self,triggered=lambda :self.renderSaloon(4))
                if record[0]==5:
                    sallon = QtGui.QAction("&Salon 6" ,self,triggered=lambda :self.renderSaloon(5))
                if record[0]==6:
                    sallon = QtGui.QAction("&Salon 7" ,self,triggered=lambda :self.renderSaloon(6))
                if record[0]==7:
                    sallon = QtGui.QAction("&Salon 8" ,self,triggered=lambda :self.renderSaloon(7))
                if record[0]==8:
                    sallon = QtGui.QAction("&Salon 9" ,self,triggered=lambda :self.renderSaloon(8))
                self.editToolBar.addAction(sallon)
                sallon.setCheckable(True)
                if self.sallonOnly ==record[0]:
                    sallon.setChecked(True)

                self.editToolBar.addSeparator()

    def dataOrdersTable(self):
        logging.info('-----dataOrdersTable-----')
        dialog = DialogOrders()
        dialog.exec_()

    def dataCardsTable(self):
        logging.info('-----dataCardsTable-----')
        dialog = DialogCards()
        dialog.exec_()



    def reportPaymentsTable(self):
        logging.info('-----reportPaymentdTable-----')
        dialog = DialogPayTable()
        dialog.exec_()

    def reportShiftTable(self):
        logging.info('-----reportShiftTable-----')
        dialog = DialogShiftTable(self)
        dialog.exec_()


    def closeShiftQ(self):
        #verificam  daca se poate  de inchis smena
        reply = QtGui.QMessageBox.question(self, 'Confirm', "Close shift?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            ##inchidem  smena,   shi tipatim raport,  al schimbului curent
            if(self.shiftCanClose):
                if self.tribarSyncShifts:
                    sync="0"
                else:
                    sync="1"
                try:
                   newID =  query("INSERT INTO `shift` (`uuid`, `att`, `user`,`sync`) VALUES ('" + getNewSID() + "', '" + str(time.time()) + "', '" + self.userInfo[0] + "','" + sync+  "')")
                except Exception as e:
                    logging.critical("Cannot close shift")
                    logging.critical(str(e))
                    eroarePopup("Cannot close shift")
                else:
                    try:
                        dialog = DialogChange(self.userInfo,query("SELECT id AS idd,uuid,user,(SELECT att FROM shift WHERE id=idd-1) AS att ,att AS finish FROM shift WHERE id =" + str(newID)  +"  ORDER BY id DESC LIMIT 1")[0])




                        ##    raportul   pe emil
                        showExtendedReport = bool(int(query("SELECT value FROM settings WHERE id=95")[0][0]))
                        reportHTML = dialog.renderHtmlCode(extended=showExtendedReport)
                        sendEmail(query("SELECT value FROM settings WHERE id=36")[0][0],reportHTML)


                        ##  tiparim  raportul
                        showExtendedReport = bool(int(query("SELECT value FROM settings WHERE id=94")[0][0]))
                        reportHTML = dialog.renderHtmlCode(extended=showExtendedReport)

                        if int(query("SELECT value FROM settings WHERE id=57")[0][0]) :
                            printZ_Report()
                        printerClass = printer.PrinterClass()
                        printerClass.printHtml(reportHTML)
                    except:
                        logging.info("Shift closed")
                        eroarePopup("Shift closed")
                        raise
            else:
                eroarePopup("Shift can`t  close! Active tables")
        else:
            #tipatim raport la  umtimul schimb inchis
            reply = QtGui.QMessageBox.question(self, 'Confirm', "Print last closed shift report?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                    shift = query("SELECT id AS idd,uuid,user,att,(SELECT att FROM shift WHERE id=idd-1) AS finish  FROM shift  ORDER BY id DESC LIMIT 1")[0]
                    dialog = DialogChange(self.userInfo,shift )
                    reportHTML = dialog.renderHtmlCode()
                    printerClass = printer.PrinterClass()
                    printerClass.printHtml(reportHTML)

    def reportChangeTable(self):
        logging.info('-----reportChangeTable-----')
        dialog = DialogChange(self.userInfo)
        dialog.exec_()

    def loginForm(self):
        logging.info('-----loginForm-----')
        dialog = DialogLogin()
        if dialog.exec_():
            logging.info('Dialogul La Login  sa inchis')
            if dialog.exitCode =="login":  ####LOGAREA
                ##pastran datele,  din forma
                self.loggedIn = 1
                self.lightCheck=0
                self.userInfo = dialog.userINfo[0]
                # logging.info(self.userInfo)
                if not self.userInfo[2]:
                    self.menuBar().show()
                self.loginAct.setDisabled(True)
                self.logoffAct.setDisabled(False)
                self.renderTables()
                self.statusUsername.setText("User : "+self.userInfo[1])

                return True
            elif dialog.exitCode =="exit": #####IESHIREA DIN PROGRMA
                #####pornit test  ca sa stingem toate luminile
                logging.info(self.workerThread.lightAll(0))
                time.sleep(2)       
                logging.info("Am ieshit din program")
                sys.exit(88)

    def logOut(self):
        logging.info('-----logOut-----')
        self.userInfo =''
        self.loggedIn = 0
        self.loginAct.setDisabled(False)
        self.logoffAct.setDisabled(True)
        self.renderTables()
        self.statusUsername.setText("No logged")
        self.menuBar().hide()

    def renderSaloon(self,saloon):
        logging.info('-----renderSallon-----')
        self.sallonOnly=saloon
        self.renderTables()
        self.removeToolBar(self.fileToolBar)
        self.removeToolBar(self.editToolBar)
        self.createToolBars()


    def createStatusBar(self):
        logging.info('-----createStatusBar-----')
        self.statusBarErrorSetFunc(err=False)
        self.statusbarTimer =   QtGui.QLabel()

        self.statusBar().addPermanentWidget (self.statusbarTimer)
        self.statusBar().addPermanentWidget (self.statusUsername)

        if int(query("SELECT value FROM settings WHERE id=67")[0][0]):
            nuller = QtGui.QPushButton('DB')
            nuller.clicked.connect(self.clearDB)
            self.statusBar().addPermanentWidget (nuller)




############### METODELE MELE
    def editUserOpen(self):
        logging.info('-----editUserOpenb-----')

        dialog = DialogUser()
        if not dialog.exec_():
            logging.info('Dialogul La useri  sa inchis')

    def clearDB(self):
        logging.info('-----clearDB-----')
        reply = QtGui.QMessageBox.question(self, 'Confirm', "Are you sure?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            query("DELETE FROM orders")
            query("DELETE FROM shift")
            query("INSERT INTO `shift` (`uuid`, `att`, `user`) VALUES ('" + getNewSID() + "', '" + str(time.time()) + "', '" + self.userInfo[0] + "')")
            query("DELETE FROM payments")


    def editTableOpen(self):
        logging.info('-----editTableOpen-----')

        dialog = DialogTable()
        # dialog.completamSelectul()
        if not dialog.exec_():
            logging.info('Dialogul La mese  sa inchis')


    def editSettingsOpen(self):
        logging.info('-----editSettingsOOpen-----')

        dialog = DialogSettings()
        if not dialog.exec_():
            logging.info('Dialogul La setari  sa inchis')



##################################################################################################
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
