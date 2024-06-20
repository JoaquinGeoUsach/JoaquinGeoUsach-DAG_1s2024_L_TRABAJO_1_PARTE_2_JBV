### Toolbox ArcGIS Pro 3.1.0
El presente README tiene como objetivo la explicación del funcionamiento de la herrmienta (toolbox) generada por el autor en ArcGIS Pro 3.1.0, llamada:

•	“DAG_1s2024_L_TRABAJO_1_PARTE_2_JBV”

Esta herramienta es interactiva y sigue un orden lógico de cada proceso el cual generará un mapa que represente el riesgo de inundación por aumento del nivel del mar por manzana en la conurbación Coquimbo – La Serena.

La ejecución de los toolset (pasos) de la herramienta deben ser en el orden estipulado en su manual y en la misma toolbox. El orden y sus especificaciones son las siguientes:


- **Paso 1: Alturas promedio por manzana. (Script: JOIN DE ALTURAS A CAPAS MANZANAS)**

En este paso se realiza un join de los promedios de altura obtenidos de un DEM a la capa base con los poligonos manzanales. Para ejecutar el script de esta herramienta se requieren de los siguientes elementos especificados en la misma herramienta:

            Capa de entrada: IND_RIESGO_MANZ_CODE
			Campo de unión: MANZENT_I
			Tabla de unión: MANZANAS_DEM_CODE
			Campo de unión: MANZENT_I

El resultado se verá reflejado en la capa de entrada del paso 1 la cual será la entrada del siguiente geoproceso.

- **Paso 2**: ** Cantidad de establecimientos por manzana.**

En este paso se generan 2 spatial joins para contar cuantos establecimientos de educación y de salud existen en cada manzana. Este proceso de contar se realiza en 2 scripts por separado.

Ambos funcionan de la misma manera pero uno usa como join la capa de establecimientos de salud (EST_SALUD_CONURB) y la otra los de educación (EST_EDU_CONURB) ubicadas en el Feature Dataset llamado "INFRAESTRUCTURA_CRÍTICA”. El proceso está explicado en la herramienta.

Se utiliza como capa de entrada la misma capa que fue manipulada en el join anterior (IND_RIESGO_MANZ_CODE), encontrada en “DEMOGRAFÍA_DPA” el nombre de las capas resultantes tendrán un nombre determinado por el usuario y deben ser guardadas en el Feature Dataset llamado “CAPAS RESULTADOS”. 

            La ultima capa generada en el join de establecimientos de educación es la capa    base.
			Los nombres no pueden tener espacios.
			Refrescar el Feature Dataset “CAPAS RESULTADOS.

-**Paso 3**:  **Densidad poblacional por manzana.**

En este paso se calcula un nuevo campo en la tabla de entrada que es la ultima capa integrada al Dataset “CAPAS RESULTADOS”  con el nombre determinado por el usuario. Las entradas y parametros están especificados en la herramienta.

Es muy importante para la herramienta que en el nombre del campo se siga la insutrcción de llamar al campo “DENS_POB”.

-**Paso 4:  Calcular distancias mínimas con respecto a parametros.**

En esta herramienta se calculan 3 nears pero con respecto a distintos parametros (borde costero, vías que conectan al borde costero y red hidrológica).

La capa de entrada es la ultima generada en el paso 2.2 que ha sido manipulada en el paso 3 y que tiene el nombre que se le otorgó en el segundo join del paso 2. Los parametros requeridos están especificados en la herramienta.

Los Nears deben ejecutarse en el orden estipulado en la toolbox y siempre debe usarse como capa de entrada la ultima capa nombrada en los spatial joins del paso 2, que es la que es modificada desde el paso 2 en adelante, encontrada en las “CAPAS RESULTADOS”. 

Las capas de referencia para los Nears son BORDECOSTERO, VIASMAR_FINAL y RED_HIDRO_CONURB. Las primeras 2 se encuentran en la bandeja de la GDB mientras que RED_HIDRO_CONURB se encuentra en un Dataset llamado “CONTENCION_NATURAL".

-****Paso 5:  Calcular indice de riesgo.****

En el paso 5 se calcula finalmente el índice de riesgo el cual se obtiene a traves del cruce de todos los parametros obtenidos anteriormente y adjuntados a la tabla nombrada por el usuario en el paso 2.2 almacenada en “CAPAS RESULTADOS”.
La formula utilizada para calcular el índice es la siguiente: 

			((0.2 * 1 / !MEAN!) + (0.1 * !DENS_POB!) + (0.1 * 1 / (!DIST_VM! + 0.01)) + (0.05 * !Join_Count!) + (0.05 * !Join_Count_1!) + (0.1 * !DIST_RH!) + (0.4 * !DIST_BC!))/(1000 * 3.772302)

La nomenclatura es la siguiente: 
•	MEAN: Media de alturas por manzana.
•	DENS_POB: Densidad poblacional por manzana.
•	DIST_VM: Distancia mínima entre manzanas y vías que conectan al mar.
•	Join_Count: Cantidad de establecimientos de salud por manzana.
•	Join_Count_1: Cantidad de establecimientos de educación por manzana.
•	DIST_RH: Distancia mínima entre manzanas y red hidrológica.
•	DIST_BC: Distancia mínima entre las manzanas y el borde costero.

En este paso ya se encuentra listo el índice y la simbología a aplicar es: Graduated Colors, Natural Brakes, 5 Classes y está ubicada en una carpeta del package.
