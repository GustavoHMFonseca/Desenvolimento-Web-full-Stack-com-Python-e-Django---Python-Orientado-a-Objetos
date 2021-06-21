def passo1(p1):
    p1 = f'--{p1}--'

    def passo2(p2):
        print( f'{p1} e {p2}')

    return passo2


# retorno = passo1('Abrir a porta')
# # teste = retorno('Entrar no quarto')
# passo1('Abrir a porta')('Entrar no quarto')

def verifica_usuario_logado(funcao):
    def verifica():
        print('[Antes vamos verifivar se o usuário está logado]')
        retorno = funcao()
        print('[FIM]')
        return retorno
    return verifica


@verifica_usuario_logado
def salvar_postagem():
    print('....[executando]')
    print('Postagem criada')


@verifica_usuario_logado
def salvar_comentario():
    print('....[executando]')
    print('Comentário criado')


salvar_comentario()
