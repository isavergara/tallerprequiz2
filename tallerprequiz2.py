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

def load_files(mat_file, csv_file):
    mat = sio.loadmat(mat_file)
    matriz_mat = mat.get('matriz', np.empty((0,0)))

    df_csv = pd.read_csv(csv_file)

    return matriz_mat, df_csv

def display_menu():
    print("\nSelect an option:")
    print("1. Calculate sum of array")
    print("2. Calculate mean of array")
    print("3. Calculate standard deviation of array")
    print("4. Calculate maximum value of array")
    print("5. Calculate minimum value of array")
    print("6. Load .mat and .csv files")
    print("7. Exit")

    option = int(input("Enter option number: "))
    return option

def process_array(option, array):
    if option == 1:
        axis = int(input("Enter axis number: "))
        result = sum_array(array, axis=axis)
        print("Sum of array:", result)
    elif option == 2:
        axis = int(input("Enter axis number: "))
        result = mean_array(array, axis=axis)
        print("Mean of array:", result)
    elif option == 3:
        axis = int(input("Enter axis number: "))
        result = std_array(array, axis=axis)
        print("Standard deviation of array:", result)
    elif option == 4:
        axis = int(input("Enter axis number: "))
        result = max_array(array, axis=axis)
        print("Maximum value of array:", result)
    elif option == 5:
        axis = int(input("Enter axis number: "))
        result = min_array(array, axis)
        print("Minimum value of array:", result)
    elif option == 6:
        ruta_mat = input("Enter .mat file path: ")
        ruta_csv = input("Enter .csv file path: ")
        matriz_mat, df_csv = load_files(ruta_mat, ruta_csv)
        print("Matriz cargada desde .mat file:")
        print(matriz_mat)
        print("DataFrame cargado desde .csv file:")
        print(df_csv)