"""
Relação de Composição -> a classe principal(todo) cria
uma instância do outra classe(parte), que se torna parte dela.
Quando a classe principal for destruída, sua instância da
outra classe também será
"""


class Usuario:  #todo
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, cep, cidade, rua):
        endereco = Endereco(cep, cidade, rua)
        self.enderecos.append(endereco)

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __del__(self):
        print(f'{self.nome} A P A G A D O')


class Endereco:  #parte
    def __init__(self, cep, cidade, rua):
        self.cep = cep
        self.cidade = cidade
        self.rua = rua

    def __del__(self):
        print(f'{self.rua} A P A G A D O')

    def __str__(self):
        return f'cep: {self.cep}, cidade: {self.cidade}, rua: {self.rua}'


usuario = Usuario('Rafaela')

usuario.inserir_endereco('03890-200', 'São Paulo', 'Rua tal, número 1')
usuario.inserir_endereco('04827-300', 'São Paulo', 'Rua nova, número 13')

usuario.lista_enderecos()
