# Bot de Exportación Personalizado en Python
Este script automatiza la exportación de datos a Excel, filtrando por provincia o solo diviendo si es necesario.

Teniendo en cuenta una variable asignada para el Libro excel.
- ruta_excel = 'datos_aleatorios.xlsx'
- df = pd.read_excel(ruta_excel, na_filter=False)

## Flexibilidad: Modifica fácilmente la provincia en el código.
- filtrador(df, columna_pais, nombre_columna, filas_por_archivo)
- rangos(df, 10000)
## Ideal para:
- Analistas de datos
- Automatización de tareas repetitivas

## Tecnologías:
- Python
- Pandas
- Openpyxl

## Bot de Exportación Personalizado en Python: Automatiza y Organiza Tus Datos

Este script de Python está diseñado para simplificar y agilizar el proceso de exportación de datos a Excel. Al especificar la provincia de interés, el bot filtrará los datos y generará múltiples archivos Excel, cada uno conteniendo un máximo de 10,000 registros. Esta segmentación facilita la gestión y el análisis de grandes conjuntos de datos.

El Divisor de rangos, solo exporta en cantidades de 10.000 en 10.000 lo puedes cambiar si es necesario. y su exportacion lo hace en extensión .CSV

## Tecnologías utilizadas:

- Python: Lenguaje de programación versátil y ampliamente utilizado para el análisis de datos.
- Pandas: Biblioteca de Python para manipulación y análisis de datos.
- Openpyxl: Biblioteca de Python para leer y escribir archivos Excel.
