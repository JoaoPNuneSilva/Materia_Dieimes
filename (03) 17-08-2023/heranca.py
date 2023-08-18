import os

class Pessoa:
    def __init__(self, nome, sobrenome):
        os.system("cls")
        self.nome = nome
        self.sobrenome = sobrenome

    def mostrar_dados(self):
        print(self.nome, self.sobrenome)

class Professor(Pessoa):
    ...
class Aluno(Pessoa):
    ...

Professor1 = Professor ("Dieimes", "Nunes")
Aluno1 = Aluno ("João Pedro", "Nunes da Silva")

Professor1.mostrar_dados()
Aluno1.mostrar_dados()