lista = ['teste','teste2']
dicionario= {'nome': 'Rafaela'}

try:  # tentar
    print(lista[2])
    # print(dicionario['teste'])
except (IndexError, KeyError) as erro:  # exceto
    print('Item selecionado fora da lista')
except Exception as erro:  # exceto
    print(f'Exception: {erro}')
else:
    print('Executado com sucesso')
finally:
    print('Executando não importa o que aconteça')

print('Continua executando')
