from abc import ABC, abstractmethod


# class Animal(ABC):
#     def correr(self):
#         print('Correr')
#
#     @abstractmethod
#     def respirar(self):
#         pass
#
#
# class Cao(Animal):
#     def respirar(self):
#         print('Respirar como um cão')
#
#
# class Passaro(Animal):
#     def respirar(self):
#         print('Respirar como um passaro')
#
#
# # animal = Animal()
# # animal.correr()
# cao = Cao()

"""
Conta bancária
Conta, Conta corretne e conta poupança
"""
class Conta(ABC):
    def __init__(self, numero_conta, saldo):
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def __init__(self,numero_conta, saldo):
        super().__init__(numero_conta, saldo)

    def sacar(self, valor):
        limite = 300
        if valor <= limite:
            self._saldo -= valor
        else:
            print(f'Limite excedido (R${limite})')


class ContaCorrente(Conta):
    def __init__(self,numero_conta, saldo):
        super().__init__(numero_conta, saldo)

    def sacar(self, valor):
        limite = 600
        if valor <= limite:
            self._saldo -= valor
        else:
            print(f'Limite excedido (R${limite}) ')


conta = ContaCorrente(15256, 1000)
conta.depositar(200)
conta.sacar(850)
print(conta.saldo)