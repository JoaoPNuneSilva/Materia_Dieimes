class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        if self.saldo >= valor + 2:
            self.saldo -= valor + 2
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        else:
            return False

# Criando objetos
conta1 = ContaBancaria("Titular 1", 1000)
conta_poupanca1 = ContaPoupanca("Titular Poupança", 500)
conta_corrente1 = ContaCorrente("Titular Corrente", 200, 300)

# Realizando operações
conta1.depositar(200)
conta_poupanca1.depositar(300)
conta_corrente1.depositar(100)

conta1.sacar(150)
conta_poupanca1.sacar(100)
conta_corrente1.sacar(300)

# Exibindo informações
print(f"Saldo Conta 1: R${conta1.saldo:.2f}")
print(f"Saldo Conta Poupança 1: R${conta_poupanca1.saldo:.2f}")
print(f"Saldo Conta Corrente 1: R${conta_corrente1.saldo:.2f}")
