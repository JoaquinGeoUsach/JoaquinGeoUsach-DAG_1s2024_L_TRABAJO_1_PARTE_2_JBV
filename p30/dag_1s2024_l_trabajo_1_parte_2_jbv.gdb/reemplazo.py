import arcpy


def script_tool(fcIn8):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn8 = arcpy.GetParameterAsText(0)   #capa

 
    script_tool(fcIn8)
    arcpy.SetParameterAsText(0, "Result")

#---------------------------------------------------------------
#Ordenar CALCULAR CANTIDAD DE ESTABLECIMIENTOS DE SALUD Y EDUCACIÓN HAY POR MANZANA (JOIN_COUNT)

#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn8)
content = []
content.append(aprxMap.listLayers()[0].name)

arcpy.AddMessage("Empieza el geoproceso")
arcpy.management.CalculateField(fcIn8, field="DIST_VM", expression="0.01")