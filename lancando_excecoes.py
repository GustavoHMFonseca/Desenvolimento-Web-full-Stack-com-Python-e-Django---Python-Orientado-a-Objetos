# def dividir(n1, n2):
#     try:
#         print(f'resultado: {n1/n2}')
#     except ZeroDivisionError as erro:
#         #print(f'Erro na função: {erro}')
#         raise


# try:
#     dividir(10,0)
# except ZeroDivisionError as erro:
#     print(f'Erro desenvolvedor: {erro}')
# print('Executando normalmente')

# def dividir(n1, n2):
#     if n2 == 0:
#         raise ValueError('Não é possivel dividir por zero.')
#     print(f'resultado:{n1/n2}')
#
# try:
#     dividir(10,0)
# except Exception as erro:
#     print(erro)
class OpcaoInvalidaError(Exception):
    pass


def seleciona_opcao(opcao):
    if opcao == '1':
        print('Cartões de crédito')
    elif opcao == '2':
        print('Financiamentos')
    else:
        raise OpcaoInvalidaError('Opção inválida')


try:
    seleciona_opcao('3')
except OpcaoInvalidaError as erro:
    print(erro)
print('Executando normalmente.')
