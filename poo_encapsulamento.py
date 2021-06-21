"""
Pilar 2 - Encapsulamento
"""

class Filtro:
    def __init__(self, imagem):
        self.imagem = imagem

    def preto_e_branco(self):
        print(f'{self.imagem} com filtro preto e branco')

    def foto_envelhecida(self):
        print(f'{self.imagem} com filtro envelhecido')


# filtro = Filtro('foto_Carro')
# filtro.preto_e_branco()

# Controle de acesso e Getter e Setters
class Conta:
    def __init__(self, numero, saldo):
        self._numero = numero
        self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor


conta = Conta(10585, 800)
conta.numero = 10856
print(conta.numero)
# conta.sacar(100)
# conta.depositar(200)



