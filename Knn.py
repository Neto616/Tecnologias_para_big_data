#Importamos math para la raiz cuadrada y matplotlib y pandas para poder graficar los datos
import math
import matplotlib.pyplot as plt
import pandas as np

"""
Función para sacar la distancia Euclidiana de dos coordenadas
recibe dos listas para sacar esta distancia
"""
def distanciaEuclidiana(distancia1: list, distancia2: list):
    return math.sqrt((distancia1[0]-distancia2[0])**2 + (distancia1[1]-distancia2[1])**2)

def generarGrafica(grupos: set, x, y, prediccion):
    cmap = plt.colormaps.get_cmap('viridis')  # Corregido: número de grupos como segundo argumento
    for indice, elemento in enumerate(list(grupos)):
        plt.scatter(x=np.array(x[elemento]), y=np.array(y[elemento]), color=cmap(indice / len(grupos)), label=elemento)
    plt.scatter(x=prediccion[0], y=prediccion[1], color="gray", label="Valor a predecir")
    plt.legend()
    plt.show()

# Generamos una función con la entrada
# datos donde pasaremos los datos de entrenamiento y
# k el número de vecinos que agarrará
# predicción que son los datos con los que vamos a buscar el resultado

def kVecinos (datos, k, prediccion):
    elementos_juntos = list(zip(*datos.values())) #Juntamos los valores en las listas que contienen los diccionarios y al resultado lo convertimos a una lista de listas
    llaves = datos[list(datos.keys())[-1]]

    distancias = list() #Generamos una lista vacia donde guardaremos las distancias euclidianas
    conteo = {} #Generamos un diccionario vacio donde vamos a almacenar los resultados que se tengan
    coordX = {}
    coordY = {}

    for indice, elemento in enumerate(elementos_juntos): #Iteramos a la variable elementos juntos obtenemos su índice y su valor
        resultado= distanciaEuclidiana([elemento[0], elemento[1]], prediccion) #Guardaremos el resultado de la distancia euclidiana
        distancias.append({indice: resultado}) #Guardamos en la lista de distancias el resultado que salío donde su clave es el índice en el que estamos iterando
        if elemento[-1] in coordX: coordX[elemento[-1]].append(elemento[0])
        else: coordX[elemento[-1]] = [elemento[0]]

        if elemento[-1] in coordY: coordY[elemento[-1]].append(elemento[1])
        else: coordY[elemento[-1]] = [elemento[0]]
    distancias= sorted(distancias, key= lambda x: list(x.values())[0]) #Una vez finaliza el ciclo ordenamos la lista por medio de los valores que este tenga

    for elemento in distancias[:k]: #iteramos cada elemento de la lista distancias que va desde el elemento 0 hasta el número del elemento que queremos obtener
        indice = next(iter(elemento.keys())) #Obtenemos la clave del elemento que estamos iterando
        resultado = elementos_juntos[indice][-1] #Obtenemos el resultado que tiene esa posición accediendo al último elemento de la misma lista

        if resultado in conteo: #Si la clave ya existe en el diccionario conteo sumaremos uno al valor que este actualmente
            conteo[resultado]= conteo[resultado] + 1
        else: #De lo contrario guardamos en el diccionario el valor e inicializamos en uno ese valor
            conteo[resultado]= 1

    generarGrafica(set(llaves), coordX, coordY, prediccion)
    prediccion_final = max(conteo, key=conteo.get) #Obtenemeos el valor máximo del diccionario y obtendremos la clave que este contiene
    print(f"\nLa predicción es: {prediccion_final}") #Imprimimos en consola el resultado de la predicción

entrada:dict = {
    "horas":       (10, 15, 18, 20, 25, 30),
    "asistencias": (8, 10, 12, 15, 15, 18),
    "resultados": ("Aprobado", "Aprobado", "Reprobado", "Reprobado")
}

entrada2:dict = {
    "duracion": (30, 45, 60, 20, 25, 40),
    "calorias": (300, 450, 600, 120, 150, 200),
    "Categoria": ("Aeróbico", "Aeróbico", "Aeróbico", "Fuerza", "Fuerza", "Fuerza")
}


kVecinos(entrada, 3, [17, 11])
kVecinos(entrada, 5, [17, 11])
kVecinos(entrada2, 3, [35, 320])
kVecinos(entrada2, 5, [35, 320])
