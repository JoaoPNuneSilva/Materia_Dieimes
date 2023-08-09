class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando três objetos da classe Estudante com diferentes informações
estudante1 = Estudante("Alice", 18)
estudante2 = Estudante("Bob", 20)
estudante3 = Estudante("Carol", 22)

# Chamando o método apresentar para exibir as informações dos estudantes
estudante1.apresentar()
estudante2.apresentar()
estudante3.apresentar()