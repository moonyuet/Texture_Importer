import sys

import bpy
from PySide2 import QtCore, QtWidgets
#from shiboken2 import wrapInstance

class FileManagementDialog(QtWidgets.QDialog):

    #VARIABLE   
    FILE_FILTERS = "PNG(*.png);; TIFF(*.tiff);;TARGA(*targa);;EXR(*exr);; All Files(*.*)"
    selected_filter = "Image(*.png *.tiff *.targa *.exr)"
    dig_instance = None
    pbr_path = []
    VERSION = 1

    @classmethod
    def show_dialog(cls):
        if not cls.dig_instance:
            cls.dig_instance = FileManagementDialog()

        if cls.dig_isntance.isHidden():
            cls.dig_instance.show()

        else:
            cls.dig_instance.raise_()
            cls.dig_instance.activateWindow()

    def __init__(self, parent= None):
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

        #TODO: Resolve the size of push button
        self.imported_filepath_btn = QtWidgets.QPushButton("...")
        #self.imported_filepath_btn.setIcon(QtGui.QIcon(":fileOpen.png"))
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
        form_layout.addRow("Select Texture:", file_import_layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.apply_btn)
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.imported_filepath_btn.clicked.connect(self.show_file_dialog)

        self.apply_btn.clicked.connect(self.assign_material)
        self.close_btn.clicked.connect(self.close)


#DECORATOR
    def print_creation_proc(func):
        def wrapper_creation_proc(self):
            print("*******CREATING AND ASSIGNING MATERIAL**********")
            func(self) 
            print("*******FINISHED**********")   
        return wrapper_creation_proc

#FUNCTIONS
    def show_file_dialog(self):
        import_filepath, self.selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Select Texture", "",
        self.FILE_FILTERS, self.selected_filter)

        if import_filepath:
            self.filepath_import.setText(import_filepath)

    @print_creation_proc
    def assign_material(self):
        activeObject = bpy.data.objects
        if activeObject == "":
            self.report({'ERROR'}, 'You must select at least ONE Mesh')
            return

        mat_pbr = bpy.data.materials.new(name = "PBR Shader")
        mat_pbr.use_nodes = True

        for obj in activeObject:
            if obj.type == "MESH":
                obj.data.materials.append(mat_pbr)
        
                bsdf = mat_pbr.node_tree.nodes.get("Principled BSDF")
        
        #diffuse map
        dif_tex = mat_pbr.node_tree.nodes.new("ShaderNodeTexImage")
        mat_pbr.node_tree.links.new(dif_tex.outputs[0], bsdf.inputs[0])
        
        #roughness map
        rough_tex = mat_pbr.node_tree.nodes.new("ShaderNodeTexImage")
        mat_pbr.node_tree.links.new(rough_tex.outputs[0], bsdf.inputs[7])

        #normal map
        nrm_node = mat_pbr.node_tree.nodes.new("ShaderNodeNormalMap")
        nrm_tex = mat_pbr.node_tree.nodes.new("ShaderNodeTexImage")
        mat_pbr.node_tree.links.new(nrm_tex.outputs[0],nrm_node.inputs[1])
        mat_pbr.node_tree.links.new (nrm_node.outputs[0], bsdf.inputs[19])
        
        #metallic map
        mtl_tex = mat_pbr.node_tree.nodes.new("ShaderNodeTexImage")
        mat_pbr.node_tree.links.new(mtl_tex.outputs[0], bsdf.inputs[4])

        #mapping and texture coordinate 
        map_node = mat_pbr.node_tree.nodes.new("ShaderNodeMapping")
        map_node.vector_type = 'TEXTURE'
        text_coord = mat_pbr.node_tree.nodes.new("ShaderNodeTexCoord")
        mat_pbr.node_tree.links.new(text_coord.outputs[2], map_node.inputs[0])
        
        #linking all maps
        mat_pbr.node_tree.links.new(map_node.outputs[0], dif_tex.inputs[0])
        mat_pbr.node_tree.links.new(map_node.outputs[0], nrm_tex.inputs[0])
        mat_pbr.node_tree.links.new(map_node.outputs[0], rough_tex.inputs[0])
        mat_pbr.node_tree.links.new(map_node.outputs[0], mtl_tex.inputs[0])

        texture_nodes = []
        texture_nodes.append(dif_tex)
        texture_nodes.append(rough_tex)
        texture_nodes.append(nrm_tex)
        texture_nodes.append(mtl_tex)
        texture_count = len(texture_nodes)
        texture_path = self.texture_path_sets()

        for t in range(0, texture_count):
            texture_nodes[t].image = bpy.data.images.load(texture_path[t])

        return activeObject


    def texture_path_sets(self):
        
        texture_path = self.pbr_path
        
        #pbr_list = ["ROUGH","NRM", "MTL"]
        pbr_list = self.texture_json_import()

        diffuse_path = self.filepath_import.text()
        texture_path.append(diffuse_path)
        
        file_split = diffuse_path.split("_")
        extension_split = file_split[1].split(".")

        for p in pbr_list:
            name_split = file_split[1].replace(extension_split[0], p)
            map_path = diffuse_path.replace(file_split[1], name_split)
            texture_path.append(map_path)

        return texture_path


    def texture_json_import(self):
        import json
        
        json_path = r"C:\Users\Kayla\Texture_Importer\03_advanced\textures.json"
        pbr_list = []

        diffuse_path = self.filepath_import.text()
        file_split = diffuse_path.split("_")
        extension_split = file_split[1].split(".")


        with open(json_path) as json_file:
            tx_data = json.load(json_file)
            if extension_split[0] == tx_data["xtex"]["basecolor"]:
                roughness = tx_data["xtex"]["roughness"]
                normal = tx_data["xtex"]["normal"]
                metallic = tx_data["xtex"]["metallic"]
            elif extension_split[0] == tx_data["pbr"]["basecolor"]:
                roughness = tx_data["pbr"]["roughness"]
                normal = tx_data["pbr"]["normal"]
                metallic = tx_data["pbr"]["metallic"]
            else:
                cmds.warning("Please select an image with the correct naming convention!")

        pbr_list.append(roughness)
        pbr_list.append(normal)
        pbr_list.append(metallic)

        return pbr_list

#EXECUTIONS
if __name__ == "__main__":
    try:
        file_management_dialog.close()
        file_management_dialog.deleteLater()
        
    except:
        pass

    app = QtWidgets.QApplication(sys.argv)
    file_management_dialog = FileManagementDialog()
    file_management_dialog.show()
