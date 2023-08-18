class SistemaOperacional:
    def __init__(self, nome, versao ): #método construtor, cria instância da classe
        self.nome = nome
        self.versao = versao

    def mostrar_sistema_operacional(self):
        return f"{self.nome}. {self.versao}"

class Computador:
    def __init__(self, sistema, ): #método construtor, cria instância da classe
        self.sistema = sistema

    def mostrar_informacoes(self):
        return f"{self.sistema} tem o sistema operacional {sistema_pc.mostrar_sistema_operacional()}"
    
sistema_pc = SistemaOperacional ("Windows", "44817")
pc = Computador ("Computador de mesa")

print(pc.mostrar_informacoes())