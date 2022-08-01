from ui import maya_pyside2_ui

    #EXECUTION
if __name__ == "__main__":
    try:
        file_management_dialog.close()
        file_management_dialog.deleteLater()
    except:
        pass

    file_management_dialog = maya_pyside2_ui.FileManagementDialog()
    file_management_dialog.show()