"""
Modulo Collection - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

Recap Dicionário:
dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])

Default dict -> Ao criar um dicionário utilizando o default dict, nos informamos um valor default, podendo utilizar um
lambda para isso. Este valor será utilizando sempre que não houver valor um valor definido. Caso tentemos acessar uma
chave que não existe, essa chave será criada e o valor default será atribuído

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entradas e retornar valores.

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não.

print(dicionario)


from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

s = sorted(d.items())
print(s)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

Cria uma chave se não existente e adiciona o valor dentro de uma lista, caso a chave ja exista, dicionários não aceitam
uma mesma chave, apenas o valor é adicionado a lista.

sorted(d.items())
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não.

print(dicionario)
