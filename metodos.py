# Métodos
# cadastro email: gh@gmail.com senha 1234

class Usuario:
    # def __init__(teste, email,senha):
    #     teste.email = email
    #     teste.senha = senha(isso tbm funciona)
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

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


usuario = Usuario('gh@gmail.com', '1234567')
#usuario.logar()
if usuario.forca_senha():
    print('Senha Forte')
else:
    print('Senha Fraca')
