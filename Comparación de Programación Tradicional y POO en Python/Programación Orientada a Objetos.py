# Programa Orientado a Objetos para determinar el promedio semanal del clima

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    print("Programa para determinar el promedio semanal del clima.")
    clima_semanal = ClimaSemanal()
    clima_semanal.ingresar_temperaturas()
    promedio = clima_semanal.calcular_promedio()
    print(f"El promedio semanal del clima es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
