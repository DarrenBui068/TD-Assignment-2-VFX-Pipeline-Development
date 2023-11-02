import os
import shutil
import maya.cmds as cmds
from maya import OpenMayaUI as omui
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

# Constants
WIP_DIRECTORY = "/path/to/WIP"
PUBLISH_DIRECTORY = "/path/to/Publish"
ASSET_TYPES = {
    "model": ["setPiece", "sets"],
    "layout": [],
    "animation": [],
    "lighting": []
}

def maya_main_window():
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QtWidgets.QWidget)

def getNextVersion(asset_name):
    # Assuming filenames are in format assetName_v01.ma, assetName_v02.ma, etc.
    version_number = 1
    while True:
        file_path = os.path.join(WIP_DIRECTORY, f"{asset_name}_v{version_number:02}.ma")
        if not os.path.exists(file_path):
            break
        version_number += 1
    return version_number

def getCurrentVersion(asset_name):
    # Returns the latest version number for a given asset
    version_number = 1
    while True:
        next_version = version_number + 1
        file_path = os.path.join(WIP_DIRECTORY, f"{asset_name}_v{next_version:02}.ma")
        if not os.path.exists(file_path):
            break
        version_number += 1
    return version_number

def saveFile(asset_name, asset_type):
    version_number = getNextVersion(asset_name)
    file_path = os.path.join(WIP_DIRECTORY, asset_type, f"{asset_name}_v{version_number:02}.ma")
    cmds.file(rename=file_path)
    cmds.file(save=True, type="mayaAscii")
    print(f"File saved to {file_path}")

def publishFile(asset_name, asset_type):
    version_number = getCurrentVersion(asset_name)
    source_file = os.path.join(WIP_DIRECTORY, asset_type, f"{asset_name}_v{version_number:02}.ma")
    publish_source_folder = os.path.join(PUBLISH_DIRECTORY, asset_type, "source")
    publish_source_file = os.path.join(publish_source_folder, f"{asset_name}_v{version_number:02}.ma")

    # Ensure publish directory exists
    if not os.path.exists(publish_source_folder):
        os.makedirs(publish_source_folder)
    
    shutil.copy2(source_file, publish_source_file)

    # Export .abc and .fbx files
    if asset_type in ["setPiece", "sets", "layout", "animation"]:
        cmds.AbcExport(j=f"-frameRange 1 120 -uvWrite -worldSpace -root {asset_name} -file {publish_source_folder}/{asset_name}_v{version_number:02}.abc")
        cmds.FbxExport(f=f"{publish_source_folder}/{asset_name}_v{version_number:02}.fbx", s=True)

    print(f"File published to source folder: {publish_source_file}")

# GUI
class SavePublishTool(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(SavePublishTool, self).__init__(parent)
        self.setWindowTitle("Save and Publish Tool")
        self.setMinimumWidth(300)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.asset_name_input = QtWidgets.QLineEdit()
        self.asset_type_combo = QtWidgets.QComboBox()
        self.asset_type_combo.addItems(["model", "layout", "animation", "lighting"])
        self.save_button = QtWidgets.QPushButton("Save")
        self.publish_button = QtWidgets.QPushButton("Publish")

    def create_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(QtWidgets.QLabel("Asset Name:"))
        layout.addWidget(self.asset_name_input)
        layout.addWidget(QtWidgets.QLabel("Asset Type:"))
        layout.addWidget(self.asset_type_combo)
        layout.addWidget(self.save_button)
        layout.addWidget(self.publish_button)

    def create_connections(self):
        self.save_button.clicked.connect(self.on_save_clicked)
        self.publish_button.clicked.connect(self.on_publish_clicked)

    def on_save_clicked(self):
        asset_name = self.asset_name_input.text()
        asset_type = self.asset_type_combo.currentText()
        saveFile(asset_name, asset_type)

    def on_publish_clicked(self):
        asset_name = self.asset_name_input.text()
        asset_type = self.asset_type_combo.currentText()
        publishFile(asset_name, asset_type)

# Show GUI
if "save_publish_tool" in globals():
    try:
        save_publish_tool.close()
        save_publish_tool.deleteLater()
    except:
        pass
    
save_publish_tool = SavePublishTool()
save_publish_tool.show()
