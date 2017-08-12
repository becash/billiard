# import sip,time
# sip.setapi('QString', 2)
# sip.setapi('QVariant', 2)

import sys,requests, socket
from PySide import QtGui
from functions import *


#################COmboview(select)  in tabele
class TableModel(QtCore.QAbstractTableModel):
    """
    A simple 5x4 table model to demonstrate the delegates
    """
    def rowCount(self, parent=QtCore.QModelIndex()): return 5
    def columnCount(self, parent=QtCore.QModelIndex()): return 4

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid(): return None
        if not role==QtCore.Qt.DisplayRole: return None
        return "{0:02d}".format(index.row())

    def setData(self, index, value, role=QtCore.Qt.DisplayRole):
        print ("setData", index.row(), index.column(), value)

    def flags(self, index):
        if (index.column() == 0):
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled
        else:
            return QtCore.Qt.ItemIsEnabled

class ComboDelegate(QtGui.QItemDelegate):
    """
    A delegate that places a fully functioning QComboBox in every
    cell of the column to which it's applied
    """

    def __init__(self, parent,items):
        self.items = items
        QtGui.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        combo = QtGui.QComboBox(parent)
        combo.addItems(self.items)
        self.connect(combo, QtCore.SIGNAL("currentIndexChanged(int)"), self, QtCore.SLOT("currentIndexChanged()"))
        return combo

    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.setCurrentIndex(int(index.model().data(index)))
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        logging.info('in dialog')
        self.parent().setData(index, editor.currentIndex())


    def currentIndexChanged(self):
        self.commitData.emit(self.sender())

class TableView(QtGui.QTableView):
    """
    A simple table to demonstrate the QComboBox delegate.
    """
    def __init__(self, *args, **kwargs):
        QtGui.QTableView.__init__(self, *args, **kwargs)

        # Set the delegate for column 0 of our table
        # self.setItemDelegateForColumn(0, ButtonDelegate(self))
        self.setItemDelegateForColumn(2, ComboDelegate(self))


if(int(settingsConfig.value("ComportSettings/EnableComport"))==1):
    import serial



