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

    def __str__(self):
        return f'cor: {self.cor}, tamanho: {self.tamanho}, peso: {self.peso}'


class Cao(Animal):  # Subclasse, classe filha
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor,tamanho,peso)
        self.peso = f'{peso} Kg'
        # self.raca = raca

    def latir(self):
        print('Latir')

    # Sobreescrita de método -> override
    def correr(self):
        super().correr()
        print('cão')

    def __str__(self):
        return super().__str__() + f', Raça : {self.raca}'


class Passaro(Animal):  # Subclasse, classe filha
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor,tamanho,peso)
    def voar(self):
        print('Voar')

    def correr(self):
        super().correr()
        print('passaro')


class Papagaio(Passaro, Cao):
    def __init__(self, cor, tamanho, peso):
        super().__init__(cor,tamanho,peso)
    def falar(self):
        print('Falar')


# cao = Cao('Marrom', '40cm', '1', 'Golden')
# print(cao)
# cao.correr()

passaro = Passaro('Amarelo', '30cm', '500g')
print(passaro)

papagaio = Papagaio('Verde', '30cm', '500g')
papagaio.correr()
papagaio.voar()
papagaio.falar()
papagaio.latir()

