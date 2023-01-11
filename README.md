# README

Este proyecto se encarga de leer los datos de población mundial de 11 países desde 1970 hasta 2022, disponibles en una base de datos en Kaggle. Utilizando el módulo CSV, se leen los archivos y se genera un diccionario para cada país.

## Requerimientos

- Python 3.x
- Módulo CSV
- Acceso a la base de datos en Kaggle

## Uso

Para utilizar este proyecto, es necesario tener acceso a la base de datos en Kaggle y descargar los archivos necesarios. Luego, utilizando el módulo CSV y la función `reader()`, se pueden separar las líneas de cada archivo y generar un diccionario para cada país.

```python
import csv

with open('population_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        print(row)

## Autor

Lautaro Acosta
