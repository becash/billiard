#!/usr/bin/env python

import sys

from PySide import QtCore, QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.settingsTree = SettingsTree()
        self.setCentralWidget(self.settingsTree)

        self.locationDialog = None

        # self.createActions()
        # self.createMenus()

        # self.autoRefreshAct.setChecked(True)
        # self.fallbacksAct.setChecked(True)

        self.setWindowTitle("Settings Editor")
        self.resize(500, 600)


        settings = QtCore.QSettings("config.ini", QtCore.QSettings.IniFormat)
        self.setSettingsObject(settings)
        # self.fallbacksAct.setEnabled(False)


    def openPropertyList(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                "Open Property List", '', "Property List Files (*.plist)")

        if fileName:
            settings = QtCore.QSettings(fileName, QtCore.QSettings.NativeFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled(False)

    def openRegistryPath(self):
        path, ok = QtGui.QInputDialog.getText(self, "Open Registry Path",
                "Enter the path in the Windows registry:",
                QtGui.QLineEdit.Normal, 'HKEY_CURRENT_USER\\')

        if ok and path != '':
            settings = QtCore.QSettings(path, QtCore.QSettings.NativeFormat)
            self.setSettingsObject(settings)
            self.fallbacksAct.setEnabled(False)

    def about(self):
        QtGui.QMessageBox.about(self, "About Settings Editor",
                "The <b>Settings Editor</b> example shows how to access "
                "application settings using Qt.")

    def createActions(self):
        self.openSettingsAct = QtGui.QAction("&Open Application Settings...",
                self, shortcut="Ctrl+O", triggered=self.openSettings)

        self.openIniFileAct = QtGui.QAction("Open I&NI File...", self,
                shortcut="Ctrl+N", triggered=self.openIniFile)

        self.openPropertyListAct = QtGui.QAction("Open Mac &Property List...",
                self, shortcut="Ctrl+P", triggered=self.openPropertyList)
        if sys.platform != 'darwin':
            self.openPropertyListAct.setEnabled(False)

        self.openRegistryPathAct = QtGui.QAction(
                "Open Windows &Registry Path...", self, shortcut="Ctrl+G",
                triggered=self.openRegistryPath)
        if sys.platform != 'win32':
            self.openRegistryPathAct.setEnabled(False)

        self.refreshAct = QtGui.QAction("&Refresh", self, shortcut="Ctrl+R",
                enabled=False, triggered=self.settingsTree.refresh)

        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.autoRefreshAct = QtGui.QAction("&Auto-Refresh", self,
                shortcut="Ctrl+A", checkable=True, enabled=False)
        self.autoRefreshAct.triggered.connect(self.settingsTree.setAutoRefresh)
        self.autoRefreshAct.triggered.connect(self.refreshAct.setDisabled)

        self.fallbacksAct = QtGui.QAction("&Fallbacks", self,
                shortcut="Ctrl+F", checkable=True, enabled=False,
                triggered=self.settingsTree.setFallbacksEnabled)

        self.aboutAct = QtGui.QAction("&About", self, triggered=self.about)

        self.aboutQtAct = QtGui.QAction("About &Qt", self,
                triggered=QtGui.qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.openSettingsAct)
        self.fileMenu.addAction(self.openIniFileAct)
        self.fileMenu.addAction(self.openPropertyListAct)
        self.fileMenu.addAction(self.openRegistryPathAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.refreshAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.optionsMenu = self.menuBar().addMenu("&Options")
        self.optionsMenu.addAction(self.autoRefreshAct)
        self.optionsMenu.addAction(self.fallbacksAct)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def setSettingsObject(self, settings):
        # settings.setFallbacksEnabled(self.fallbacksAct.isChecked())
        self.settingsTree.setSettingsObject(settings)

        # self.refreshAct.setEnabled(True)
        # self.autoRefreshAct.setEnabled(True)

        # niceName = settings.fileName()
        # niceName.replace('\\', '/')
        # niceName = niceName.split('/')[-1]
        #
        # if not settings.isWritable():
        #     niceName += " (read only)"
        #
        # self.setWindowTitle("%s - Settings Editor" % niceName)

class SettingsTree(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        super(SettingsTree, self).__init__(parent)

        self.setItemDelegate(VariantDelegate(self))

        self.setHeaderLabels(("Setting", "", "Value"))
        self.header().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.header().setResizeMode(2, QtGui.QHeaderView.Stretch)
        self.hideColumn(1)

        self.settings = None
        self.refreshTimer = QtCore.QTimer()
        self.refreshTimer.setInterval(2000)
        self.autoRefresh = False

        self.groupIcon = QtGui.QIcon()
        self.groupIcon.addPixmap(self.style().standardPixmap(QtGui.QStyle.SP_DirClosedIcon),
                QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.groupIcon.addPixmap(self.style().standardPixmap(QtGui.QStyle.SP_DirOpenIcon),
                QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.keyIcon = QtGui.QIcon()
        self.keyIcon.addPixmap(self.style().standardPixmap(QtGui.QStyle.SP_FileIcon))

        self.refreshTimer.timeout.connect(self.maybeRefresh)

    def setSettingsObject(self, settings):
        self.settings = settings
        self.clear()

        if self.settings is not None:
            self.settings.setParent(self)
            self.refresh()
            if self.autoRefresh:
                self.refreshTimer.start()
        else:
            self.refreshTimer.stop()

    def sizeHint(self):
        return QtCore.QSize(800, 600)

    def setAutoRefresh(self, autoRefresh):
        self.autoRefresh = autoRefresh

        if self.settings is not None:
            if self.autoRefresh:
                self.maybeRefresh()
                self.refreshTimer.start()
            else:
                self.refreshTimer.stop()

    def setFallbacksEnabled(self, enabled):
        if self.settings is not None:
            self.settings.setFallbacksEnabled(enabled)
            self.refresh()

    def maybeRefresh(self):
        if self.state() != QtGui.QAbstractItemView.EditingState:
            self.refresh()

    def refresh(self):
        if self.settings is None:
            return

        # The signal might not be connected.
        try:
            self.itemChanged.disconnect(self.updateSetting)
        except:
            pass

        self.settings.sync()
        self.updateChildItems(None)

        self.itemChanged.connect(self.updateSetting)

    def event(self, event):
        if event.type() == QtCore.QEvent.WindowActivate:
            if self.isActiveWindow() and self.autoRefresh:
                self.maybeRefresh()

        return super(SettingsTree, self).event(event)



    def updateSetting(self, item):
        key = item.text(0)
        ancestor = item.parent()

        while ancestor:
            key = ancestor.text(0) + '/' + key
            ancestor = ancestor.parent()

        d = item.data(2, QtCore.Qt.UserRole)
        if key[-2:]=="__" :
            value = item.data(2, QtCore.Qt.UserRole)




        else:
            value = item.data(2, QtCore.Qt.UserRole)

        self.settings.setValue(key, value)

        if self.autoRefresh:
            self.refresh()

    def updateChildItems(self, parent):
        dividerIndex = 0

        for group in self.settings.childGroups():
            childIndex = self.findChild(parent, group, dividerIndex)
            if childIndex != -1:
                child = self.childAt(parent, childIndex)
                child.setText(1, '')
                child.setText(2, '')
                child.setData(2, QtCore.Qt.UserRole, None)
                self.moveItemForward(parent, childIndex, dividerIndex)
            else:
                child = self.createItem(group, parent, dividerIndex)

            child.setIcon(0, self.groupIcon)
            dividerIndex += 1

            self.settings.beginGroup(group)
            self.updateChildItems(child)
            self.settings.endGroup()

        for key in self.settings.childKeys():
            childIndex = self.findChild(parent, key, 0)
            if childIndex == -1 or childIndex >= dividerIndex:
                if childIndex != -1:
                    child = self.childAt(parent, childIndex)
                    for i in range(child.childCount()):
                        self.deleteItem(child, i)
                    self.moveItemForward(parent, childIndex, dividerIndex)
                else:
                    child = self.createItem(key, parent, dividerIndex)
                child.setIcon(0, self.keyIcon)
                dividerIndex += 1
            else:
                child = self.childAt(parent, childIndex)

            value = self.settings.value(key)
            if value is None:
                child.setText(1, 'Invalid')
            else:
                child.setText(1, value.__class__.__name__)
            child.setText(2, VariantDelegate.displayText(value))
            child.setData(2, QtCore.Qt.UserRole, value)

        while dividerIndex < self.childCount(parent):
            self.deleteItem(parent, dividerIndex)

    def createItem(self, text, parent, index):
        after = None

        if index != 0:
            after = self.childAt(parent, index - 1)

        if parent is not None:
            item = QtGui.QTreeWidgetItem(parent, after)
        else:
            item = QtGui.QTreeWidgetItem(self, after)

        item.setText(0, text)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        return item


    def childAt(self, parent, index):
        if parent is not None:
            return parent.child(index)
        else:
            return self.topLevelItem(index)

    def childCount(self, parent):
        if parent is not None:
            return parent.childCount()
        else:
            return self.topLevelItemCount()

    def findChild(self, parent, text, startIndex):
        for i in range(self.childCount(parent)):
            if self.childAt(parent, i).text(0) == text:
                return i
        return -1

    def moveItemForward(self, parent, oldIndex, newIndex):
        for int in range(oldIndex - newIndex):
            self.deleteItem(parent, newIndex)

class VariantDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        super(VariantDelegate, self).__init__(parent)

        self.boolExp = QtCore.QRegExp()
        self.boolExp.setPattern('true|false')
        self.boolExp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)

        self.byteArrayExp = QtCore.QRegExp()
        self.byteArrayExp.setPattern('[\\x00-\\xff]*')

        self.charExp = QtCore.QRegExp()
        self.charExp.setPattern('.')

        self.colorExp = QtCore.QRegExp()
        self.colorExp.setPattern('\\(([0-9]*),([0-9]*),([0-9]*),([0-9]*)\\)')

        self.doubleExp = QtCore.QRegExp()
        self.doubleExp.setPattern('')

        self.pointExp = QtCore.QRegExp()
        self.pointExp.setPattern('\\((-?[0-9]*),(-?[0-9]*)\\)')

        self.rectExp = QtCore.QRegExp()
        self.rectExp.setPattern('\\((-?[0-9]*),(-?[0-9]*),(-?[0-9]*),(-?[0-9]*)\\)')

        self.signedIntegerExp = QtCore.QRegExp()
        self.signedIntegerExp.setPattern('-?[0-9]*')

        self.sizeExp = QtCore.QRegExp(self.pointExp)

        self.unsignedIntegerExp = QtCore.QRegExp()
        self.unsignedIntegerExp.setPattern('[0-9]*')

        self.dateExp = QtCore.QRegExp()
        self.dateExp.setPattern('([0-9]{,4})-([0-9]{,2})-([0-9]{,2})')

        self.timeExp = QtCore.QRegExp()
        self.timeExp.setPattern('([0-9]{,2}):([0-9]{,2}):([0-9]{,2})')

        self.dateTimeExp = QtCore.QRegExp()
        self.dateTimeExp.setPattern(self.dateExp.pattern() + 'T' + self.timeExp.pattern())

    def paint(self, painter, option, index):
        if index.column() == 2:
            value = index.model().data(index, QtCore.Qt.UserRole)
            if not self.isSupportedType(value):
                myOption = QtGui.QStyleOptionViewItem(option)
                myOption.state &= ~QtGui.QStyle.State_Enabled
                super(VariantDelegate, self).paint(painter, myOption, index)
                return

        super(VariantDelegate, self).paint(painter, option, index)

    def createEditor(self, parent, option, index):
        if index.column() != 2:
            return None

        originalValue = index.model().data(index, QtCore.Qt.UserRole)
        if not self.isSupportedType(originalValue):
            return None

        lineEdit = QtGui.QLineEdit(parent)
        lineEdit.setFrame(False)

        if isinstance(originalValue, bool):
            regExp = self.boolExp
        elif isinstance(originalValue, float):
            regExp = self.doubleExp
        elif isinstance(originalValue, int):
            regExp = self.signedIntegerExp
        elif isinstance(originalValue, QtCore.QByteArray):
            regExp = self.byteArrayExp
        elif isinstance(originalValue, QtGui.QColor):
            regExp = self.colorExp
        elif isinstance(originalValue, QtCore.QDate):
            regExp = self.dateExp
        elif isinstance(originalValue, QtCore.QDateTime):
            regExp = self.dateTimeExp
        elif isinstance(originalValue, QtCore.QTime):
            regExp = self.timeExp
        elif isinstance(originalValue, QtCore.QPoint):
            regExp = self.pointExp
        elif isinstance(originalValue, QtCore.QRect):
            regExp = self.rectExp
        elif isinstance(originalValue, QtCore.QSize):
            regExp = self.sizeExp
        else:
            regExp = QtCore.QRegExp()

        if not regExp.isEmpty():
            validator = QtGui.QRegExpValidator(regExp, lineEdit)
            lineEdit.setValidator(validator)

        return lineEdit

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.UserRole)
        if editor is not None:
            editor.setText(self.displayText(value))

    def setModelData(self, editor, model, index):
        if not editor.isModified():
            return

        text = editor.text()
        validator = editor.validator()
        if validator is not None:
            state, text, _ = validator.validate(text, 0)
            if state != QtGui.QValidator.Acceptable:
                return

        originalValue = index.model().data(index, QtCore.Qt.UserRole)

        if isinstance(originalValue, QtGui.QColor):
            self.colorExp.exactMatch(text)
            value = QtGui.QColor(min(int(self.colorExp.cap(1)), 255),
                                 min(int(self.colorExp.cap(2)), 255),
                                 min(int(self.colorExp.cap(3)), 255),
                                 min(int(self.colorExp.cap(4)), 255))
        elif isinstance(originalValue, QtCore.QDate):
            value = QtCore.QDate.fromString(text, QtCore.Qt.ISODate)
            if not value.isValid():
                return
        elif isinstance(originalValue, QtCore.QDateTime):
            value = QtCore.QDateTime.fromString(text, QtCore.Qt.ISODate)
            if not value.isValid():
                return
        elif isinstance(originalValue, QtCore.QTime):
            value = QtCore.QTime.fromString(text, QtCore.Qt.ISODate)
            if not value.isValid():
                return
        elif isinstance(originalValue, QtCore.QPoint):
            self.pointExp.exactMatch(text)
            value = QtCore.QPoint(int(self.pointExp.cap(1)),
                                  int(self.pointExp.cap(2)))
        elif isinstance(originalValue, QtCore.QRect):
            self.rectExp.exactMatch(text)
            value = QtCore.QRect(int(self.rectExp.cap(1)),
                                 int(self.rectExp.cap(2)),
                                 int(self.rectExp.cap(3)),
                                 int(self.rectExp.cap(4)))
        elif isinstance(originalValue, QtCore.QSize):
            self.sizeExp.exactMatch(text)
            value = QtCore.QSize(int(self.sizeExp.cap(1)),
                                 int(self.sizeExp.cap(2)))
        elif isinstance(originalValue, list):
            value = text.split(',')
        else:
            value =type(originalValue)(text)

        model.setData(index, self.displayText(value), QtCore.Qt.DisplayRole)
        model.setData(index, value, QtCore.Qt.UserRole)

    @staticmethod
    def isSupportedType(value):
        return isinstance(value, (bool, float, int, QtCore.QByteArray,
                str, QtGui.QColor, QtCore.QDate, QtCore.QDateTime,
                QtCore.QTime, QtCore.QPoint, QtCore.QRect, QtCore.QSize,
                list))

    @staticmethod
    def displayText(value):
        if isinstance(value, (bool, int, QtCore.QByteArray)):
            return str(value)
        if isinstance(value, str):
            return value
        elif isinstance(value, float):
            return '%g' % value
        elif isinstance(value, QtGui.QColor):
            return '(%u,%u,%u,%u)' % (value.red(), value.green(), value.blue(), value.alpha())
        elif isinstance(value, (QtCore.QDate, QtCore.QDateTime, QtCore.QTime)):
            return value.toString(QtCore.Qt.ISODate)
        elif isinstance(value, QtCore.QPoint):
            return '(%d,%d)' % (value.x(), value.y())
        elif isinstance(value, QtCore.QRect):
            return '(%d,%d,%d,%d)' % (value.x(), value.y(), value.width(), value.height())
        elif isinstance(value, QtCore.QSize):
            return '(%d,%d)' % (value.width(), value.height())
        elif isinstance(value, list):
            return ','.join(value)
        elif value is None:
            return '<Invalid>'

        return '<%s>' % value


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