class WorkerThread(QtCore.QThread):
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow

        super(WorkerThread, self).__init__()
        if(int(settingsConfig.value("ComportSettings/EnableComport"))==1):
            #####tot ce tine de serial
            self.bytesToControler=''
            try:
                self.serial = serial.Serial(
                    port=settingsConfig.value("ComportSettings/Port"),
                    baudrate=settingsConfig.value("ComportSettings/Baudrate"),
                    timeout=1
                )
            except serial.SerialException:
                    e = sys.exc_info()[0]
                    logging.critical( "Error, CHECK COM PORT SETTINGS: %s" % e )
            else:
                self.lightAll(1)

        if int(settingsConfig.value("URLcontroler/EnableURL")) or int(settingsConfig.value("USRprotocol/Enable")):
                self.lightAll(1)

    def run(self):
        logging.info("----------run-----------")
        if (int(settingsConfig.value("FirebirdSettings/EnableFirebird"))):
            self.syncFirebirdPayments()

        if (int(settingsConfig.value("ComportSettings/EnableComport"))):
            if self.comportWrite(self.bytesToControler):
                ### returnam ,    in cas de succes
                self.emit(QtCore.SIGNAL("threadDone(QString)"), "ok")
            else:
                ## returnam in caz de probleme
                self.emit(QtCore.SIGNAL("threadDone(QString)"), "errorControler")

        if int(settingsConfig.value("URLcontroler/EnableURL")):
            logging.info(self.bytesUrlChanels)
            for ch in self.bytesUrlChanels :
                if(ch[0]=="USR-WIFI-IO-83"):
                    self.controlerUSR_WIfi_io_83(ch[2],ch[1])


        if int(settingsConfig.value("USRprotocol/Enable")):
            logging.info(self.bytesUrlChanels)
            for ch in self.bytesUrlChanels :
                if(ch[0]=="USR"):
                    self.controlerUSR(ch[2],ch[1])







    def comportWrite(self,string):
        logging.info("----------comportWrite-----------")
        bute = bytearray.fromhex(string)
        logging.info(string)
        logging.info(type(bute))
        logging.info(bute)
        try:
            self.serial.write(bute)
        except AttributeError as e:
            logging.critical( "COM Error, CHECK COM PORT"+str(e))
            return False
        else:
            if self.serial.read():
                logging.info("COM OK")
                return True
            else:
                logging.warning("COM Light Ctroller Missing")
                return False


    def syncFirebirdPayments(self):
        logging.info("----------syncFirebirdPayments-----------")
        unsync = query("SELECT *,table_id as ids,(SELECT name FROM tables WHERE id =ids) FROM orders WHERE sync = 0 AND stoptime IS NOT NULL AND   payed=9  AND stoptime <  "+ str(time.time())+" LIMIT 3")
        uuidTribarProduct =  query("SELECT value FROM settings WHERE id = 10")[0][0]
        uuidTribarTable =  str(query("SELECT value FROM settings WHERE id = 20")[0][0])
        # logging.info(uuidTribarTable)

        #####VERIFICAM  DACA EXISTA UUID NECESARE
        if (len(queryFirebird('SELECT "UUID" FROM "Tables" WHERE "TableNo"=\''+ uuidTribarTable +'\'')) and
            len(queryFirebird('SELECT "Name" FROM "Products" WHERE "UUID"=\''+ uuidTribarProduct +'\''))):

            for elemm in unsync:
                if len(queryFirebird('SELECT "Name" FROM "Users" WHERE "UUID"=\''+ elemm[2] +'\'')):
                    logging.info("VERIFICAM  DACA EXISTA UUID NECESARE"+elemm)
                    try:
                        timeStamp = time.strftime("%d-%b-%Y %H:%M:%S", time.localtime(time.time()))
                        try:
                            queryFirebird('INSERT INTO "Orders" (UUID, "CashType", "At", "Operator",  "ClosedAt","Discount","State","PredCheck","NotExtSync","TableNo")\
                                      VALUES (\'' + elemm[0] + '\',  0, \''+ timeStamp  +'\', \'' + elemm[2] + '\',  \''+ timeStamp+'\',0,1,0,1,'+ uuidTribarTable +');')
                        except:
                            logging.critical("Error, Insert Row in firefird")
                            raise
                        else:
                            sumForGame =getSummForGame(elemm)
                            queryFirebird('INSERT INTO "OrderDetails" ("ParentID", "At", "Product",  "OutOrder", "Price", "Counts", "Printed",  UUID, "Ready","Modified") \
                            VALUES (\''+ elemm[0] +'\', \''+timeStamp +'\', \''+uuidTribarProduct +'\', 4, '+str(sumForGame)+', 1, 1, \''+getNewSID() +'\', 0,\'Table:'+ elemm[13] +' ['+time.strftime("%H:%M", time.localtime(elemm[3]))+"-"+time.strftime("%H:%M", time.localtime(elemm[4]))+']\');')
                    except:
                        raise
                    else:
                        query("UPDATE orders SET sync=1 WHERE uuid='"+ elemm[0] +"'")
                    # return ###  acest return face sa ca se prelucreze doar o inscriere
                else:
                    logging.info("TRIOBAR : User UUID ERROR")

        else:
                logging.info("TRIOBAR : Table or Product UUID ERROR")




    def controlerUSR_WIfi_io_83(self,setState,chanel):

        time.sleep(0.3)
        logging.info("----------controlerUSR_WIfi_io_83-----------")
        try:
            getCurentState = requests.get(settingsConfig.value("URLcontroler/controlerUSR_WIfi_io_83") +'/httpapi.json?CMD=UART_WRITE&UWHEXVAL=0',
                auth=requests.auth.HTTPBasicAuth(settingsConfig.value("URLcontroler/UserName"), settingsConfig.value("URLcontroler/Password")),
                timeout = 2  ).text
        except Exception as e:
            self.mainWindow.statusBarErrorSetFunc(err='urlCcontrolerErr')

            logging.warning(str(e))
            # eroarePopup(str(e))
            return
        logging.info("controlerUSR_WIfi_io_83 return state"+getCurentState)
        ####convertim  in biti,  shi inversam  ca sa putem extrage  bitii
        try:
            getCurentState = str(bin(int(getCurentState)-1792))[2:].zfill(8)[::-1]
            # print(getCurentState)


        except Exception as e:
            logging.warning("Controller responce")
            logging.warning(e)
            eroarePopup(e)
            return
        logging.info("getCurentState>>",getCurentState)

        # getCurentState = str(getCurentState)
        # print(chanel)
        curentChanelState = getCurentState[(int(chanel)-1):int(chanel)]
        # print(curentChanelState)
        logging.info('>>'+curentChanelState+'<<')
        if(int(setState)!=int(curentChanelState)):
            try:
                setCurentState = requests.get(settingsConfig.value("URLcontroler/controlerUSR_WIfi_io_83") + '/httpapi.json?CMD=UART_WRITE&UWHEXVAL='+str(chanel),
                                          auth=requests.auth.HTTPBasicAuth(settingsConfig.value("URLcontroler/UserName"), settingsConfig.value("URLcontroler/Password")),
                                            timeout = 2 ).text
            except Exception as e:
                self.mainWindow.statusBarErrorSetFunc(err='urlCcontrolerErr')
                logging.warning("-----CONTROLLER RESPOND ERROR")
                logging.warning(str(e))
                eroarePopup(str(e))
            logging.info(set)




    def controlerUSR(self,setState,chanel):
        time.sleep(0.2)
        logging.info("----------controlerUSR-----------")

        # data = sock.recv(1024)
        # print(data.decode())
        if setState:
            comand = b'\x02'
        else:
            comand = b'\x01'

        if int(chanel) < 16:
            hexPrefix = '0'
        else:
            hexPrefix = ''

        try:
            self.USRsock.send(b'\x55\xAA\x00\x03\x00' +comand+  bytes.fromhex(hexPrefix+hex(int(chanel))[2:] )  +b'\x00')
            # data = sock.recv(1024)
            # print(data)

        except Exception as e:
            # logging.warning("----------controlerUSR-----------")
            # logging.warning(e)
            # print(e)
            try:
                self.USRsock = socket.socket()
                self.USRsock.connect((settingsConfig.value("USRprotocol/IP"), int(settingsConfig.value("USRprotocol/Port"))))
                self.USRsock.send(bytes(settingsConfig.value("USRprotocol/Password"),'ascii') +b'\x0D\x0A')
                self.controlerUSR(setState,chanel)
            except Exception as e:
                logging.warning("----------controlerUSR-----------")
                logging.warning(e)
                print(e)





    def lightAll(self,mode):
        logging.info("----------lightAll-----------")
        colona = False
        if mode ==1 and int(settingsConfig.value("ComportSettings/EnableComport")):
            colona ="com_on"
        elif mode==0 and int(settingsConfig.value("ComportSettings/EnableComport")):
            colona = "com_off"

        if int(settingsConfig.value("URLcontroler/EnableURL")) or int(settingsConfig.value("USRprotocol/Enable")) :
            colona = "controler,channel"

        if(colona):
            tabs =query("SELECT "+colona+" FROM tables WHERE enable =1 ORDER by `order`,`salon`")
            if int(settingsConfig.value("ComportSettings/EnableComport")):
                self.bytesToControler=''
                for tab in tabs:
                    self.bytesToControler += tab[0]+" "
                if self.comportWrite(self.bytesToControler):
                    return True
            else:
                for tab in tabs:
                    # print(tab)
                    # print(mode)
                    if(tab[0]=='USR-WIFI-IO-83') and int(settingsConfig.value("URLcontroler/EnableURL")):
                        self.controlerUSR_WIfi_io_83(mode,tab[1])
                    if(tab[0]=='USR') and int(settingsConfig.value("USRprotocol/Enable")):
                        self.controlerUSR(mode,tab[1])

        if(mode):
            time.sleep(3)
            self.lightAll(0)
        return True




