import arcpy


def script_tool(fcIn3, fcIn4, dirOut, outName):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn3 = arcpy.GetParameterAsText(0)
    fcIn4 = arcpy.GetParameterAsText(1)
    dirOut = arcpy.GetParameterAsText(2)
    outName = arcpy.GetParameterAsText(3)

    script_tool(fcIn3, fcIn4 ,dirOut, outName)
    arcpy.SetParameterAsText(3, "Result")

#Ordenar UNIÓN DE ESTABLECIMIENTOS DE SALUD Y EDUCACIÓN EN UNA SOLA CAPA

fcOut = f"{dirOut}\{outName}"

#Entorno
#Definir entorno
arcpy.AddMessage("Empieza la definición de enterno")
aprx = arcpy.mp.ArcGISProject("CURRENT")

#Contenidos activos en el proyecto
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn3)
aprxMap.addDataFromPath(fcIn4)
content = []
n = len(aprxMap.listLayers())
for i in list(range(0,n)):
    content.append(aprxMap.listLayers()[i].name)

arcpy.AddMessage("Se empieza a ejecutar el merge")
arcpy.management.Merge(fcIn3, fcIn4, fcOut)