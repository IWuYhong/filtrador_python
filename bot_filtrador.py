import pandas as pd
import os
import re

'''
Ejemplo de control de extracción de Datos de un XLSX, 
el cual le entregaba un XLSX
alrededor de 200k Lineas para dividir el archivo en series de 10k.

Quise hacer un filtrado de una columna llamada pais, en este caso se encontraba en la decima columna.


Pequeño proyecto para db_call_center

ve hago mencion a 'Venezuela'
'''

# Ruta al archivo Excel que contiene los datos
ruta_excel = 'datos_aleatorios.xlsx' 

# Leer el archivo Excel, convirtiendo valores vacíos en cadenas vacías
df = pd.read_excel(ruta_excel, na_filter=False) 


# Configuración


# Filtrar el DataFrame para incluir solo las filas donde la columna de pais es "Venezuela"
nombre_columna = 'Venezuela'
# Número de filas por archivo, aca estableces la cantidad que desees organizar.
filas_por_archivo = 10
# Iniciando desde la Columna A que equivale al indice [0], en este caso es la J
x = 9

# Limpiar el nombre de la columna, eliminando espacios y caracteres especiales
# Usamos re.sub() para reemplazar caracteres no deseados de manera compatible con todas las versiones de Python
# Obtener el nombre de la columna de pais directamente desde la celda J1
columna_pais = df.columns[x]  # Asumiendo que "J" es la décima columna (índice 9)
columna_pais = columna_pais.strip().replace(' ', '_')
columna_pais = re.sub('[^a-zA-Z0-9_]', '', columna_pais)

# y crear un DataFrame aparte para las filas con valores vacíos en esa columna
df_filtrado = df[df[columna_pais].astype(str) == nombre_columna]
df_vacios = df[df[columna_pais].astype(str) == ''] 

# Ruta a la carpeta de escritorio
ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop") 

# Crear la carpeta 've' si no existe
ruta_carpeta_ve = os.path.join(ruta_escritorio, 've')
os.makedirs(ruta_carpeta_ve, exist_ok=True)

# Dividir el DataFrame filtrado en trozos y guardarlos en archivos Excel
for i in range(0, len(df_filtrado), filas_por_archivo):
    inicio = i
    fin = i + filas_por_archivo
    nombre_archivo = f've {inicio + 1} - {fin}.xlsx'
    ruta_archivo = os.path.join(ruta_carpeta_ve, nombre_archivo)
    df_filtrado.iloc[inicio:fin, 0:10].to_excel(ruta_archivo, index=False) 

# Guardar las filas con celdas vacías en un archivo aparte si existen
if not df_vacios.empty:
    ruta_archivo_vacios = os.path.join(ruta_carpeta_ve, 've Celdas Vacías.xlsx')
    df_vacios.iloc[:, 0:10].to_excel(ruta_archivo_vacios, index=False)

print("¡Proceso completado! Los archivos se han creado en la carpeta ve en tu escritorio.")
