# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_by_class_base.ui'
#
# Created: Wed Dec 17 12:37:30 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LoadByClass(object):
    def setupUi(self, LoadByClass):
        LoadByClass.setObjectName(_fromUtf8("LoadByClass"))
        LoadByClass.resize(397, 441)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadByClass.sizePolicy().hasHeightForWidth())
        LoadByClass.setSizePolicy(sizePolicy)
        LoadByClass.setMinimumSize(QtCore.QSize(0, 0))
        LoadByClass.setMaximumSize(QtCore.QSize(1000, 1000))
        self.gridLayout_3 = QtGui.QGridLayout(LoadByClass)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(LoadByClass)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabSpatialite = QtGui.QWidget()
        self.tabSpatialite.setObjectName(_fromUtf8("tabSpatialite"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabSpatialite)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tabSpatialite)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spatialiteFileEdit = QtGui.QLineEdit(self.tabSpatialite)
        self.spatialiteFileEdit.setObjectName(_fromUtf8("spatialiteFileEdit"))
        self.horizontalLayout.addWidget(self.spatialiteFileEdit)
        self.pushButtonOpenFile = QtGui.QPushButton(self.tabSpatialite)
        self.pushButtonOpenFile.setObjectName(_fromUtf8("pushButtonOpenFile"))
        self.horizontalLayout.addWidget(self.pushButtonOpenFile)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.tabSpatialite)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spatialiteCrsEdit = QtGui.QLineEdit(self.tabSpatialite)
        self.spatialiteCrsEdit.setObjectName(_fromUtf8("spatialiteCrsEdit"))
        self.horizontalLayout_2.addWidget(self.spatialiteCrsEdit)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabSpatialite, _fromUtf8(""))
        self.tabPostGIS = QtGui.QWidget()
        self.tabPostGIS.setObjectName(_fromUtf8("tabPostGIS"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabPostGIS)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.tabPostGIS)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBoxPostgis = QtGui.QComboBox(self.groupBox_3)
        self.comboBoxPostgis.setObjectName(_fromUtf8("comboBoxPostgis"))
        self.verticalLayout.addWidget(self.comboBoxPostgis)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_12.addWidget(self.label_7)
        self.postGISCrsEdit = QtGui.QLineEdit(self.groupBox_3)
        self.postGISCrsEdit.setObjectName(_fromUtf8("postGISCrsEdit"))
        self.horizontalLayout_12.addWidget(self.postGISCrsEdit)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabPostGIS, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(LoadByClass)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.classesListWidget = QtGui.QListWidget(self.groupBox)
        self.classesListWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.classesListWidget.setObjectName(_fromUtf8("classesListWidget"))
        self.horizontalLayout_3.addWidget(self.classesListWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.selectAllCheck = QtGui.QCheckBox(LoadByClass)
        self.selectAllCheck.setObjectName(_fromUtf8("selectAllCheck"))
        self.verticalLayout_2.addWidget(self.selectAllCheck)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.pushButtonOk = QtGui.QPushButton(LoadByClass)
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.horizontalLayout_9.addWidget(self.pushButtonOk)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.pushButtonCancel = QtGui.QPushButton(LoadByClass)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_9.addWidget(self.pushButtonCancel)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)

        self.retranslateUi(LoadByClass)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(LoadByClass)

    def retranslateUi(self, LoadByClass):
        LoadByClass.setWindowTitle(QtGui.QApplication.translate("LoadByClass", "Load by Class", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LoadByClass", "File                    ", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOpenFile.setText(QtGui.QApplication.translate("LoadByClass", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LoadByClass", "Coordinate System", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSpatialite), QtGui.QApplication.translate("LoadByClass", "Spatialite", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("LoadByClass", "Connections", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("LoadByClass", "Coordinate System", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPostGIS), QtGui.QApplication.translate("LoadByClass", "PostGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("LoadByClass", "Select the classes", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAllCheck.setText(QtGui.QApplication.translate("LoadByClass", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setText(QtGui.QApplication.translate("LoadByClass", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(QtGui.QApplication.translate("LoadByClass", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

