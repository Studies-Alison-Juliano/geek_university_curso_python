"""
List Comprehension pt 2

Nós podemos adicionar estruturas condicionais logicas as nossas list comprehension
"""
# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6]
pares = [n1 for n1 in numeros if n1 % 2 == 0]
impares = [n1 for n1 in numeros if n1 % 2 != 0]
print(pares)
print(impares)

# Refatorar
# Qualquer número par módulo de 2 é 0 e 0 em python é False. Not False = True
pares = [n1 for n1 in numeros if not n1 % 2]
# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
impares = [n1 for n1 in numeros if n1 % 2]
print(pares)
print(impares)

# Exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
