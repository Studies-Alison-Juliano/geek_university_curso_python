"""
Min e Max

max() -> Retorna o maior valor de um iterável ou o maior de dois ou mais elementos.

# Exemplos
lista = [1, 8, 4, 99, 35, 129]
print(max(lista))  # 129

tupla = (1, 8, 4, 99, 35, 129)
print(max(lista))  # 129

set = {1, 8, 4, 99, 35, 129}
print(max(set))  # 129

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 35, 'f': 129}
print(max(dicionario.values()))  # 129
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Faça um programa que receba doi valores do usuário e mostre o maior
val1 = int(input('n :'))
val2 = int(input('n2 :'))
print(max(val1, val2))

print(max(4, 67, 82))  # 82
print(max('a', 'ab', 'abc'))  # abc
print(max('a', 'b', 'c', 'g'))  # g
print(max(3.145, 5.789))  # 5.789
print(max('Geek University'))  # y

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

{ mesma coisa que max() só que o inverso }

# Outros exemplos

nomes = ['Arya', 'Simom', 'Dora', 'Tim', 'Olivander']
print(max(nomes))  # Tim
print(min(nomes))  # Arya
print(max(nomes, key=lambda nome: len(nome)))  # Olivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim

"""

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock, to yong to die', 'tocou': 32}
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO!
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
