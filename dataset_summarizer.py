
import pandas as pd


class DatasetSummarizer:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def generate_summary(self, output_file="resumen_dataset.txt"):
        with open(output_file, "w", encoding="utf-8") as file:

            file.write("RESUMEN DEL DATASET\n")
            file.write("===================\n\n")

            file.write(f"Filas: {self.dataframe.shape[0]}\n")
            file.write(f"Columnas: {self.dataframe.shape[1]}\n\n")

            file.write("TIPOS DE DATOS\n")
            file.write(str(self.dataframe.dtypes))
            file.write("\n\n")

            file.write("VALORES NULOS\n")
            file.write(str(self.dataframe.isnull().sum()))
            file.write("\n\n")

            file.write("ESTADISTICAS DESCRIPTIVAS\n")
            file.write(
                self.dataframe.describe(include="all").to_string()
            )

        print(f"Resumen guardado en: {output_file}")

