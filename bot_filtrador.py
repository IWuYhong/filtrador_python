import pandas as pd
import os
import re

def filtrador(df, columna_pais, nombre_columna, filas_por_archivo):
    """
    Filtra un DataFrame por una columna específica y lo divide en archivos más pequeños.

    Args:
        df: DataFrame a filtrar.
        columna_pais: Nombre de la columna a filtrar.
        nombre_columna: Valor a buscar en la columna.
        filas_por_archivo: Número de filas por archivo a crear.
    """

    # Limpiar el nombre de la columna
    columna_pais = columna_pais.strip().replace(' ', '_')
    columna_pais = re.sub('[^a-zA-Z0-9_]', '', columna_pais)

    # Filtrar y dividir el DataFrame
    df_filtrado = df[df[columna_pais].astype(str) == nombre_columna]
    df_vacios = df[df[columna_pais].astype(str) == '']

    # Ruta a la carpeta de destino
    ruta_carpeta = os.path.join(os.path.expanduser("~"), "Desktop", nombre_columna)
    os.makedirs(ruta_carpeta, exist_ok=True)

    # Dividir el DataFrame filtrado en trozos y guardarlos en archivos Excel
    for i in range(0, len(df_filtrado), filas_por_archivo):
        inicio = i
        fin = i + filas_por_archivo
        nombre_archivo = f'{nombre_columna} {inicio + 1} - {fin}.xlsx'
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
        df_filtrado.iloc[inicio:fin].to_excel(ruta_archivo, index=False)

    # Guardar las filas con celdas vacías en un archivo aparte si existen
    if not df_vacios.empty:
        ruta_archivo_vacios = os.path.join(ruta_carpeta, f'{nombre_columna} Celdas Vacías.xlsx')
        df_vacios.to_excel(ruta_archivo_vacios, index=False)

def rangos(df, filas_por_archivo):
    """
    Divide un DataFrame en archivos CSV más pequeños sin aplicar ningún filtro, 
    utilizando ';' como delimitador.

    Args:
        df: DataFrame a dividir.
        filas_por_archivo: Número de filas por archivo a crear.
    """

    # Ruta a la carpeta de destino
    ruta_carpeta = os.path.join(os.path.expanduser("~"), "Desktop", "Todos")
    os.makedirs(ruta_carpeta, exist_ok=True)

    # Dividir el DataFrame en trozos y guardarlos en archivos CSV
    for i in range(0, len(df), filas_por_archivo):
        inicio = i
        fin = i + filas_por_archivo
        nombre_archivo = f'Todos_{inicio + 1}_{fin}.csv'
        ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
        df.iloc[inicio:fin].to_csv(ruta_archivo, index=False, sep=';')

# Ejemplo de uso
ruta_excel = 'datos_aleatorios.xlsx'
df = pd.read_excel(ruta_excel, na_filter=False)

# Filtrar por país
# filtrador(df, 'pais', 'Venezuela', 10000)

# Dividir todos los datos sin filtrar
# rangos(df, 10000)
