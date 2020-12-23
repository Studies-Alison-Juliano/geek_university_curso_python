"""
Modulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

Recap Tupla:
tupla = (1, 2, 3)
print(tupla[1])

Named tupla -> São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros
"""
# Importando
from collections import namedtuple
from collections import OrderedDict

# Precisamos definir o nome e parâmetros
# Forma 1 - Declaração namedtuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração namedtuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='ray')
print(ray)

# Acessando os dados
# Forma 1

print(ray[0])  # Idade
print(ray[1])  # raca
print(ray[2])  # nome

# Forma 2
print(ray.idade)  # Idade
print(ray.raca)  # raca
print(ray.nome)  # nome

