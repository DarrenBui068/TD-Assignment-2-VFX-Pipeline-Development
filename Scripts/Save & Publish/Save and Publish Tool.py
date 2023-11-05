import os
import re
from maya import cmds
from PySide2 import QtWidgets, QtCore

def maya_main_window():
    from maya import OpenMayaUI as omui
    from shiboken2 import wrapInstance
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class SaveTool(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(SaveTool, self).__init__(parent)
        self.setWindowTitle("Save Tool")
        self.setMinimumWidth(400)
        self.default_directory = r"C:\Users\ASUS\Desktop\TD-Assignment-2-VFX-Pipeline-Development"
        self.current_directory = self.default_directory
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.update_directory()  # Initialize the directory to default

    def create_widgets(self):
        self.save_button = QtWidgets.QPushButton("Save")
        self.auto_save_button = QtWidgets.QPushButton("Auto Save")
        self.publish_radio = QtWidgets.QRadioButton("Publish")
        self.wip_radio = QtWidgets.QRadioButton("WIP")
        self.wip_radio.setChecked(True)  # Set WIP as the default selection
        self.assets_combo = QtWidgets.QComboBox()
        self.subfolder_combo = QtWidgets.QComboBox()
        self.status_label = QtWidgets.QLabel("")
        self.new_folder_name_line_edit = QtWidgets.QLineEdit()
        self.create_folder_button = QtWidgets.QPushButton("Create Folder")
        self.publish_button = QtWidgets.QPushButton("Publish")

    def create_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.save_button)
        layout.addWidget(self.auto_save_button)
        layout.addWidget(self.publish_button)

        auto_save_layout = QtWidgets.QFormLayout()
        auto_save_layout.addRow("Publish:", self.publish_radio)
        auto_save_layout.addRow("WIP:", self.wip_radio)
        auto_save_layout.addRow("Assets:", self.assets_combo)
        auto_save_layout.addRow("Subfolder:", self.subfolder_combo)
        layout.addLayout(auto_save_layout)

        create_folder_layout = QtWidgets.QHBoxLayout()
        create_folder_layout.addWidget(self.new_folder_name_line_edit)
        create_folder_layout.addWidget(self.create_folder_button)
        layout.addLayout(create_folder_layout)

        layout.addWidget(self.status_label)

    def create_connections(self):
        self.save_button.clicked.connect(self.save_file)
        self.auto_save_button.clicked.connect(self.auto_save_file)
        self.publish_radio.toggled.connect(self.update_directory)
        self.wip_radio.toggled.connect(self.update_directory)
        self.assets_combo.currentIndexChanged.connect(self.update_subfolders)
        self.create_folder_button.clicked.connect(self.create_folder)
        self.publish_button.clicked.connect(self.publish_assets)
    def publish_assets(self):
        # 这里插入你的导出逻辑
        selected_objs = cmds.ls(selection=True)
        
        if not selected_objs:
            self.status_label.setText("Error: No assets selected for export.")
            return
        
        export_path = os.path.join(self.default_directory, "Publish")

        if not os.path.exists(export_path):
            os.makedirs(export_path)
        
        for obj in selected_objs:
            # 这里我用了类似你提供的版本控制逻辑来避免覆盖已有文件
            version = 1
            while True:
                abc_file = os.path.join(export_path, f"{obj}_v{version}.abc")
                if not os.path.exists(abc_file):
                    break
                version += 1
            
            # 将选择的对象导出为Alembic文件
            cmds.AbcExport(j='-frameRange 1 1 -root {0} -file {1}'.format(obj, abc_file))
        
        self.status_label.setText("Publish Complete!")

    def save_file(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", self.current_directory, "All Files (*.*);;")

        if file_path:
            self.save_scene(file_path)

    def auto_save_file(self):
        # Use the selected object's name in Maya as the base for the file name
        selection = cmds.ls(selection=True)
        if not selection:
            self.status_label.setText("Error: No object selected in Maya.")
            return

        base_name = selection[0]  # Take the first selected object name
        base_name = re.sub(r'_v\d+', '', base_name)  # Remove any existing version numbers

        asset_type = self.assets_combo.currentText()
        subfolder = self.subfolder_combo.currentText()
        folder_path = self.construct_folder_path(asset_type, subfolder)
        self.ensure_folder_exists(folder_path)
        version_number = self.get_next_version_number(folder_path, base_name)
        file_extension = os.path.splitext(base_name)[1] if '.' in base_name else '.ma'
        file_name = f"{base_name}_v{version_number:03d}{file_extension}"
        full_path = os.path.join(folder_path, file_name)

        self.save_scene(full_path)
        self.status_label.setText(f"Saved: {full_path}")

    def update_directory(self):
        if self.publish_radio.isChecked():
            self.current_directory = os.path.join(self.default_directory, "Publish")
        elif self.wip_radio.isChecked():
            self.current_directory = os.path.join(self.default_directory, "WIP")
        else:
            self.current_directory = os.path.join(self.default_directory, "WIP")

        self.assets_combo.clear()
        self.subfolder_combo.clear()
        self.populate_assets_combo()
        self.update_subfolders()

    def update_subfolders(self):
        asset = self.assets_combo.currentText()
        asset_directory = os.path.join(self.current_directory, asset)
        self.subfolder_combo.clear()
        if os.path.exists(asset_directory):
            subfolders = next(os.walk(asset_directory))[1]
            self.subfolder_combo.addItems(subfolders)
        else:
            self.status_label.setText(f"No subfolders found for {asset}.")

    def construct_folder_path(self, asset_type, subfolder):
        return os.path.join(self.current_directory, asset_type, subfolder)

    def ensure_folder_exists(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def get_next_version_number(self, folder_path, base_name):
        existing_files = os.listdir(folder_path)
        version_numbers = [int(re.search(r'_v(\d+)', file).group(1)) for file in existing_files if re.search(r'_v(\d+)', file)]
        return max(version_numbers) + 1 if version_numbers else 1

    def populate_assets_combo(self):
        if os.path.exists(self.current_directory):
            assets = next(os.walk(self.current_directory))[1]
            self.assets_combo.addItems(assets)
        else:
            self.status_label.setText("The default directory does not exist.")

    def create_folder(self):
        folder_name = self.new_folder_name_line_edit.text()
        if folder_name:
            new_folder_path = os.path.join(self.current_directory, folder_name)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                self.status_label.setText(f"Created folder: {new_folder_path}")
                self.update_directory()
            else:
                self.status_label.setText("Folder already exists.")
        else:
            self.status_label.setText("Please enter a folder name.")

    def save_scene(self, file_path):
        try:
            cmds.file(rename=file_path)
            cmds.file(save=True, type='mayaAscii')
            self.status_label.setText(f"Scene saved to {file_path}")
        except Exception as e:
            self.status_label.setText(f"Error: {e}")

# Initialize the dialog
try:
    save_tool_dialog.close() # pylint: disable=E0601
    save_tool_dialog.deleteLater()
except:
    pass

save_tool_dialog = SaveTool()
save_tool_dialog.show()
