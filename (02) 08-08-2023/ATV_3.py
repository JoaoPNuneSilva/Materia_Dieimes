class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}.")

# Criando três objetos da classe Estudante com diferentes informações, incluindo curso
estudante1 = Estudante("Alice", 18, "Engenharia")
estudante2 = Estudante("Bob", 20, "Ciência da Computação")
estudante3 = Estudante("Carol", 22, "Medicina")

# Chamando o método apresentar para exibir as informações dos estudantes, incluindo o curso
estudante1.apresentar()
estudante2.apresentar()
estudante3.apresentar()