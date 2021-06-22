"""
Atributos de classe
Atributos de instância
"""


# class Pessoa:
#     planeta = 'Terra'
#
#     def __init__(self):
#         self.nome = 'sem nome'
#
#
# Pessoa.planeta = 'Marte'
#
# gustavo = Pessoa()
# gustavo.nome = 'Gustavo'
# print(gustavo.planeta)
#
# ana = Pessoa()
# ana.nome = 'Ana'
# print(ana.planeta)

"""
Método de classe
Método de instância
 """


class Pessoa:
    planeta = 'Terra'

    def __init__(self, nome):
        self.nome = nome
    # Vê apenas a instância
    def exibir_nome(self):
        print(f'Nome: {self.nome}')

    # Vê apenas a classe e não a instância
    @classmethod
    def exibir_planeta(cls):
        print(cls.planeta)

    # Não sabe nada sobre a classe ou a instância
    @staticmethod
    def recuperar_planetas_habitaveis():
        print('Terra e Marte')


gustavo = Pessoa('Gustavo')
gustavo.exibir_nome()
gustavo.exibir_planeta()

ana = Pessoa('Ana')
ana.exibir_nome()

Pessoa.exibir_planeta()
