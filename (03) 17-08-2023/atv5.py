class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor, marca, modelo):
        self.motor = motor
        self.marca = marca
        self.modelo = modelo

motor_gasolina = Motor("Gasolina", 150)

carro = Carro(motor_gasolina, "Toyota", "Corolla")

print(f"Carro: {carro.marca} {carro.modelo}")
print(f"Motor: Tipo: {carro.motor.tipo}, Potência: {carro.motor.potencia} cavalos")