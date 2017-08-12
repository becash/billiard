import sys,traceback,logging


try:
    from PySide.QtCore import QIODevice, QTimer
    from PySide.QtGui import *
    from PySide.QtNetwork import QLocalServer, QLocalSocket

    from main_window  import MainWindow
    from functions import *

    class MainDialog(MainWindow):
        def __init__(self, parent=None):
            super(MainDialog, self).__init__(parent)


    class QSingleApplication(QApplication):
        def singleStart(self, mainWindow):
            self.mainWindow = mainWindow
            # Socket
            self.m_socket = QLocalSocket()
            self.m_socket.connected.connect(self.connectToExistingApp)
            self.m_socket.error.connect(self.startApplication)
            self.m_socket.connectToServer(self.applicationName(), QIODevice.WriteOnly)
        def connectToExistingApp(self):
            if len(sys.argv)>1 and sys.argv[1] is not None:
                self.m_socket.write(sys.argv[1])
                self.m_socket.bytesWritten.connect(self.quit)
            else:
                logging.warning("The program is already running.")
                QMessageBox.warning(None, self.tr("Already running"), self.tr("The program is already running."))
                # Quit application in 250 ms
                QTimer.singleShot(250, self.quit)
        def startApplication(self):
            self.m_server = QLocalServer()
            if self.m_server.listen(self.applicationName()):
                self.m_server.newConnection.connect(self.getNewConnection)
                self.mainWindow.show()
            else:
                logging.warning("Error listening the socket.")
                QMessageBox.critical(None, self.tr("Error"), self.tr("Error listening the socket."))
        def getNewConnection(self):
            self.new_socket = self.m_server.nextPendingConnection()
            self.new_socket.readyRead.connect(self.readSocket)
        def readSocket(self):
            f = self.new_socket.readLine()
            self.mainWindow.getArgsFromOtherInstance(str(f))
            self.mainWindow.activateWindow()
            self.mainWindow.show()


    app = QSingleApplication(sys.argv)
    app.setApplicationName(appName)
    myWindow = MainDialog()
    app.singleStart(myWindow)
    sys.exit(app.exec_())
except Exception as e:
    print("----------------EROARE NEASHTEPTATA--------------")
    logging.debug("----------------EROARE NEASHTEPTATA--------------")
    try:
        print("Raportam eroarea")
        logging.debug("Raportam eroarea")
        postFields = {
            'app' : "BILIARD",
            'eroarea': str(e),
            'stack':traceback.format_exc()
        }
        import requests
        r = requests.post('http://develop.suav.biz/jsErrLog/',data=postFields)
        print(r.text)
        logging.debug(r.text)
        raise
    except Exception as e:
        print("NU SA PRIMIT sa raportam")
        logging.debug("NU SA PRMIT  sa raportam")
        print(e)
        logging.debug(e)
        raise