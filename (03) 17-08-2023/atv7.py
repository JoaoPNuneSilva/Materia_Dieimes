class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}, Data: {self.data}"

# Criando objetos
documento = Documento("Documento Genérico", "Conteúdo qualquer")
email = Email("Email Importante", "Conteúdo confidencial", "remetente@example.com", "destinatario@example.com")
relatorio = Relatorio("Relatório Mensal", "Análise de vendas", "01/08/2023")

# Exibindo informações
print(documento.exibir())
print(email.exibir())
print(relatorio.exibir())
