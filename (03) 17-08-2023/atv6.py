#exemplo1
class Autor:
    def __init__(self, nome):
        self.nome = nome

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_info(self):
        return f"'{self.titulo}' escrito por {self.autor.nome}"

# Criando objetos
autor1 = Autor("João Silva")
livro1 = Livro("Aventuras na Floresta", autor1)

print(livro1.mostrar_info())

#exemplo2

class CPU:
    def __init__(self, modelo):
        self.modelo = modelo

class RAM:
    def __init__(self, capacidade):
        self.capacidade = capacidade

class Computador:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def mostrar_info(self):
        return f"Computador com CPU {self.cpu.modelo} e RAM {self.ram.capacidade} GB"

# Criando objetos
cpu1 = CPU("Intel i5")
ram1 = RAM(8)
computador1 = Computador(cpu1, ram1)

print(computador1.mostrar_info())
