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
#Ordenar CREACIÓN DEL CAMPO DEL ÍNDICE DE RIESGO DE INUNDACIÓN POR AUMENTO DE NIVEL DEL MAR POR MANZANA

arcpy.management.CalculateField(fcIn6, nombre_campo, "((0.2 * 1 / !MEAN!) + (0.1 * !DENS_POB!) + (0.1 * 1 / (!DIST_VM! + 0.01)) + (0.05 * !Join_Count!) + (0.05 * !Join_Count_1!) + (0.1 * !DIST_RH!) + (0.4 * 1/(!DIST_BC!+0.1)))/(1000 * 0.147036)", field_type="DOUBLE")