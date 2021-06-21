"""
Polimorfismo -> Qualidade ou estado de ser capaz de
assumir diferentes formas
poli -> muitas
morfo -> formas
"""


class Animal:  # Super classe, classe pai
    def __init__(self, cor, tamanho, peso):
        self.cor = cor
        self.tamanho = tamanho
        self.peso = peso

    def correr(self):
        print('Correr')
        print('como')
        print('um')

    def dormir(self):
        print('Dormir')


class Cao(Animal):  # Subclasse, classe filha
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor,tamanho,peso)

    def latir(self):
        print('Latir')

    # Sobreescrita de método -> override
    def correr(self):
        super().correr()
        print('cão')


class Passaro(Animal):  # Subclasse, classe filha
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor,tamanho,peso)
    def voar(self):
        print('Voar')

    def correr(self):
        super().correr()
        print('passaro')


cao = Cao('Marrom', '40cm', '1kg')
print(cao.cor)
cao.correr()

passaro = Passaro('Amarelo', '30cm', '500g')
