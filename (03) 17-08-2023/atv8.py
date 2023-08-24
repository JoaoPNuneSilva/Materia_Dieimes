class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto_valor = self.preco * (percentual / 100)
        preco_com_desconto = self.preco - desconto_valor
        return preco_com_desconto

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def desconto(self, percentual):
        desconto_geral = super().desconto(percentual)
        desconto_livro = desconto_geral * 0.10
        preco_com_desconto = desconto_geral - desconto_livro
        return preco_com_desconto

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma

# Criando objetos
produto1 = Produto("Produto Genérico", 100)
livro1 = Livro("Livro Interessante", 50, "Autor Incrível")
jogo1 = Jogo("Jogo Incrível", 60, "PS5")

# Aplicando descontos
desconto_produto1 = produto1.desconto(10)
desconto_livro1 = livro1.desconto(10)
desconto_jogo1 = jogo1.desconto(20)

# Exibindo preços com desconto
print(f"Produto 1 com desconto: R${desconto_produto1:.2f}")
print(f"Livro 1 com desconto: R${desconto_livro1:.2f}")
print(f"Jogo 1 com desconto: R${desconto_jogo1:.2f}")
