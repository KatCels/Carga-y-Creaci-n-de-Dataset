
class GeneradorResumenTXT:
    def __init__(self, resultado_csv, resultado_json):
        self.resultado_csv = resultado_csv
        self.resultado_json = resultado_json

    def generar(self, ruta_salida="resumen.txt"):
        csv_info = self.resultado_csv
        json_info = self.resultado_json

        contenido = f"""
RESUMEN DE LA ACTIVIDAD AE2
===========================

1. FUENTES DE LOS DATOS

CSV:
URL de origen: {csv_info['url_origen']}
Archivo importado: {csv_info['archivo_original']}
Archivo guardado: {csv_info['archivo_salida']}

JSON:
URL de origen: {json_info['url_origen']}
Archivo importado: {json_info['archivo_original']}
Archivo guardado: {json_info['archivo_salida']}

2. MODIFICACIONES REALIZADAS

CSV:
{csv_info['modificacion']}

JSON:
{json_info['modificacion']}

3. CLASES Y MÉTODOS UTILIZADOS

ManejadorCSV:
importar(), modificar(), guardar()

ManejadorJSON:
importar(), modificar(), guardar()

GeneradorResumenTXT:
generar()

4. CANTIDAD DE DATOS PROCESADOS

Registros CSV: {csv_info['cantidad_registros']}
Secciones principales del objeto JSON: {json_info['cantidad_secciones']}

5. RESULTADO

Se conservaron los archivos originales y se generaron
archivos nuevos con las modificaciones realizadas.
"""

        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            archivo.write(contenido.strip() + "\n")

        return ruta_salida
