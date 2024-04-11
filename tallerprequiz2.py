#importar librerías a usar
import numpy as np
import pandas as pd
import scipy.io as sio

# 1 Crear una matriz de Numpyaleatoria de 4dimensiones y un sizede 1200000 

#  matriz de 4 dimensiones
matriz = np.random.rand(10, 10, 10, 1200)

# Print de la matriz
print(matriz)

#2Crea una copia de la matriz creada en el ítem anterior(usar método copy)de solo 3 dimensiones (“Cortando una de las dimensiones”)
# Crear una copia de la matriz anterior con solo 3 dimensiones
matriz_3d = matriz.copy()[:, :, :, 0]


#3. De lamatriz 3D, muestra todos los atributos propios de dicha matriz , dimensión, tamaño, etc..

#tipo de dato y tamaño
print("\ndtype:", matriz_3d.dtype)
print("itemsize:", matriz_3d.itemsize)

#imprimir dimensión y tamaño total
print("\nShape:", matriz_3d.shape)
print("Tamaño:", matriz_3d.size)

#4 Modificar su forma y pasarla a 2D
# Modificar forma con reshape
array_2d = matriz.reshape((10 * 10, 10 * 120))


print("\nDimensions:", array_2d.ndim)
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)

#5 Convertir la matriz 2D a un DataFrame de Pandas
df = pd.DataFrame(array_2d)

# Imprimir atributos del DataFrame
print("\nDataFrame:")
print("Dimensions:", df.ndim)
print("Shape:", df.shape)
print("Size:", df.size)
print("Dtypes:", df.dtypes)
print("Index:", df.index)
print("Columns:", df.columns)

# 6. Crear una función que permita cargar un archivo .mat y .csv

def cargar_archivos(ruta_mat, ruta_csv):
    # Cargar archivo .mat
    mat = sio.loadmat(ruta_mat)
    matriz_mat = mat.get('matriz', np.empty((0,0)))

    # Cargar archivo .csv
    df_csv = pd.read_csv(ruta_csv)

    # Devolver ambos datos
    return matriz_mat, df_csv
#Funciones
def sum_array(arr, axis=None):
    return np.sum(arr, axis=axis)
def subtract_array(arr, val, axis=None):
    return np.subtract(arr, val, axis=axis)
def multiply_array(arr1, arr2, axis=None):
    return np.multiply(arr1, arr2, axis=axis)
def divide_array(arr1, arr2, axis=None):
    return np.divide(arr1, arr2, axis=axis)
def log_array(arr, axis=None):
    return np.log(arr, out=np.zeros_like(arr), axis=axis)
def average_array(arr, axis=None):
    return np.mean(arr, axis=axis)
def std_array(arr, axis=None):
    return np.std(arr, axis=axis)
