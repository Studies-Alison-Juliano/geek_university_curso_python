"""
Exercícios seção 7

1 - https://i.imgur.com/69T2Lc3.png
R.

vetor = [1, 0, 5, -2, -5, 7]
print(vetor)
soma = vetor[0] + vetor[1] + vetor[5]
print(soma)
vetor[4] = 100
print(vetor)
for n in vetor:
    print(n)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

2 - https://i.imgur.com/ovS1X6g.png
R.

conjunto = []
conjunto1 = []

for q in range(11):
    r = float(input(f'{q}/10 - Informe um numero real: \n'))
    conjunto.append(r)
    conjunto1.append(round(r ** 2, 2))

print(conjunto)
print(conjunto1)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

3 - https://i.imgur.com/65mCyB7.png
R.

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8]
xy = random.sample(lista, k=2)  # Seleciona dois números randomicos da lista
print(f'X = {xy[0]} Y = {xy[1]} e soma dos dois é: {sum(xy)}')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

4 - https://i.imgur.com/lD8fEkk.png
R.

lista = []
par = []
for v in range(10):
    Q = int(input('Informe qualquer valor: '))
    lista.append(Q)

for n in lista:
    contap = n % 2
    if contap == 0:
        par.append(n)

n = 0
numeros = []
for l in par:
    numeros.append(str(l))

print(f'Existem na lista {len(par)} números pares e eles são: {", ".join(numeros)}')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

5- https://i.imgur.com/8sUvkeQ.png
R.

lista = []

for v in range(10):
    Q = int(input('Informe qualquer valor: '))
    lista.append(Q)

conjunto = set({})
for n in lista:
    if lista.count(n) > 1:
        conjunto.add(str(n))

print(f'O(s) números {", ".join(conjunto)} aparecem mais de uma vez na lista')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

6 - https://i.imgur.com/L6KxeSA.png
R.

lista = []
for v in range(1, 5+1):
    Q = int(input('Informe qualquer valor: '))
    lista.append(Q)

desire = int(input('Type 1 if you want to see the list or 2 to see inverse mode of the list or 0 to exit: '))
if desire == 0:
    print('Até a próxima')
elif desire == 1:
    print(lista)
elif desire == 2:
    print(lista[::-1])
else:
    print('Numero invalido!')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

7 - https://i.imgur.com/un0X3gR.png
R.

v1 = [2, 10, 55, 6, 7, 8, 9, 10, 11, 12]
v2 = [1, 20, 55, 20, 33, 77, 88, 5, 8, 9]
vf = []

for n1 in v1:
    vf.append(n1)

cp = 1
for n2 in v2:
    vf.insert(cp, n2)
    cp += 2

print(vf)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

8 - https://i.imgur.com/RNmq0sj.png

R. Usando tupla e lista
lista = []
es = []
for n in range(1, 10+1):
    aluno = input(f'Informe o nome do {n}°aluno: ')
    altura = float(input(f'Informe a altura do {n}°aluno: '))
    t1 = aluno, altura
    lista.append(t1)
print(lista)

for t in lista:
    es.append(t[1])
print(f'O aluno mais alto é o {lista[es.index(max(es))]} e o mais baixo é o {lista[es.index(min(es))]}')

R. Usando dicionário (Mais completo)

lista = {}
dic = {}
for na in range(1, 10+1):
    nome = input('Informe o nome do aluno: ')
    altura = float(input('Informe a altura do aluno: '))
    dic[f'{nome}'] = altura
for k, v in dic.items():
    if v == max(dic.values()):
        lista[f'{k}'] = v
if len(lista) > 1:
    print('Alunos com a mesma altura e maiores da sala:')
    for n, v in lista.items():
        print(n, 'tem de altura', v, 'm')
else:
    for n1, v1 in lista.items():
        print(n1, 'tem de altura', v1, 'm')


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

9. https://i.imgur.com/Kzkg58b.png
R.

lista = []
contador = 1

while len(lista) < 100:
    if contador % 7 != 0 and str(contador)[-1] != '7':
        lista.append(contador)
    contador += 1
print(lista)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

10.
R.
v1 = {2, 10, 55, 6, 7, 8, 9, 10, 11, 12}
v2 = {1, 20, 55, 20, 33, 77, 88, 5, 8, 9}
ambos = v1.intersection(v2)  # Separa os elementos iguais de dois vetores
print(ambos)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

11. https://i.imgur.com/d8fPC91.png
R.
lista = []

while len(lista) < 15:
    numero = int(input('Informe um numero: '))
    if numero in lista:
        print('Numero ja existente, informe outro.')
    else:
        lista.append(numero)
print(lista)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

12.
R.

v1 = [2, 10, 55, 6, 7, 8, 9, 10, 11, 12]
print(sorted(v1[:5]) + sorted(v1[5:], reverse=True))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

13.
R.

n = int(input('Informe um numero: \n'))
lista = [1, 2, 1]
ext = []
plista = []
contador = 0
for linha in range(1, n+1):
    for coluna in range(linha + 1):
        soma = lista[contador] + lista[contador+1]
        ext.append(soma)
        if coluna == linha:
            ext.insert(0, 1)
            ext.insert(len(ext), 1)

            # print na tela do triangulo pascal
            for n in ext:
                plista.append(str(n))
            print(' '.join(plista))
            plista.clear()

            lista.extend(ext)
            ext.clear()
            contador += 2
        else:
            contador += 1

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

14.
R.
n = int(input('Informe um numero: '))
matriz = []

for n1 in range(n):
    matriz.append([0] * n)
maior = 0
for l in range(n):
    for c in range(n):
        matriz[l][c] = int(input('Informe um numero para matriz: '))
        if matriz[l][c] > 10:
            maior += 1
for l in range(n):
    for c in range(n):
        print(f'{matriz[l][c]:^5}', end=' ')
    print()
print(f'Existem {maior} números maiores que 10 nessa matriz')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

15. Imprima a localização do maior numero na matriz
R.

n = int(input('Informe um numero: '))
matriz = []

for n1 in range(n):
    matriz.append([0] * n)
maior = 0
localizacao = 0


for l in range(n):
    for c in range(n):
        matriz[l][c] = int(input(f'{l}/{c}- Informe um numero para matriz: '))
        if maior < matriz[l][c]:
            maior = matriz[l][c]
            localizacao = l, c

for l in range(n):
    for c in range(n):
        print(f'{matriz[l][c]:^5}', end=' ')
    print()

print(localizacao)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

16.
R.

from random import randint

n = int(input('Informe o tamanho da matriz: '))
matriz = []
matriz1 = []
maiormatriz = []

for n1 in range(n):
    matriz.append([0] * n)
    matriz1.append([0] * n)
    maiormatriz.append([0] * n)

for l in range(n):
    for c in range(n):
        matriz[l][c] = randint(1, 500)
        matriz1[l][c] = randint(1, 500)

for l in range(n):
    for c in range(n):
        matriz[l].sort()
        matriz1[l].sort()

contador = 0
contador1 = 1
for l in range(n):
    for c in range(int(n/2), n):
        maiormatriz[l][contador] = matriz[l][c]
        maiormatriz[l][contador1] = matriz1[l][c]
        contador += 2
        contador1 += 2
        if contador == n or contador1 == n:
            contador = 0
            contador1 = 1

# PRINT =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
for l in range(n):
    for c in range(n):
        print(f'{matriz[l][c]:^5}', end=' ')
    print()
print()
for l in range(n):
    for c in range(n):
        print(f'{matriz1[l][c]:^5}', end=' ')
    print()
print()

for l in range(n):
    for c in range(n):
        print(f'{maiormatriz[l][c]:^5}', end=' ')
    print()
print()


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""
matriz = []

for l in range(3):
    vetor = []
    for c in range(3):
        valor = 0
        vetor.append(valor)
    matriz.append(vetor)

for l in range(3):
    for c in range(3):
        print(f'{matriz[l][c]:^5}', end='')
    print()

jogadas = 0
while jogadas < 9:
    print('Jogador 1, sua vez!')
    l1 = int(input('Informe a linha em que vai fazer a jogada: '))
    print(f'Linha {l1} selecionada')
    c1 = int(input('Informe a coluna em que vai fazer a jogada: '))
    print(f'Coluna {c1} selecionada')
    matriz[l1][c1] = -1
    print()
    print('Jogador 2, sua vez!')
    l2 = int(input('Informe a linha em que vai fazer a jogada: '))
    print(f'Linha {l2} selecionada')
    c2 = int(input('Informe a coluna em que vai fazer a jogada: '))
    print(f'Coluna {c2} selecionada')
    matriz[l2][c2] = 1

