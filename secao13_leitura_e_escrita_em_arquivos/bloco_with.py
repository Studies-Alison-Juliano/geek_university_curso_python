"""
O bloco with

Passos para se trabalhar com arquivos
# 1 - Abrir o arquivo
# 2 - Manipulação de arquivo
# 3 - Fechamento de arquivo

O bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados são fechados após o bloco with.

"""
# O bloco with - Forma Pythônica de manipular arquivos
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)  # False

print(arquivo.closed)  # True

