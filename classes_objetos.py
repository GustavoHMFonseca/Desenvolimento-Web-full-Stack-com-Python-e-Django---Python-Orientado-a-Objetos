"""
notação Pascal case: ContaBancaria
notação Camel case: contaBancaria
notação Snake Case: conta_bancaria
"""
# def calcular():
#     pass


class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor


conta = Conta("Gustavo", 1000)
# conta.depositar(100)
conta.sacar(100)
print(f'Nome: {conta.nome} Saldo:{conta.saldo}')

conta = Conta("Maria", 800)
# conta.depositar(100)
conta.sacar(100)
print(f'Nome: {conta.nome} Saldo:{conta.saldo}')
