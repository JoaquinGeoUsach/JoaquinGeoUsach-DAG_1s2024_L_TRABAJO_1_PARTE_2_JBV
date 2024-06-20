"""
Script documentation

- Tool parameters are accessed using arcpy.GetParameter() or 
                                     arcpy.GetParameterAsText()
- Update derived parameter values using arcpy.SetParameter() or
                                        arcpy.SetParameterAsText()
"""
import arcpy


def script_tool(fcIn8, target_feature_class):
    """Script code goes below"""

    return


if __name__ == "__main__":

    fcIn8 = arcpy.GetParameterAsText(0)
    target_feature_class = arcpy.GetParameterAsText(1)


    script_tool(fcIn8, target_feature_class)
    arcpy.SetParameterAsText(1, "Result")

#------------------------------------
aprx = arcpy.mp.ArcGISProject("CURRENT")
aprxMap = aprx.listMaps()[0]
aprxMap.addDataFromPath(fcIn8)
content = []
content.append(aprxMap.listLayers()[0].name)
# Ejecutar Append para agregar los datos de la capa al Feature Class
arcpy.management.Append(inputs=fcIn8, target=target_feature_class, schema_type="NO_TEST")

arcpy.AddMessage(f"Los datos de {fcIn8} se han agregado a {target_feature_class} correctamente.")