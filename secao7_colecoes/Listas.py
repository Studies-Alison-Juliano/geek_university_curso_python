"""
Listas

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

Listas em Python funcionam como vetores/matrizes (arrays em outras linguagens), com a diferença de serem DINÂMICOS e
também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, se vc criar um array do tipo int e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter
    sempre no maximo 5 valores

Ja em Python:
- DINÂMICO: Não possuem tamanho fixo; Ou seja podemos criar uma lista e simplesmente ir adicionando elementos
- Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado

As listas de Python são representadas entre [] (colchetes)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente checar se determinado valor está contido na lista

num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Adicionar elementos em lista
# Para adicionar elementos em lista utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# Obs: Com append só conseguimos adicionar um elemento por vez. Exp: lista1.append(1, 2, 3, 4) - Erro

lista1.append([8, 3, 1])  # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 77])  # Coloca cada elemento da lista como valor adicional a lista. OBS: Apenas iteráveis
print(lista1)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos inserir um novo elemento na lista informando a posição do índice.
  OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista

lista1.insert(2, 'Novo Mundo')  # Primeiro numero é a posição e o segundo é a inserção
print(lista1)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2 ou lista1.extend(lista2)
print(lista1)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente inverter uma lista

lista1.reverse()
lista2.reverse()
print(lista1) ou print(lista1[::-1])
print(lista2) ou print(lista2[::-1])

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Copiar uma lista

lista6 = lista2.copy()  # Lista6 copiara lista2
print(lista6)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos contar quantos elementos existem dentro de uma lista

print(len(lista1))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente remover o último elemento de uma lista
OBS: O pop não somente remove o último elemento mas também o retorna

print(lista5)
lista5.pop()
print(lista5)

- Podemos remover um elemento pelo índice

lista5.pop(2)
print(lista5)

OBS: Os elementos a direita deste índice serão deslocados para esquerda
OBS2: Se não houver elemento no índice informado teremos um erro

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos remover todos os elementos de uma lista (Zerar a lista)

print(lista5)
lista5.clear()
print(lista5)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente repetir elementos em uma lista

print(lista5)
nova = lista5 * 3
print(nova)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos facilmente converter uma string para uma lista

# Exemplo 1:
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas

#Exemplo 2:
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos dizendo: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string

curso = ' '.join(lista6)
print(curso)

# Abaixo estamos dizendo: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string

curso = '$'.join(lista6)
print(curso)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos colocar qualquer tipo de dado dentro de uma lista

lista6 = [1, 2, 34, True, 'Geek', 'd', [1, 2, 3], 123456]
print(lista6)
print(type(lista6))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Iterando sobre lista

- Exemplo 1: Utilizando for

soma = ''   #  Somando tipo string
for elemento in lista2:
    print(elemento)
    soma += elemento
print(soma)

- Exemplo 2: Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Utilizando variareis em uma lista

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Fazemos acesso aos elementos de forma indexado
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazemos acesso aos elementos de forma indexado inverso. Para entender melhor o indice negativo, pense na lista como se
fosse um circulo, onde o final de um elemento está ligado ao inicio da lista

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Gerar indice em um for
cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

for ind, cor in enumerate(cores):
    print(ind, cor)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Outros metodos não tão importantes mas também uteis

# Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6
print(numeros.index(6))

# Em qual índice da lista está o valor 5
print(numeros.index(9))

# OBS: Caso não tenha este elemento na lista será apresentado um erro

# OBS: Retorna o índice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, começar a buscar a partir de um índice
print(numeros.index(5, 1))  # Buscando a partir do índice 1
print(numeros.index(5, 2))  # Buscando a partir do índice 2

# Podemos fazer busca dentro de um range. Inicio/Fim
print(numeros.index(7, 1, 3))  # Buscar o elemento 7 dentro do range de 1 a 3

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Revisão slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro inicio
print(lista1[1:])  # Iniciando no índice 1 e pegando todos os restantes

# Trabalhando com slice de lista com o parâmetro fim
print(lista1[:2])  # Começa no índice 0 e vai até o índice 2

# Trabalhando com slice de lista com o parâmetro passo
print(lista1[1::2])  # Começa no índice 1 e vai até o final pulando de 2 em 2

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Soma*, Valor maximo*, Valor minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais
lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
print(max(lista))  # Valor maximo
print(min(lista))  # Valor minimo
print(len(lista))  # Tamanho da lista
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Desempacotamento de lista

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber os dados, teremos value error

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Copiando uma lista para outra (Shallow copy e Deep copy)

# Forma 1:
lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # Copia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy, copiamos os dados de uma lista para nova lista, mas elas ficaram totalmente
# independentes, ou seja, modificando uma lista, não afeta a outra. Isso em python é chamado de Deep Copy

# Forma 2:
lista = [1, 2, 3]
print(lista)

nova = lista  # Copia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja ue utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar
# modificação em uma das listas, essa modificação refletiu em ambas as listas. Isso em Python é chamado de Shallow Copy
"""
cpf = '280012386'
n = 1
indice = 0
conta = 0
while n < len(cpf)+1:
    conta_cpf = n * int(cpf[indice])  # 1 × 2 + 2 × 8 + 3 × 0 + 4 × 0 + 5 × 1 + 6 × 2 + 7 × 3 + 8 × 8 + 9 × 6 = 174
    conta = conta + conta_cpf
    n += 1
    indice += 1
dv1 = conta % 11
if dv1 == 10:
    dv1 = 0
print(dv1)
