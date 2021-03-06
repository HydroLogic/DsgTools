# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LoadByClass
                                 A QGIS plugin
 Load database classes.
                             -------------------
        begin                : 2014-06-17
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Philipe Borba - Cartographic Engineer @ Brazilian Army
        email                : borba@dsg.eb.mil.br
        mod history          : 2014-12-17 by Luiz Andrade - Cartographic Engineer @ Brazilian Army
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
import load_by_class_base

from qgis.core import QgsCoordinateReferenceSystem,QgsDataSourceURI,QgsVectorLayer,QgsMapLayerRegistry,QgsMessageLog
from qgis.gui import QgsMessageBar

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot, Qt
from PyQt4.QtSql import QSqlQuery
from PyQt4.QtGui import QApplication, QCursor

import os
from DsgTools.Utils.utils import Utils
from DsgTools.Factories.SqlFactory.sqlGeneratorFactory import SqlGeneratorFactory

class LoadByClass(QtGui.QDialog, load_by_class_base.Ui_LoadByClass):
    def __init__(self, parent=None):
        """Constructor."""
        super(LoadByClass, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.filename = ""
        self.dbLoaded = False
        self.epsg = 0
        self.crs = None
        self.selectedClasses = []

        #Sql factory generator
        self.isSpatialite = True

        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.factory = SqlGeneratorFactory()
        self.gen = self.factory.createSqlGenerator(self.isSpatialite)
        self.utils = Utils()

        self.bar = QgsMessageBar()
        self.setLayout(QtGui.QGridLayout(self))
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.bar.setSizePolicy(sizePolicy)
        self.layout().addWidget(self.bar, 0,0,1,1)

        #Objects Connections
        QtCore.QObject.connect(self.pushButtonOpenFile, QtCore.SIGNAL(("clicked()")), self.loadDatabase)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL(("clicked()")), self.cancel)
        QtCore.QObject.connect(self.selectAllCheck, QtCore.SIGNAL(("stateChanged(int)")), self.selectAll)
        QtCore.QObject.connect(self.pushButtonOk, QtCore.SIGNAL(("clicked()")), self.okSelected)
        QtCore.QObject.connect(self.tabWidget,QtCore.SIGNAL(("currentChanged(int)")), self.restoreInitialState)

        self.db = None
        #populating the postgis combobox
        self.populatePostGISConnectionsCombo()

    def __del__(self):
        self.closeDatabase()

    def closeDatabase(self):
        if self.db:
            self.db.close()
            self.db = None

    def restoreInitialState(self):
        self.filename = ""
        self.dbLoaded = False
        self.epsg = 0
        self.crs = None
        self.selectedClasses = []
        self.spatialiteFileEdit.setText(self.filename)
        self.postGISCrsEdit.setText('')
        self.postGISCrsEdit.setReadOnly(True)
        self.spatialiteCrsEdit.setText('')
        self.spatialiteCrsEdit.setReadOnly(True)

        tam = self.classesListWidget.__len__()
        for i in range(tam+1,1,-1):
            item = self.classesListWidget.takeItem(i-2)

        self.selectAllCheck.setCheckState(0)
        #Setting the database type
        if self.tabWidget.currentIndex() == 0:
            self.isSpatialite = True
        else:
            self.isSpatialite = False
        #getting the sql generator according to the database type
        self.gen = self.factory.createSqlGenerator(self.isSpatialite)
        self.comboBoxPostgis.setCurrentIndex(0)

    def updateBDField(self):
        if self.dbLoaded == True:
            self.spatialiteFileEdit.setText(self.filename)
        else:
            self.filename = ""
            self.spatialiteFileEdit.setText(self.filename)

    def getDatabaseVersion(self):
        self.dbVersion = self.utils.getDatabaseVersion(self.db)
        self.qmlPath = self.utils.getQmlDir(self.db)

    def listClassesFromDatabase(self):
        self.classesListWidget.clear()
        self.getDatabaseVersion()
        sql = self.gen.getTablesFromDatabase()
        query = QSqlQuery(sql, self.db)
        while query.next():
            if self.isSpatialite:
                tableName = query.value(0)
                layerName = tableName
            else:
                tableSchema = query.value(0)
                tableName = query.value(1)
                layerName = tableSchema+'.'+tableName
            if tableName.split("_")[-1] == "p" or tableName.split("_")[-1] == "l" \
                or tableName.split("_")[-1] == "a":

                item = QtGui.QListWidgetItem(layerName)
                self.classesListWidget.addItem(item)
        self.classesListWidget.sortItems()
        self.setCRS()

    def setCRS(self):
        try:
            self.epsg = self.utils.findEPSG(self.db)
            if self.epsg == -1:
                self.bar.pushMessage("", self.tr("Coordinate Reference System not set or invalid!"), level=QgsMessageBar.WARNING)
            else:
                self.crs = QgsCoordinateReferenceSystem(self.epsg, QgsCoordinateReferenceSystem.EpsgCrsId)
                if self.isSpatialite:
                    self.spatialiteCrsEdit.setText(self.crs.description())
                    self.spatialiteCrsEdit.setReadOnly(True)
                else:
                    self.postGISCrsEdit.setText(self.crs.description())
                    self.postGISCrsEdit.setReadOnly(True)
        except:
            pass

    @pyqtSlot(int)
    def on_comboBoxPostgis_currentIndexChanged(self):
        if self.comboBoxPostgis.currentIndex() > 0:
            self.loadDatabase()

    def loadDatabase(self):
        self.closeDatabase()
        if self.isSpatialite:
            (self.filename, self.db) = self.utils.getSpatialiteDatabase()
            if self.filename:
                self.spatialiteFileEdit.setText(self.filename)
        else:
            self.db = self.utils.getPostGISDatabase(self.comboBoxPostgis.currentText())
        try:
            if not self.db.open():
                QgsMessageLog.logMessage(self.db.lastError().text(), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
            else:
                self.dbLoaded = True
                self.listClassesFromDatabase()
        except:
            pass

    def populatePostGISConnectionsCombo(self):
        self.comboBoxPostgis.clear()
        self.comboBoxPostgis.addItem(self.tr("Select Database"))
        self.comboBoxPostgis.addItems(self.utils.getPostGISConnections())

    def cancel(self):
        self.restoreInitialState()
        self.close()

    def selectAll(self):
        if self.selectAllCheck.isChecked():
            tam = self.classesListWidget.__len__()
            for i in range(tam+1):
                item = self.classesListWidget.item(i-1)
                self.classesListWidget.setItemSelected(item,2)

        else:
            tam = self.classesListWidget.__len__()
            for i in range(tam+1):
                item = self.classesListWidget.item(i-1)
                self.classesListWidget.setItemSelected(item,0)

    def getSelectedItems(self):
        lista = self.classesListWidget.selectedItems()
        self.selectedClasses = []
        tam = len(lista)
        for i in range(tam):
            self.selectedClasses.append(lista[i].text())
        self.selectedClasses.sort()

    def okSelected(self):
        try:
            QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
            if self.isSpatialite:
                self.loadSpatialiteLayers()
            else:
                self.loadPostGISLayers()
            QApplication.restoreOverrideCursor()
        except:
            QApplication.restoreOverrideCursor()

    def loadPostGISLayers(self):
        self.getSelectedItems()
        (database, host, port, user, password) = self.utils.getPostGISConnectionParameters(self.comboBoxPostgis.currentText())
        uri = QgsDataSourceURI()
        uri.setConnection(str(host),str(port), str(database), str(user), str(password))
        if len(self.selectedClasses)>0:
            try:
                geom_column = 'geom'
                for layer in self.selectedClasses:
                    split = layer.split('.')
                    schema = split[0]
                    layerName = split[1]
                    sql = self.gen.loadLayerFromDatabase(layer)
                    uri.setDataSource(schema, layerName, geom_column, sql,'id')
                    uri.disableSelectAtId(True)
                    self.loadEDGVLayer(uri, layerName, 'postgres')
                self.restoreInitialState()
                self.close()
            except:
                self.bar.pushMessage(self.tr("Error!"), self.tr("Could not load the selected classes!"), level=QgsMessageBar.CRITICAL)
        else:
            self.bar.pushMessage(self.tr("Warning!"), self.tr("Please, select at least one class!"), level=QgsMessageBar.WARNING)

    def loadSpatialiteLayers(self):
        self.getSelectedItems()
        uri = QgsDataSourceURI()
        uri.setDatabase(self.filename)
        schema = ''
        geom_column = 'GEOMETRY'
        if len(self.selectedClasses)>0:
            try:
                for layer_name in self.selectedClasses:
                    uri.setDataSource(schema, layer_name, geom_column)
                    self.loadEDGVLayer(uri, layer_name, 'spatialite')
                self.restoreInitialState()
                self.close()
            except:
                self.bar.pushMessage(self.tr("Error!"), self.tr("Could not load the layer(s)!"), level=QgsMessageBar.CRITICAL)
        else:
            self.bar.pushMessage(self.tr("Warning!"), self.tr("Please select at least one layer!"), level=QgsMessageBar.WARNING)

    def loadEDGVLayer(self, uri, layer_name, provider):
        vlayer = QgsVectorLayer(uri.uri(), layer_name, provider)
        vlayer.setCrs(self.crs)
        QgsMapLayerRegistry.instance().addMapLayer(vlayer) #added due to api changes
        if self.isSpatialite and (self.dbVersion == '3.0' or self.dbVersion == '2.1.3'):
            lyr = '_'.join(layer_name.replace('\r', '').split('_')[1::])
        else:
            lyr = layer_name.replace('\r','')
        vlayerQml = os.path.join(self.qmlPath, lyr+'.qml')
        vlayer.loadNamedStyle(vlayerQml, False)
        QgsMapLayerRegistry.instance().addMapLayer(vlayer)
        if not vlayer.isValid():
            QgsMessageLog.logMessage(vlayer.error().summary(), "DSG Tools Plugin", QgsMessageLog.CRITICAL)
