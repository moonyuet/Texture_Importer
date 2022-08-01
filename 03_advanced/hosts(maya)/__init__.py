import sys
import maya.cmds as cmds

path = "E:/hosts(maya)/maya_texture_importer"
sys.path.append(path)

MENU = "Texture_Importer"

def delete_plugin_shelf():
    if cmds.shelfLayout(MENU, exists=True):
        cmds.deleteUI(MENU)

def plugin_shelf():
    delete_plugin_shelf()
    cmds.shelfLayout(parent = MENU, parent="ShelfLayout")
    cmds.shelfButton(parent = MENU, annotation = "Texture Importer",
    command='from maya_texture_importer import main;reload(main);main.main()')

plugin_shelf()