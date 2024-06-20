import arcpy


def script_tool(fcIn, zone_field, fcIn2, zone_field1):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn = arcpy.GetParameterAsText(0)        #capa
    zone_field = arcpy.GetParameterAsText(1)  #campo
    fcIn2 = arcpy.GetParameterAsText(2)       #tabla
    zone_field1 = arcpy.GetParameterAsText(3) #campo

    script_tool(fcIn, zone_field, fcIn2, zone_field1)
    arcpy.SetParameterAsText(3, "Result")

#------------------------------------------------

#Ordenar OBTENCIÓN DE ALTURAS DEM PROMEDIO POR MANZANAS
#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")

aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn)
content = []
content.append(aprxMap.listLayers()[0].name)

arcpy.management.JoinField(fcIn, zone_field, fcIn2, zone_field1, "MEAN")