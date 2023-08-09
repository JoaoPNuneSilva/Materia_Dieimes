#ATV_1
class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando um objeto da classe Estudante
estudante1 = Estudante("Alice", 18)

# Chamando o método apresentar para exibir a mensagem formatada
estudante1.apresentar()
