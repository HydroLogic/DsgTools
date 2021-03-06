 SOURCES         =	BDGExTools/BDGExTools.py \
 					ComplexTools/complexWindow.py \
 					ComplexTools/manageComplex.py \
 					DbTools/PostGISTool/postgisDBTool.py \
 					DbTools/SpatialiteTool/cria_spatialite_dialog.py \
 					Factories/ThreadFactory/dpiThread.py \
 					Factories/ThreadFactory/postgisDbThread.py \
 					ImageTools/processingTools.py \
 					LayerTools/load_by_category.py \
 					LayerTools/load_by_class.py \
 					LayerTools/ui_create_inom_dialog.py \
 					ProcessingTools/processManager.py \
 					QmlTools/qmlParser.py \
 					ServerTools/serverConfigurator.py \
 					ServerTools/viewServers.py \
 					dsg_tools.py

 FORMS           =	ComplexTools/complexWindow_base.ui \
 					ComplexTools/ui_manageComplex.ui \
 					DbTools/PostGISTool/ui_postgisDBTool.ui \
 					DbTools/SpatialiteTool/cria_spatialite_dialog_base.ui \
 					ImageTools/ui_processingTools.ui \
 					LayerTools/load_by_category_dialog.ui \
 					LayerTools/load_by_class_base.ui \
 					LayerTools/ui_create_inom_dialog_base.ui \
 					ServerTools/ui_serverConfigurator.ui \
 					ServerTools/ui_viewServers.ui \
 					ui_about.ui

 TRANSLATIONS    = i18n/DsgTools_pt.ts

RESOURCES += \
    resources.qrc
