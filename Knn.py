import math #Importamos la libreria math para poder acceder a las funciones como la raiz cuadrada

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
    elementos_juntos = list(zip(*datos.values()))
    distancias = list()
    conteo = {}
    #print(list(c))
    for indice, elemento in enumerate(elementos_juntos):
        resultado= distanciaEuclidiana([elemento[0], elemento[1]], prediccion)
        distancias.append({indice: resultado})
    distancias= sorted(distancias, key= lambda x: list(x.values())[0])

    for elemento in distancias[:k]:
        indice = next(iter(elemento.keys()))
        resultado = elementos_juntos[indice][-1]
        print(resultado)

        if resultado in conteo:
            conteo[resultado]= conteo[resultado] + 1
        else:
            conteo[resultado]= 1
    print(conteo)
    print(f"La repetición maxima es de: {max(conteo.values())}")
    return max(conteo.values())

entrada:dict = {
    "horas":       (10, 15, 18, 20, 25, 30),
    "asistencias": (8, 10, 12, 15, 15, 18),
    "resultados": ("Aprobado", "Aprobado", "Reprobado", "Reprobado")
}

kVecinos(entrada, 3, [17, 11])
