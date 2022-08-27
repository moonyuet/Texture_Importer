# maya_shelf ***************************************************************************
# content = Texture Importer
#
# date    = 2022-08-07
# email   = moonyuet2008@hotmail.com
#*******************************************************************************
from maya import cmds
import os

#*******************************************************************************
#SETUP ENVIRONMENT
PATH = os.environ.get("TEXTURE_IMPORTER")

ICON_PATH = PATH + "icon/"

MENU = "TEXTURE_IMPORTER"

#*******************************************************************************
#FUNCTION
def delete_plugin_shelf():
    if cmds.shelfLayout(MENU, exists=True):
        cmds.deleteUI(MENU)

def plugin_shelf():
    delete_plugin_shelf()
    cmds.shelfLayout(MENU, parent= "ShelfLayout")
    cmds.shelfButton(parent=MENU, annotation='Texture Importer', image1 = ICON_PATH + "texture_importer.png",
                     command='import main; main.start()')

plugin_shelf()