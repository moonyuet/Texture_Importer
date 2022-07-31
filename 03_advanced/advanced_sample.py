import json
json_path = r"C:\Users\Kayla\Texture_Importer\03_advanced\textures.json"
pbr_list = []

with open(json_path) as json_file:
    tx_data = json.load(json_file)

    roughness = tx_data["xtex"]["roughness"]
    normal = tx_data["xtex"]["normal"]
    metallic = tx_data["pbr"]["metallic"]
    pbr_list.append(roughness)
    pbr_list.append(normal)

print(pbr_list)