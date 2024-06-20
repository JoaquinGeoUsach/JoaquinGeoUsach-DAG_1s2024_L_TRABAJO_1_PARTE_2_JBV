import arcpy


def script_tool(fcIn7, near_features):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn7 = arcpy.GetParameterAsText(0) #capa
    near_features = arcpy.GetParameterAsText(1) #capa

    script_tool(fcIn7, near_features)
    arcpy.SetParameterAsText(1, "Result")

#-----------------------------------------------------
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn7)
content = []
content.append(aprxMap.listLayers()[0].name)

arcpy.analysis.Near(fcIn7, near_features="VIASMAR_FINAL", field_names="NEAR_FID DIST_VM_FID;NEAR_DIST DIST_VM", distance_unit="Meters")