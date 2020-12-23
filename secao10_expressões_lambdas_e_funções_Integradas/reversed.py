"""
Reversed

OBS:Não confunda com a função reverse() que estudamos nas listas

A função reverse() apenas funciona em lista.
Ja a função reversed() funciona com qualquer iterável

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""
# Exemplo
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, Tupla ou conjunto
# Lista
print(list(reversed(lista)))
# Tupla
print(tuple(reversed(lista)))
# Conjunto (Set)
print(set(reversed(lista)))

# Iterar sobre um reversed()
for letra in reversed(lista):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for
print(''.join(reversed('Geek University')))

print('Geek University'[::-1])

# Loop reversed()
for n in reversed(range(10)):
    print(n)
