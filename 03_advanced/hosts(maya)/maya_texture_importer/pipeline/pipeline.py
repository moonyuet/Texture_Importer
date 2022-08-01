from PySide2 import QtWidgets

import maya.cmds as cmds
from ui import maya_pyside2_ui

class MayaTextureImporter(QtWidgets.QDialog):

    #VARIABLE
    FILE_FILTERS = "PNG(*.png);;TIFF(*.tiff);;TARGA(*targa);;EXR(*exr);; All Files(*.*)" 
    selected_filter = "Image(*.png *.tiff *.targa *.exr)" 

    pbr_path = []
    VERSION = 1
    #DECORATOR
    def print_creation_proc(func):
        def wrapper_creation_proc(self):
            print("*******CREATING AND ASSIGNING MATERIAL**********")
            func(self) 
            print("******************FINISHED*********************")   
        return wrapper_creation_proc


    #FUNCTION
    def show_file_dialog(self):
        import_filepath, self.selected_filter = QtWidgets.QFileDialog.getOpenFileName(self, "Select Texture", "", 
        self.FILE_FILTERS, self.selected_filter)
        if import_filepath:
            self.fileManagementDialog = maya_pyside2_ui.FileManagementDialog()
            self.fileManagementDialog.filepath_import.setText(import_filepath)

    @print_creation_proc
    def assign_material(self):
        
        target_obj = self.target_object()

        if target_obj:
        
            #create Arnold Shader
            new_aiShader = cmds.createNode('aiStandardSurface')
            shader_grp = cmds.sets(name=new_aiShader + "_MASTER",
                                        empty=True,
                                        renderable=True,
                                        noSurfaceShader=True)
                
            #version   
            version =  self.VERSION
            version += 1
            new_version = 'v{:03}'.format(version)

            #Building the connections between textures and the new material
            cmds.connectAttr(new_aiShader + ".outColor", shader_grp + ".surfaceShader")

            diffuse_map = cmds.shadingNode( 'file',n = "BaseColor_Map" + "." + new_version, at =True )
            cmds.connectAttr(diffuse_map + ".outColor", new_aiShader + ".baseColor")

            roughness_map = cmds.shadingNode( 'file',n = "Roughness_Map"+ "." + new_version, at =True )
            cmds.connectAttr(roughness_map + ".outAlpha", new_aiShader + ".specularRoughness")
            metallic_map = cmds.shadingNode( 'file',n = "Metallic_Map" + "." + new_version, at =True )
            cmds.connectAttr(metallic_map + ".outAlpha", new_aiShader + ".metalness")

            normal_map = cmds.shadingNode( 'file',n = "Normal_Map" + "." + new_version, at =True )
            #convert normal_map to bump_map
            bump_2d_node = cmds.shadingNode('bump2d', n= "normal_bump_parameter" + "." + new_version, au =True)
            cmds.setAttr(bump_2d_node + ".bumpInterp", 1)
            cmds.connectAttr(normal_map + ".outAlpha", bump_2d_node + ".bumpValue")
            cmds.connectAttr(bump_2d_node + ".outNormal", new_aiShader + ".normalCamera")

            cmds.shadingNode('place2dTexture', n= "Mapping Transform" + "." + new_version, au = True)

            file_list = cmds.ls(type= ["file"])
            Coord_list = cmds.ls(type= ["place2dTexture"])
            count = len(Coord_list) 

            for f in file_list:
                for j in range (0, count):     
                    cmds.connectAttr(Coord_list[j] + ".outUV", f + ".uvCoord", f = True)
                    cmds.connectAttr(Coord_list[j] + ".offset", f + ".offset", f= True)
                    cmds.connectAttr(Coord_list[j] + ".repeatUV", f + ".repeatUV", f = True)
                    cmds.connectAttr(Coord_list[j] + ".rotateUV", f + ".rotateUV", f = True)
                    if not cmds.isConnected(Coord_list[j] + ".outUV", f + ".uvCoord"):
                        cmds.delete(Coord_list[j])

            #get the textures
            pbr_path = self.texture_path_sets()

            cmds.setAttr(str(diffuse_map) + ".fileTextureName", pbr_path[0], type = "string")
            cmds.setAttr(str(roughness_map) + ".fileTextureName", pbr_path[1], type = "string")
            cmds.setAttr(str(normal_map) + ".fileTextureName", pbr_path[2], type = "string")
            cmds.setAttr(str(metallic_map) + ".fileTextureName", pbr_path[3], type = "string")

            return cmds.sets(target_obj, forceElement = str(shader_grp))

    
    def target_object(self):
        current_obj = cmds.ls(selection = True)

        if not current_obj or len(current_obj) > 1:
            cmds.warning("You must select ONE mesh to assign material")
            return

        return current_obj

    
    def texture_path_sets(self):
        
        texture_path = self.pbr_path
        
        #pbr_list = ["ROUGH","NRM", "MTL"]
        pbr_list = self.texture_json_import()

        self.fileManagementDialog = maya_pyside2_ui.FileManagementDialog()
        diffuse_path = self.fileManagementDialog.filepath_import.text()
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
            
            json_path = "./data/textures.json"
            pbr_list = []

            self.fileManagementDialog = maya_pyside2_ui.FileManagementDialog()
            diffuse_path = self.fileManagementDialog.filepath_import.text()
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
        