###TESTAREA
#
# if __name__=="__main__":
#     from sys import argv, exit
#
#     class Widget(QtGui.QWidget):
#         """
#         A simple test widget to contain and own the model and table.
#         """
#         def __init__(self, parent=None):
#             QtGui.QWidget.__init__(self, parent)
#
#             l=QtGui.QVBoxLayout(self)
#             self._tm=TableModel(self)
#             self._tv=TableView(self)
#             self._tv.setModel(self._tm)
#             for row in range(0, self._tm.rowCount()):
#                 self._tv.openPersistentEditor(self._tm.index(row, 2))
#
#             l.addWidget(self._tv)
#
#     a=QtGui.QApplication(argv)
#     w=Widget()
#     w.show()
#     w.raise_()
#     exit(a.exec_())
#


####################  PINA AICI functia  COmboview

#####DATEPIKER
class PyDateTimeEdit(QtGui.QDateTimeEdit):
    #
    # Initialize base class
    # Force use of the calendar popup
    # Set default values for calendar properties
    #
    def __init__(self, *args):
        super(PyDateTimeEdit, self).__init__(*args)

        self.setCalendarPopup(True)
        self.__cw = None
        self.__firstDayOfWeek = QtCore.Qt.Monday
        self.__gridVisible = False
        self.__horizontalHeaderFormat = QtGui.QCalendarWidget.ShortDayNames
        self.__verticalHeaderFormat = QtGui.QCalendarWidget.ISOWeekNumbers
        self.__navigationBarVisible = True

    #
    # Call event handler of base class
    # Get the calendar widget, if not already done
    # Set the calendar properties
    #
    def mousePressEvent(self, event):
        super(PyDateTimeEdit, self).mousePressEvent(event)

        if not self.__cw:
            self.__cw = self.findChild(QtGui.QCalendarWidget)
            if self.__cw:
                self.__cw.setFirstDayOfWeek(self.__firstDayOfWeek)
                self.__cw.setGridVisible(self.__gridVisible)
                self.__cw.setHorizontalHeaderFormat(self.__horizontalHeaderFormat)
                self.__cw.setVerticalHeaderFormat(self.__verticalHeaderFormat)
                self.__cw.setNavigationBarVisible(self.__navigationBarVisible)

    #
    # Make sure, the calendarPopup property is invisible in Designer
    #
    def getCalendarPopup(self):
        return True
    # calendarPopup = QtCore.pyqtProperty(bool, fget=getCalendarPopup)

    #
    # Property firstDayOfWeek: Qt::DayOfWeek
    # Get: getFirstDayOfWeek()
    # Set: setFirstDayOfWeek()
    # Reset: resetFirstDayOfWeek()
    #
    def getFirstDayOfWeek(self):
        return self.__firstDayOfWeek
    def setFirstDayOfWeek(self, dayOfWeek):
        if dayOfWeek != self.__firstDayOfWeek:
            self.__firstDayOfWeek = dayOfWeek
            if self.__cw:
                self.__cw.setFirstDayOfWeek(dayOfWeek)
    def resetFirstDayOfWeek(self):
        if self.__firstDayOfWeek != QtCore.Qt.Monday:
            self.__firstDayOfWeek = QtCore.Qt.Monday
            if self.__cw:
                self.__cw.setFirstDayOfWeek(QtCore.Qt.Monday)
    # firstDayOfWeek = QtCore.pyqtProperty(QtCore.Qt.DayOfWeek,
    #                                      fget=getFirstDayOfWeek,
    #                                      fset=setFirstDayOfWeek,
    #                                      freset=resetFirstDayOfWeek)
    #
    # #
    # Property gridVisible: bool
    # Get: isGridVisible()
    # Set: setGridVisible()
    # Reset: resetGridVisible()
    #
    def isGridVisible(self):
        return self.__gridVisible
    def setGridVisible(self, show):
        if show != self.__gridVisible:
            self.__gridVisible = show
            if self.__cw:
                self.__cw.setGridVisible(show)
    def resetGridVisible(self):
        if self.__gridVisible != False:
            self.__gridVisible = False
            if self.__cw:
                self.__cw.setGridVisible(False)
    # gridVisible = QtCore.pyqtProperty(bool,
    #                                   fget=isGridVisible,
    #                                   fset=setGridVisible,
    #                                   freset=resetGridVisible)
    #
    #
    # Property horizontalHeaderFormat: QCalendarWidget::HorizontalHeaderFormat
    # Get: getHorizontalHeaderFormat()
    # Set: setHorizontalHeaderFormat()
    # Reset: resetHorizontalHeaderFormat()
    #
    def getHorizontalHeaderFormat(self):
        return self.__horizontalHeaderFormat
    def setHorizontalHeaderFormat(self, format):
        if format != self.__horizontalHeaderFormat:
            self.__horizontalHeaderFormat = format
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(format)
    def resetHorizontalHeaderFormat(self):
        if self.__horizontalHeaderFormat != QtGui.QCalendarWidget.ShortDayNames:
            self.__horizontalHeaderFormat = QtGui.QCalendarWidget.ShortDayNames
            if self.__cw:
                self.__cw.setHorizontalHeaderFormat(QtGui.QCalendarWidget.ShortDayNames)
    # horizontalHeaderFormat = QtCore.pyqtProperty(QtGui.QCalendarWidget.HorizontalHeaderFormat,
    #                                              fget=getHorizontalHeaderFormat,
    #                                              fset=setHorizontalHeaderFormat,
    #                                              freset=resetHorizontalHeaderFormat)
    #
    #
    # Property verticalHeaderFormat: QCalendarWidget::VerticalHeaderFormat
    # Get: getVerticalHeaderFormat()
    # Set: setVerticalHeaderFormat()
    # Reset: resetVerticalHeaderFormat()
    #
    def getVerticalHeaderFormat(self):
        return self.__verticalHeaderFormat
    def setVerticalHeaderFormat(self, format):
        if format != self.__verticalHeaderFormat:
            self.__verticalHeaderFormat = format
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(format)
    def resetVerticalHeaderFormat(self):
        if self.__verticalHeaderFormat != QtGui.QCalendarWidget.ISOWeekNumbers:
            self.__verticalHeaderFormat = QtGui.QCalendarWidget.ISOWeekNumbers
            if self.__cw:
                self.__cw.setVerticalHeaderFormat(QtGui.QCalendarWidget.ISOWeekNumbers)
    # verticalHeaderFormat = QtCore.pyqtProperty(QtGui.QCalendarWidget.VerticalHeaderFormat,
    #                                            fget=getVerticalHeaderFormat,
    #                                            fset=setVerticalHeaderFormat,
    #                                            freset=resetVerticalHeaderFormat)

    #
    # Property navigationBarVisible: bool
    # Get: isNavigationBarVisible()
    # Set: setNavigationBarVisible()
    # Reset: resetNavigationBarVisible()
    #
    def isNavigationBarVisible(self):
        return self.__navigationBarVisible
    def setNavigationBarVisible(self, visible):
        if visible != self.__navigationBarVisible:
            self.__navigationBarVisible = visible
            if self.__cw:
                self.__cw.setNavigationBarVisible(visible)
    def resetNavigationBarVisible(self):
        if self.__navigationBarVisible != True:
            self.__navigationBarVisible = True
            if self.__cw:
                self.__cw.setNavigationBarVisible(True)
    # navigationBarVisible = QtCore.pyqtProperty(bool,
    #                                            fget=isNavigationBarVisible,
    #                                            fset=setNavigationBarVisible,
    #                                            freset=resetNavigationBarVisible)
    #


########PRINTER  CLAS
class PrintView(QtGui.QTableView):
    def __init__(self):
        super(PrintView, self).__init__()
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def print_(self, printer):
        self.resize(printer.width(), printer.height())
        self.render(printer)





################################CLAS EPNTRU   MESE,  care   se aliniaza dupa   latimea la pagina
class FlowLayout(QtGui.QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)


        if parent is not None:
            self.setMargin(margin)

        self.setSpacing(spacing)

        self.itemList = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

#        size += QtCore.QSize(2 * self.margin(), 2 * self.margin())
        return size

    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        lineHeight = 0

        for item in self.itemList:
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton, QtGui.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton, QtGui.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
                item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))

            x = nextX
            lineHeight = max(lineHeight, item.sizeHint().height())

        return y + lineHeight - rect.y()



##################USER LEVELS
userLevels = []
userLevels.append("Provider")
userLevels.append("Administrator")
userLevels.append("User")
userLevels.append("Guest")


###########SEELECT  BOOL
selectBool = []
selectBool.append("Disabled")
selectBool.append("Enabled")

salons = []
salons.append("1")
salons.append("2")
salons.append("3")
salons.append("4")
salons.append("5")
salons.append("6")
salons.append("7")
salons.append("8")
salons.append("9")


