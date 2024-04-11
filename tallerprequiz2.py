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

# Imprimir la matriz 3D, dimensiones y tamaño
print("\nMatriz de 3 dimensiones:")
print(matriz_3d)
print("\nDimensiones:", matriz_3d.ndim)
print("Tamaño:", matriz_3d.size)
