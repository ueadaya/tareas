# Definir las ciudades, días de la semana y semanas
ciudades = ["Ciudad Ambato", "Ciudad Babahoyo", "Ciudad Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semanada 4"]

# Crear la matriz 3D
matriz_temperaturas = []

# Llenar la matriz con temperaturas aleatorias
import random

for ciudad in ciudades:
    matriz_ciudad = []
    for semana in semanas:
        matriz_semana = []
        for dia in dias_semana:
            temperatura = random.randint(20, 35)  # Generar una temperatura aleatoria entre 20 y 35 grados
            matriz_semana.append(temperatura)
        matriz_ciudad.append(matriz_semana)
    matriz_temperaturas.append(matriz_ciudad)

# Calcular el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for j, semana in enumerate(semanas):
        promedio_semana = sum(matriz_temperaturas[i][j]) / len(matriz_temperaturas[i][j])
        promedio_semana_redondeado = round(promedio_semana, 1)  # Redondear el promedio a 1 decimal
        print(f"{semana}: {promedio_semana_redondeado}°C")


def calcular_temperatura_promedio(matriz_temperaturas, ciudad, semana):
    # Obtener el índice de la ciudad y la semana en las listas
    indice_ciudad = ciudades.index(ciudad)
    indice_semana = semanas.index(semana)

    # Obtener la lista de temperaturas de la ciudad y la semana específicas
    temperaturas = matriz_temperaturas[indice_ciudad][indice_semana]

    # Calcular el promedio de temperaturas
    promedio = sum(temperaturas) / len(temperaturas)

    # Redondear el promedio a 1 decimal
    promedio_redondeado = round(promedio, 1)

    return promedio_redondeado


temperatura_promedio = calcular_temperatura_promedio(matriz_temperaturas, "Ciudad Ambato", "Semana 1")
print(f"La temperatura promedio en Ciudad Ambato durante la Semana 1 es de {temperatura_promedio}°C.")
