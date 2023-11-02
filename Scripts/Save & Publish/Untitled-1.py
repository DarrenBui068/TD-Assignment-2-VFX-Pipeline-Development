import os
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from PySide2 import QtWidgets, QtGui
from shiboken2 import wrapInstance

def maya_main_window():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QtWidgets.QWidget)

class ImportExportTool(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(ImportExportTool, self).__init__(parent)
        
        self.setWindowTitle("Import & Export Tool")
        self.setMinimumWidth(400)
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setPlaceholderText("Search for files (e.g. .abc, .fbx, filename)")
        
        self.info_label = QtWidgets.QLabel("")
        self.import_button = QtWidgets.QPushButton("Import File")
        self.export_button = QtWidgets.QPushButton("Export Multiple Files")
        
    def create_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.search_bar)
        layout.addWidget(self.info_label)
        layout.addWidget(self.import_button)
        layout.addWidget(self.export_button)

    def create_connections(self):
        self.import_button.clicked.connect(self.import_file)
        self.export_button.clicked.connect(self.export_file)

    def import_file(self):
        filter_text = self.search_bar.text()
        file_path = cmds.fileDialog2(fileMode=1, caption="Select File to Import", fileFilter=filter_text)
        if file_path:
            try:
                cmds.file(file_path[0], i=True)
                self.show_dialog("Import Successful!", f"File '{os.path.basename(file_path[0])}' has been imported successfully.\nFormat: {os.path.splitext(file_path[0])[1]}\nLocation: {file_path[0]}")
            except Exception as e:
                self.show_dialog("Import Failed!", str(e))

    def export_file(self):
        filter_text = self.search_bar.text()
        file_paths = cmds.fileDialog2(fileMode=3, caption="Save Files", fileFilter=filter_text)
        if file_paths:
            for file_path in file_paths:
                try:
                    cmds.file(rename=file_path)
                    cmds.file(save=True, type="mayaBinary", force=True)
                    self.show_dialog("Export Successful!", f"File '{os.path.basename(file_path)}' has been exported successfully.\nFormat: {os.path.splitext(file_path)[1]}\nLocation: {file_path}")
                except Exception as e:
                    self.show_dialog("Export Failed!", str(e))

    def show_dialog(self, title, message):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

if "import_export_tool" in globals():
    try:
        import_export_tool.close()
        import_export_tool.deleteLater()
    except:
        pass

import_export_tool = ImportExportTool()
import_export_tool.show()
