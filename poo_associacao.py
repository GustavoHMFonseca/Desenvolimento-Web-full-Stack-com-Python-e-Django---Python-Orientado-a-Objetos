"""
Relação de Associação -> É uma das relações mais comuns
entre dois objetos, acontece quando um objeto "utiliza"
outro, porém, sem que eles dependam um do outro.
"""
# teste = ''
# teste3 = None  # null
# del teste3
# print(teste3)


class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.video_game = None

    def andar(self):
        print(f'Jogador {self.nome} andando')


class VideoGame:
    def __init__(self, nome):
        self.nome = nome

    def rodar_jogo(self):
        print(f'Rodar Jogo no {self.nome}')


pessoa = Pessoa('João')
videogame = VideoGame('Xbox')

pessoa.video_game = videogame
pessoa.video_game.rodar_jogo()
