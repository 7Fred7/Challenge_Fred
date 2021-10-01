## LIBRARIES
# from glob import glob
import numpy as np                    # NUMPY SCIPY: Para obtener estadísticas
from scipy import stats    
import pandas as pd                   # PANDAS: para leer analizar datos
import cv2                            # Libreria recomendada para imagenes
import os      
#*****************************************************************************
# LEER RESOLUCIÓN DE IMAGENES
input_images_path = "C:/Users/operador/Documents/Challenge_PPS/Challenge_Fred/obj"
files_names = os.listdir(input_images_path)
# print (files_names)                 # OBSERVAR SI ESTA TOMANDO LAS IMAGENES
alto = []                             # Almacenar en listas
ancho = []
resolution = []
for file_name in files_names:
      # print(file_name)
      if file_name.split(".")[-1] not in ["jpg","png"]:
           continue                   #SOLO LEER IMAGENES
      image_path = input_images_path + "/" + file_name
      #print (image_path)              # OBSERVAR SI ESTA TOMANDO EL PATH
      image = cv2.imread(image_path)
      if image is None:
          continue                     #ERROR DE ENCONTRAR UN TXT
      image_path_h, image_path_w, _  = image.shape         
      #print (image.shape[1])         # OBSERVAR EL ANCHO
      ancho.append(image.shape[1])
      #print (image.shape[0])
      alto.append(image.shape[0])     # OBSERVAR EL ALTO
      resolution_1 = image.shape[1]*image.shape[0]
      #print (resolution_1)           # OBSERVAR LA RESOLUCIÓN
      resolution.append(resolution_1)
#*****************************************************************************
# DATAFRAME
df = pd.DataFrame(list(zip(alto, ancho, resolution)),
                  columns = ["Alto", "Ancho", "Resolución"])
#*****************************************************************************
# FUNCIONES
# Máximo
def maximo(valores):
    mayor = valores [0]
    
    for i in range (1, len(valores)):
        if valores[i] > mayor:
            mayor = valores [i]                    
    return mayor
# Mínimo
def minimo(valores):
    menor = valores [0]
    
    for i in range (1, len(valores)):
        if valores[i] < menor:
            menor = valores [i]                    
    return menor
# MEDIA
Media = np.mean(resolution)
# MEDIANA
Mediana = np.median(resolution)
# MODA
Moda = stats.mode(resolution)
#*****************************************************************************
# RESULTADOS
print (df)
print ('El valor máximo es: ' , maximo(resolution))
print ('El valor minimo es: ' , minimo(resolution))
print ('Media:', Media)
print ('Mediana: ', Mediana)
print ('Moda:', Moda)
