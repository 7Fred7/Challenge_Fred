## LIBRARIES
# NUMPY SCIPY: Para obtener estadísticas
import numpy as np
from scipy import stats    
# PANDAS: para leer analizar datos
import pandas as pd

# Importar datos (txt)
# Se detallan las columnas con el nombre correspondiente
datos = pd.read_csv('obj/9999998_00116_d_0000094.txt',sep=' ',header=None, names = ['Clase','Pos_X','Pos_Y','Ancho','Alto',])
#print (datos.info())
#print (datos.head())
print (datos)
# Extraer Columnas
Ancho = datos.iloc[:, 3]
#print (Ancho)
Alto = datos.iloc [: , 4]
#print (Alto)

# Obtener la Resolución
Resolution = Ancho * Alto
#print (Resolution)

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
Media = np.mean(Resolution)
# MEDIANA
Mediana = np.median(Resolution)
# MODA
Moda = stats.mode(Resolution)


print ('El valor máximo es: ' , maximo(Resolution))
print ('El valor minimo es: ' , minimo(Resolution))
print ('Media:', Media)
print ('Mediana: ', Mediana)
print ('Moda:', Moda)
