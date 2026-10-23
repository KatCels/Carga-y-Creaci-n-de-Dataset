
import json


class ManejadorJSON:
    def __init__(self, ruta_archivo, url_origen):
        self.ruta_archivo = ruta_archivo
        self.url_origen = url_origen
        self.datos = None
        self.modificacion = "Sin modificaciones"

    def importar(self):
        with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
            self.datos = json.load(archivo)

        return self.datos

    def modificar(self):
        if self.datos is None:
            raise ValueError("Primero debes importar los datos.")

        if not isinstance(self.datos, dict):
            raise ValueError("Se esperaba un objeto JSON.")

        valor_anterior = self.datos.get("actividad_ae2")
        self.datos["actividad_ae2"] = (
            "Se agregó este campo para demostrar la modificación del JSON."
        )

        self.modificacion = (
            f"Se agregó o actualizó la clave 'actividad_ae2'. "
            f"Valor anterior: {valor_anterior}"
        )

        return self.modificacion

    def guardar(self, ruta_salida):
        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            json.dump(
                self.datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )

        return ruta_salida
