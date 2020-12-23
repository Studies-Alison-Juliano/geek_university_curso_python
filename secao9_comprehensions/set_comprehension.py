"""
Set Comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""
# Exemplo
numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo 2
numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio! Faça uma alteração na estrutura a cima para gerar um dicionário ao invés de set
# Exemplo 3 (dicionário)
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para finalizar
letras = {letra for letra in 'Geek University'}
print(letras)
