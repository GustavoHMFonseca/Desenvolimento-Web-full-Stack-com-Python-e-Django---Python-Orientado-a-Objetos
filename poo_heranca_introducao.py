# Heranca - Reutilização e manutenção
# Classe: Cao Passaro
class Animal:# Super classe, classe pai
    def __init__(self):
        self.com = ''
        self.tamanho = ''
        self.peso = ''

    def correr(self):
        print('Correr')

    def dormir(self):
        print('Dormir')


class Cao(Animal):# Subclasse, classe filha

    def latir(self):
        print('Latir')


class Passaro(Animal):# Subclasse, classe filha

    def voar(self):
        print('Voar')


cao = Cao()
cao.cor = 'Marrom'
cao.correr()
cao.dormir()
cao.latir()
print(cao.cor)

passaro = Passaro()
passaro.cor = 'Amarelo'
passaro.correr()
passaro.dormir()
passaro.voar()
print(passaro.cor)
