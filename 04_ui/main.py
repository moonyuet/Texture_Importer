# init ***************************************************************************
# content = Texture Importer
#
# date    = 2022-08-07
# email   = moonyuet2008@hotmail.com
#*******************************************************************************

import sys
from PySide2 import QtWidgets
from pipeline.texture_importer import TextureImporter

#*******************************************************************
# START
def create():
    app = QtWidgets.QApplication(sys.argv)
    textureImporter = TextureImporter()
    sys.exit(app.exec_())

def start():
    global textureImporter
    textureImporter = TextureImporter()
