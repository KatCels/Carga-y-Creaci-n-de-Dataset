import csv


class ManejadorCSV:
    def __init__(self, ruta_archivo, url_origen):
        self.ruta_archivo = ruta_archivo
        self.url_origen = url_origen
        self.encabezados = []
        self.registros = []
        self.modificacion = "Sin modificaciones"

    def importar(self):
        with open(self.ruta_archivo, "r", newline="", encoding="utf-8-sig") as archivo:
            lector = csv.reader(archivo)
            filas = list(lector)

        if not filas:
            raise ValueError("El archivo CSV está vacío.")

        self.encabezados = filas[0]
        self.registros = filas[1:]

        return self.registros

    
    
    def modificar(self):
        if not self.encabezados:
            raise ValueError("Primero debes importar los datos.")

        nuevo_registro = [
            "registro_006",
            "com.ejemplo.app",
            "Buena aplicación, funciona bien.",
            "October 23 2026",
            "5",
            "1487"
        ]

        self.registros.append(nuevo_registro)

        self.modificacion = "Se agregó el registro registro_006."

        print("Método modificar() ejecutado correctamente.")
        print("Nuevo registro:", nuevo_registro)

        return nuevo_registro



    def guardar(self, ruta_salida):
        with open(ruta_salida, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.registros)

        return ruta_salida
