import arcpy


def script_tool(fcIn6, nombre_campo):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn6 = arcpy.GetParameterAsText(0)   #capa
    nombre_campo = arcpy.GetParameterAsText(1)   #string
    script_tool(fcIn6, nombre_campo)
    arcpy.SetParameterAsText(1, "Result")

#---------------------------------------------------------------
#Ordenar CALCULAR CANTIDAD DE ESTABLECIMIENTOS DE SALUD Y EDUCACIÓN HAY POR MANZANA (JOIN_COUNT)

#Entorno
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn6)
content = []
content.append(aprxMap.listLayers()[0].name)

arcpy.AddMessage("Empieza el geoproceso")
arcpy.management.CalculateField(fcIn6, "DENS_POB", expression = "!TOTAL_PERS! / !Shape_Area!", field_type="DOUBLE")


