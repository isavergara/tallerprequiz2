# Importar librerías a usar
import numpy as np
import pandas as pd
import scipy.io as sio

# 1. Crear una matriz aleatoria de numpy de 4 dimensiones con un tamaño de 1200000 
matriz = np.random.rand(10, 10, 10, 1200)

# Imprimir la matriz
print(matriz)

# 2. Crear una copia de la matriz creada en el ítem anterior (usando el método copy) de solo 3 dimensiones ("Cortando una de las dimensiones")
matriz_3d = matriz.copy()[:, :, :, 0]

# 3. De la matriz 3D, mostrar todos los atributos propios de dicha matriz, como el tipo de dato, tamaño, etc.
print("\nTipo de dato:", matriz_3d.dtype)
print("Tamaño de cada elemento en bytes:", matriz_3d.itemsize)
print("\nDimensiones:", matriz_3d.shape)
print("Tamaño total:", matriz_3d.size)

# 4. Modificar la forma de la matriz a 2D
array_2d = matriz.reshape((10 * 10, 10 * 1200))

print("\nDimensiones:", array_2d.ndim)
print("Forma:", array_2d.shape)
print("Tamaño total:", array_2d.size)

# 5. Convertir la matriz 2D a un DataFrame de Pandas
df = pd.DataFrame(array_2d)

# Imprimir atributos del DataFrame
print("\nDataFrame:")
print("Dimensiones:", df.ndim)
print("Forma:", df.shape)
print("Tamaño total:", df.size)
print("Tipos de datos por columna:", df.dtypes)
print("Índice:", df.index)
print("Columnas:", df.columns)

# 6. Crear una función que permita cargar un archivo .mat y .csv
def cargar_archivos(archivo_mat, archivo_csv):
    mat = sio.loadmat(archivo_mat)
    matriz_mat = mat.get('matriz', np.empty((0,0)))
    df_csv = pd.read_csv(archivo_csv)
    return matriz_mat, df_csv

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Calcular suma de la matriz")
    print("2. Calcular media de la matriz")
    print("3. Calcular desviación estándar de la matriz")
    print("4. Calcular valor máximo de la matriz")
    print("5. Calcular valor mínimo de la matriz")
    print("6. Cargar archivos .mat y .csv")
    print("7. Salir")
    opcion = int(input("Ingrese el número de opción: "))
    return opcion

def procesar_matriz(opcion, matriz):
    if opcion == 1:
        eje = int(input("Ingrese el número de eje: "))
        resultado = np.sum(matriz, axis=eje)
        print("Suma de la matriz:", resultado)
    elif opcion == 2:
        eje = int(input("Ingrese el número de eje: "))
        resultado = np.mean(matriz, axis=eje)
        print("Media de la matriz:", resultado)
    elif opcion == 3:
        eje = int(input("Ingrese el número de eje: "))
        resultado = np.std(matriz, axis=eje)
        print("Desviación estándar de la matriz:", resultado)
    elif opcion == 4:
        eje = int(input("Ingrese el número de eje: "))
        resultado = np.max(matriz, axis=eje)
        print("Valor máximo de la matriz:", resultado)
    elif opcion == 5:
        eje = int(input("Ingrese el número de eje: "))
        resultado = np.min(matriz, axis=eje)
        print("Valor mínimo de la matriz:", resultado)
    elif opcion == 6:
        ruta_mat = input("Ingrese la ruta del archivo .mat: ")
        ruta_csv = input("Ingrese la ruta del archivo .csv: ")
        matriz_mat, df_csv = cargar_archivos(ruta_mat, ruta_csv)
        print("Matriz cargada desde el archivo .mat:")
        print(matriz_mat)
        print("DataFrame cargado desde el archivo .csv:")
        print(df_csv)


while True:
    opcion = mostrar_menu()
    if opcion == 7:
        break
    elif opcion in [1, 2, 3, 4, 5]:
        eje = int(input("Ingrese el número de eje (0, 1, 2, o 3): "))
        procesar_matriz(opcion, matriz)
    elif opcion == 6:
        procesar_matriz(opcion, matriz)
    else:
        print("Opción no válida.")
