# Programa Tradicional para determinar el promedio semanal del clima

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    print("Programa para determinar el promedio semanal del clima.")
    temperaturas_semanales = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas_semanales)
    print(f"El promedio semanal del clima es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
