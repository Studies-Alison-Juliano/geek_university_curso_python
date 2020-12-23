"""
1. https://i.imgur.com/dK3TTeK.png

import os

# Criação de arquivos e diretórios com except caso arquivo/diretório ja exista
try:
    os.mkdir('C:/Users/aliso/PycharmProjects/guppe/Exercicios/arquivos_diretorios')
    os.mkdir('C:/Users/aliso/PycharmProjects/guppe/Exercicios/arquivos_diretorios/ex1')
    os.open('C:/Users/aliso/PycharmProjects/guppe/Exercicios/arquivos_diretorios/ex1/arq.txt', 0o600)
except FileExistsError:
    print('Arquivo/diretório ja existentes! \n')

# Input de conteúdo no arquivo
with open('arquivos_diretorios/ex1/arq.txt', 'a+') as arquivo:
    while True:
        text1 = input('Informe qualquer coisa ou digite 0 para finalizar:')
        if text1 != '0':
            arquivo.write(text1 + '\n')
        else:
            break
    arquivo.seek(0)
    print(arquivo.read())

# Quantas linhas e quantas vogais há no arquivo
with open('arquivos_diretorios/ex1/arq.txt') as linhas:
    print(f'Existem {len(linhas.readlines())} linhas de texto no arquivo')
    linhas.seek(0)
    vogal = (letra for letra in linhas.read() if letra.lower() in ['a', 'e', 'i', 'o', 'u'])
    print(f'Existem {len(list(vogal))} vogais no arquivo')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
2. https://i.imgur.com/TcZZzzR.png

import os

try:
    os.mkdir('arquivos_diretorios/ex2')
    os.open('arquivos_diretorios/ex2/ex2.txt', 0o600)
except FileExistsError:
    print('Ja existente!')

with open('arquivos_diretorios/ex2/ex2.txt', 'a') as arquivo:
    arq1 = open('C:/Users/aliso/PycharmProjects/guppe/workfile.txt').read()
    arq2 = open('C:/Users/aliso/PycharmProjects/guppe/texto.txt').read()
    arquivo.write(arq1 + '\n\n' + arq2)
"""
import os
import io

try:
    os.mkdir('arquivos_diretorios/ex3')
    os.open('arquivos_diretorios/ex3/cidades.txt', 0o600)
except FileExistsError:
    print('Ja existente!')

with io.open('arquivos_diretorios/ex3/cidades.txt', encoding='utf8') as cidade, \
     io.open('arquivos_diretorios/ex3/ex3.txt', 'w', encoding='utf8') as maior_habitante:

    cidade_dict = {k[0]: int(k[1]) for k in (tuple(cit.split(' ')) for cit in cidade.read().split('\n'))}
    maior_habitante.write(f'A cidade com mais habitantes é {max(cidade_dict.keys())} com aproximadamente {max(cidade_dict.values())} habitantes')
