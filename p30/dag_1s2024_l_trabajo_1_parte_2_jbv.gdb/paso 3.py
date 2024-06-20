﻿import arcpy


def script_tool(fcIn4, join_features, outName, dirOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn4 = arcpy.GetParameterAsText(0)   #capa
    join_features = arcpy.GetParameterAsText(1)   #capa
    outName = arcpy.GetParameterAsText(2)       #nombre de salida  
    dirOut = arcpy.GetParameterAsText(3)       #Directorio de salida
    script_tool(fcIn4, join_features, outName, dirOut)
    arcpy.SetParameterAsText(3, "Result")

#---------------------------------------------------------------
#Ordenar CALCULAR CANTIDAD DE ESTABLECIMIENTOS DE SALUD Y EDUCACIÓN HAY POR MANZANA (JOIN_COUNT)
#Entorno
#Definir entorno
fcOut = f"{dirOut}\{outName}"
aprx = arcpy.mp.ArcGISProject("CURRENT")

aprxMap = aprx.listMaps()[0]


content = []
content.append(aprxMap.listLayers()[0].name)

arcpy.AddMessage("Empieza el geoproceso")
arcpy.analysis.SpatialJoin(fcIn4, join_features, fcOut)
aprxMap.addDataFromPath(fcOut)