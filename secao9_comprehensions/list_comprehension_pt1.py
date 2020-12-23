"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da list comprehension:

[ dado for dado in iteravel ]

# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [n1 * 10 for n1 in numeros]
print(res)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Para entender melhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for n2 in numeros
- A segunda parte: n1 * 10

res = [n1 / 2 for n1 in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(n1) for n1 in numeros]
print(res)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# List comprehension versos Loop

# Loop
numeros_dobrados = []
for n in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(n * 2)
print(numeros_dobrados)

# List Comprehension
print([n1 * 2 for n1 in [1, 2, 3, 4, 5]])
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""
# Outros Exemplos
string = 'Geek University'
print([letra.upper() for letra in string])

# Exemplo 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'pedro', 'guilherme', 'vanessa', 'julia']
print([caixa_alta(amigo) for amigo in amigos])

# Exemplo 3
print([numero * 3 for numero in range(1, 10)])

# Exemplo 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])
