
import sys

from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui
import maya.cmds as cmds
from ui import maya_pyside2_ui


def maya_main_window():

    main_window_ptr = omui.MQtUtil.mainWindow()
    if sys.version_info.major >= 3:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    else:
        return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class FileManagementDialog(QtWidgets.QDialog):
    #VARIABLE
    dig_instance = None

    @classmethod
    def show_dialog(cls):
        if not cls.dig_instance:
            cls.dig_instance = FileManagementDialog()
        
        if cls.dig_instance.isHidden():
            cls.dig_instance.show()
        else:
            cls.dig_insatnce.raise_()
            cls.dig_instance.activateWindow()
    
    def __init__(self, parent=maya_main_window()):
        super(FileManagementDialog, self).__init__(parent)

        self.setWindowTitle("Texture Importer")
        self.setMinimumSize(300, 80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

#CREATE WIDGETS
    def create_widgets(self):
        self.imported_caption = QtWidgets.QLabel("Import Your Texture")

        self.filepath_import = QtWidgets.QLineEdit()
        self.imported_filepath_btn = QtWidgets.QPushButton()
        self.imported_filepath_btn.setIcon(QtGui.QIcon(":fileOpen.png"))
        self.imported_filepath_btn.setToolTip("Select Texture")

        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        imported_caption_layout = QtWidgets.QHBoxLayout()
        imported_caption_layout.addWidget(self.imported_caption)

        file_import_layout = QtWidgets.QHBoxLayout()
        file_import_layout.addWidget(self.filepath_import)
        file_import_layout.addWidget(self.imported_filepath_btn)
        
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(imported_caption_layout)
        form_layout.addRow("Select Texture:",file_import_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        from pipeline import pipeline
        self.texture_importer = pipeline.MayaTextureImporter()
        self.imported_filepath_btn.clicked.connect(self.texture_importer.show_file_dialog)
        self.apply_btn.clicked.connect(self.texture_importer.assign_material)
        self.close_btn.clicked.connect(self.close)
