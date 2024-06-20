"""
Script documentation

- Tool parameters are accessed using arcpy.GetParameter() or 
                                     arcpy.GetParameterAsText()
- Update derived parameter values using arcpy.SetParameter() or
                                        arcpy.SetParameterAsText()
"""
import arcpy


def script_tool(fcIn8, outName, dirOut):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn8 = arcpy.GetParameterAsText(0)
    outName = arcpy.GetParameterAsText(1)       #nombre de salida  
    dirOut = arcpy.GetParameterAsText(2)       #Directorio de salida

    script_tool(fcIn8, outName, dirOut)
    arcpy.SetParameterAsText(2, "Result")
fcOut = f"{dirOut}\{outName}"
#Definir entorno
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn8)
content = []
content.append(aprxMap.listLayers()[0].name)

#-------------------------------------------------------
#Ordenar ELIMINACIÓN DE 0 DEL CAMPO DE DISTANCIAS A LAS VIAS QUE CONECTAN AL BORDE COSTERO
arcpy.management.SelectLayerByAttribute(content[0], selection_type="NEW_SELECTION", where_clause="DIST_VM = 0", invert_where_clause=None)
arcpy.conversion.ExportFeatures(fcIn8, fcOut)