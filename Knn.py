import math #Importamos la libreria math para poder acceder a las funciones como la raiz cuadrada
import pandas as np
import matplotlib.pyplot as pl
"""
Función para sacar la distancia Euclidiana de dos coordenadas
recibe dos listas para sacar esta distancia
"""
def distanciaEuclidiana(distancia1: list, distancia2: list):
    return math.sqrt((distancia1[0]-distancia2[0])**2 + (distancia1[1]-distancia2[1])**2)

# Generamos una función con la entrada
# datos donde pasaremos los datos de entrenamiento y
# k el numero de vecinos que agarrara
# prediccion que son los datos con los que vamos a buscar el resultado

def kVecinos (datos, k, prediccion):
    elementos_juntos = list(zip(*datos.values())) #Juntamos los valores en las listas que contienen los diccionarios y al resultado lo convertimos a una lista de listas
    distancias = list() #Generamos una lista vacia donde guardaremos las distancias euclidianas
    conteo = {} #Generamos un diccionario vacio donde vamos a almacenar los resultados que se tengan

    for indice, elemento in enumerate(elementos_juntos): #Iteramos a la variable elementos juntos obtenemos su índice y su valor
        resultado= distanciaEuclidiana([elemento[0], elemento[1]], prediccion) #Guardaremos el resultado de la distancia euclidiana
        distancias.append({indice: resultado}) #Guardamos en la lista de distancias el resultado que salío donde su clave es el índice en el que estamos iterando
    distancias= sorted(distancias, key= lambda x: list(x.values())[0]) #Una vez finaliza el ciclo ordenamos la lista por medio de los valores que este tenga

    for elemento in distancias[:k]: #iteramos cada elemento de la lista distancias que va desde el elemento 0 hasta el número del elemento que queremos obtener
        indice = next(iter(elemento.keys())) #Obtenemos la clave del elemento que estamos iterando
        resultado = elementos_juntos[indice][-1] #Obtenemos el resultado que tiene esa posición accediendo al último elemento de la misma lista

        if resultado in conteo: #Si la clave ya existe en el diccionario conteo sumaremos uno al valor que este actualmente
            conteo[resultado]= conteo[resultado] + 1
        else: #De lo contrario guardamos en el diccionario el valor e inicializamos en uno ese valor
            conteo[resultado]= 1

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

#generarGrafica(entrada["horas"], entrada["asistencias"], entrada["resultados"], [17, 11])

#kVecinos(entrada, 3, [17, 11])
#kVecinos(entrada2, 3, [35, 320])
kVecinos(entrada2, 5, [35, 320])
