"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():
    with open('clusters_report.txt', 'r') as file:
        data = file.readlines()

    processed_data = []
    for line in data:
        line = line.strip()
        line = line.lower().replace(' ', '_')
        line = ', '.join(line.split(','))
        processed_data.append(line)

    df = pd.DataFrame(processed_data, columns=['nombres_de_columnas'])

    return df
