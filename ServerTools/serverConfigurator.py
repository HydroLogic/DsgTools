# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DsgTools
                                 A QGIS plugin
 Brazilian Army Cartographic Production Tools
                              -------------------
        begin                : 2014-11-08
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Luiz Andrade - Cartographic Engineer @ Brazilian Army
        email                : luiz.claudio@dsg.eb.mil.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, uic
import os

from ui_serverConfigurator import Ui_Dialog

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui_serverConfigurator.ui'))

class ServerConfigurator(QDialog, FORM_CLASS):
    def __init__(self, iface):
        """Constructor."""
        super(ServerConfigurator, self).__init__()
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.iface = iface
        self.isEdit = 0
        self.oldName=''

        #self.populateServersCombo()

        self.passwordEdit.setEchoMode(QLineEdit.Password)

    @pyqtSlot(bool)
    def on_saveButton_clicked(self):
        if self.checkFields():
            name = self.servEdit.text()
            host = self.hostEdit.text()
            port = self.portEdit.text()
            user = self.userEdit.text()
            password = self.passwordEdit.text()
            if not self.storeServerConfiguration(name, host, port, user, password):
                return
#             self.populateServersCombo()
            QMessageBox.warning(self, self.tr("Info!"), self.tr("Server stored."))
            self.done(1)
        else:
            QMessageBox.warning(self, self.tr("Warning!"), self.tr("Fill all parameters."))
        

    @pyqtSlot(bool)
    def on_cancelButton_clicked(self):
        self.done(0)

#     @pyqtSlot(bool)
#     def on_removeButton_clicked(self):
#         self.removeServerConfiguration()
#         self.populateServersCombo()
#         QMessageBox.warning(self, self.tr("Info!"), self.tr("Server removed."))

#     def on_serversCombo_currentIndexChanged(self, index):
#         self.getServerConfiguration(self.serversCombo.currentText())

    def checkFields(self):
        if self.hostEdit.text() == '' or self.portEdit.text() == '' \
            or self.userEdit.text() == '' or self.passwordEdit.text() == '':
            return False
        return True

    def storeServerConfiguration(self, name, host, port, user, password):
        settings = QSettings()
        if self.isEdit:
            settings.beginGroup('PostgreSQL/servers/'+self.oldName)
            settings.remove('')
            settings.endGroup()
        else:
            if settings.contains('PostgreSQL/servers/'+name+'/host'):
                QMessageBox.warning(self, self.tr("Warning!"), self.tr("Already has a server with this name."))
                self.servEdit.setStyleSheet('background-color: rgb(255, 150, 150)')
                return 0
        settings.beginGroup('PostgreSQL/servers/'+name)
        settings.setValue('host', host)
        settings.setValue('port', port)
        settings.setValue('username', user)
        settings.setValue('password', password)
        settings.endGroup()
        return 1

#     def removeServerConfiguration(self):
#         settings = QSettings()
#         settings.beginGroup('PostgreSQL/servers/'+self.serversCombo.currentText())
#         settings.remove('')
#         settings.endGroup()

    def setServerConfiguration(self, name):
        self.isEdit = 1
        self.oldName=name
        settings = QSettings()
        settings.beginGroup('PostgreSQL/servers/'+name)
        host = settings.value('host')
        port = settings.value('port')
        user = settings.value('username')
        password = settings.value('password')
        settings.endGroup()

        self.servEdit.setText(name)
        self.hostEdit.setText(host)
        self.portEdit.setText(port)
        self.userEdit.setText(user)
        self.passwordEdit.setText(password)

#     def getServers(self):
#         settings = QSettings()
#         settings.beginGroup('PostgreSQL/servers')
#         currentConnections = settings.childGroups()
#         settings.endGroup()
#         return currentConnections

#     def populateServersCombo(self):
#         self.serversCombo.clear()
#         currentConnections = self.getServers()
#         for connection in currentConnections:
#             self.serversCombo.addItem(connection)
