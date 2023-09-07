class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def mostrar_informacoes(self):
        return f"{self.nome}. {self.data_nascimento}"

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacoes(self):
        return f"{self.titulo} tem o autor {self.autor.mostrar_informacoes()}"
    
autor_pessoa = Autor("Vitor Santos", "1990")
livro = Livro("Linguagem Corporal", autor_pessoa)

print(livro.mostrar_informacoes())