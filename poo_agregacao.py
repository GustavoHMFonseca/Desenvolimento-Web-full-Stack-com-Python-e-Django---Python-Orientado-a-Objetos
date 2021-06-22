"""
Relação de Agregação -> uma classe precisa da outra
para executar sua ação, ou seja, uma classe utiliza
a outra como parte de si.
"""


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if len(self.produtos) == 0:
            print('Carrinho ainda existe, mas sem produtos')
        for produto in self.produtos:
            print(f'{produto.nome} R$ {produto.preco}')


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def cadastrar_produto(self):
        pass

    def remover_produto(self):
        pass


carrinho = Carrinho()

# produto1 = Produto('Notebook Acer', 3000)
# produto2 = Produto('Iphone', 8000)
# produto3 = Produto('Controle Xbox', 300)
#
# carrinho.adicionar_produto(produto1)
# carrinho.adicionar_produto(produto2)
# carrinho.adicionar_produto(produto3)

carrinho.listar_produtos()
