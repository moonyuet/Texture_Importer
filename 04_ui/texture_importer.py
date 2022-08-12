# UI ***************************************************************************
# content = Texture Importer
#
# date    = 2022-08-07
# email   = moonyuet2008@hotmail.com
#*******************************************************************************

import os
from select import select
import sys
import webbrowser

from Qt import QtWidgets, QtGui, QtCore, QtCompat
from PySide2.QtCore import QMetaObject
#*******************************************************************
# VARIABLE
TITLE = os.path.splitext(os.path.basename(__file__))[0]
selected_filter = "Image(*.png *.tiff *.targa *.exr)" 

#*******************************************************************
#CLASS
class TextureImporter():
    def __init__(self):
        #locate ui path

        texture_ui = ("./").join([os.path.dirname(__file__), "ui", TITLE + ".ui"])
        
        #load ui with abs path
        self.textureUtil = QtCompat.loadUi(texture_ui)
        
        #set up the UI connection
        self.textureUtil.btnFileLoad.clicked.connect(self.show_file_dialog)
        self.textureUtil.btnApply.clicked.connect(self.assign_material)

        self.textureUtil.btnHelp.clicked.connect(self.access_documentation)
        #Show the UI
        self.textureUtil.show()

#TODO set up all the things which can be set up by just using the Qt Library

#*******************************************************************
# DECORATOR
    def print_creation_proc(func):
        def wrapper_creation_proc(self):
            print("*******CREATING AND ASSIGNING MATERIAL**********")
            func(self) 
            print("******************FINISHED*********************")   
        return wrapper_creation_proc

#*******************************************************************
# FUNCTION
    def show_file_dialog(self):
        import_filepath, self.selected_filter = QtWidgets.QFileDialog.getOpenFileName(caption="Select Texture",
            directory="/home",
            filter= selected_filter) 
        if import_filepath:
            self.textureUtil.textureLineEdit.setText(import_filepath)
            self.textureUtil.textureLoad.setPixmap(import_filepath)

    def access_documentation(self):
        return webbrowser.open("https://github.com/moonyuet/Texture_Importer")

    @print_creation_proc
    def assign_material(self):
        self.texture_path_sets()
        print("Hello World")

    def texture_path_sets(self):
        """
        Image Format:
        0: PBR
        1. xTex

        """        
        texture_option = self.textureUtil.textureCombo.currentIndex()
        
        if texture_option == 0:
            print("PBR")
        elif texture_option == 1:
            print("xTex")
            
#*******************************************************************
# START
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    textureImporter = TextureImporter()
    app.exec_()