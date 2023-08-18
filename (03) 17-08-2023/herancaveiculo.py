class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.tipo_moto = tipo_moto

    def exibir_info(self):
        