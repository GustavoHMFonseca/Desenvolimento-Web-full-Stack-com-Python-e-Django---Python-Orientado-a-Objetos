# Métodos
# cadastro email: gh@gmail.com senha 1234

class Usuario:
    # def __init__(teste, email,senha):
    #     teste.email = email
    #     teste.senha = senha(isso tbm funciona)
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.enderecos = []

    def __str__(self):
        return f'Email: {self.email}, Senha: {self.senha}'

    def __iter__(self):
        return self.enderecos.__iter__()

    def _validar(self):
        email_cadastro = 'gh@gmail.com'
        senha_cadastro = '1234'
        if email_cadastro == self.email and senha_cadastro == self.senha:
            print("Usuário Validado")
        else:
            print("Email ou senha incorretos.")

    def logar(self):
        self._validar()
        print('enviar para a tela principal')

    def forca_senha(self):
        if len(self.senha) > 5:
            return True
        else:
            return False

    # def cadastrar_endereco(self, endereco1, endereco2):
    #     print(f'Endereços: {endereco1}, {endereco2}')
    def cadastrar_endereco(self, *enderecos):
        for endereco in enderecos:
            print(f'Endereços: {endereco}')


usuario = Usuario('gh@gmail.com', '1234567')
usuario.enderecos = ['Rua 1', 'Rua 2', 'Rua 3']

for endereco in usuario:
    print(f'Endereço: {endereco}')

# #usuario.logar()
# if usuario.forca_senha():
#     print('Senha Forte')
# else:
#     print('Senha Fraca')

# lista = ["Rua1", "Rua2"]
# usuario.cadastrar_endereco(*lista)
#usuario.cadastrar_endereco('Rua 1', 'Rua 2', 'Rua 3')
