class Estudante:
    def __init__(self, nome):
        self.nome = nome

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

joao = Estudante ("João")
maria = Estudante ("Marcia")

turmaA = Turma("Turma A")
turmaA.adicionar_estudante(joao)
turmaA.adicionar_estudante(maria)