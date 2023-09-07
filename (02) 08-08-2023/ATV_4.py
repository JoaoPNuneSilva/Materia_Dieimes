class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}.")

    def aniversario(self):
        self.idade += 1
        print(f"Parabéns! Hoje é o aniversário de {self.nome}. Agora tenho {self.idade} anos.")

# Criando um objeto da classe Estudante com informações
estudante1 = Estudante("Alice", 18, "Engenharia")
estudante2 = Estudante("Bob", 20, "Ciência da Computação")
estudante3 = Estudante("Carol", 22, "Medicina")

# Chamando o método aniversario para aumentar a idade do estudante em 1 junto ao método apresentar
estudante1.apresentar()
estudante1.aniversario()
print("")
estudante2.apresentar()
estudante2.aniversario()
print("")
estudante3.apresentar()
estudante3.aniversario()

# # Chamando o método apresentar para mostrar as novas informações
# estudante1.apresentar()
# estudante2.apresentar()
# estudante3.apresentar()