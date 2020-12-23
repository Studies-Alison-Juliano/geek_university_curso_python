"""
1. Faça um algoritmo que determine e mostre os cinco primeiros multiples de três
R.
for num in range(1, 16):            for num in list(range(1, 6)):
    mult = num % 3                      num *= 3
    if mult == 0:                       print(num)
        print(num)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
2. Faça um programa que peça ao usuário digitar 10 numeros e os some:
R.
soma = 0
for num in range(1, 11):
    num = int(input(f'{num}/10. Digite um numero :'))
    soma = soma+num
print(f'Soma de todos :{soma}')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
3. Escreva um programa que leia 10 numeros e informe o maior e menor valor dentre eles
R.
lista = []

for num in range(1, 11):
    lista.append(int(input(f'{num} Informe um numero : ')))
print(f'O maior numero é o : {max(lista)} e o menor é o : {min(lista)}')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
4.Faça um programa que leia um numero inteiro N depois imprima os N primeiros números impares naturais
R.
n = int(input('Informe um Numero : '))
qtd = n * 3
for n in range(n, qtd):
    impar = n % 2
    if impar != 0:
        print(n)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
5.Faça um programa que leia e some os 50 primeiros numero pares

soma = 0
for n in range(0, 50):
    par = n % 2
    if par == 0:
        soma += n
print(soma)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
6.Faça um programa que leia um numero natural e imprima em ordem decrescente os pares

n = int(input('Informe um numero natural: \n'))
par = n % 2
if par == 0:
    while n > 0:
        n -= 2
        print(n)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
7.Escreva um algoritmo que leia N números e imprima o maior deles e quantas vezes ele aparece. A quantidade de números
deve ser fornecida pelo usuário.

lista = []
quantidade = int(input('Informe quantos valores vai inserir: \n'))
for n in range(quantidade):
    lista.append(int(input(f'{n}. Informe um valor :')))
print(f'O maior numero é {max(lista)} e ele aparece {lista.count(max(lista))}')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
8.Escreva um algoritmo que leia um numero inteiro dentre 100 a 999 e imprima em seguida cada algorítimo que compõe o
número.

n = input('Informe um valor dentre 100 e 999: \n')
if 100 < int(n) < 999:
    for _, n in enumerate(n):
        print(n)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
9. Ler um sequencia de números inteiro e determinar se eles são pares ou não. Devera ser informado o número de dados
lidos e o número de valores pares. O processo termina quanto o número digitado for o 1000.

lista = []
listapar = []
n = 0
while n != 1000:
    lista.append(int(input('Informe um valor ou digite 1.000 para finalizar: \n ')))
    conta = lista.count(1000)
    if conta >= 1:
        break
for n in lista:
    par = n % 2
    if par == 0:
        listapar.append(n)
print(f'Existem {len(lista)-1} valores e dentre estes {len(listapar)-1} são pares')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
10. Faça um programa que receba dois números. Calcule e mostre:
.A soma dos números pares desse intervalo de números, incluindo os digitados
.A multiplicação dos números impares desse intervalo, incluindo os digitados

lista = []
soma = 0
multi = 1
for n in range(1, 2+1):
    lista.append(int(input(f'{n}/2. Informe dois números distintos:\n')))
for np in range(min(lista), max(lista)+1, 1):
    par = np % 2
    if par == 0:
        soma += np
    elif par != 0:
        multi *= np
print(f'Soma dos números pares é de {soma} e a Multi dos impares é : {multi}')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
11. Faça o calculo da fração:

dem = 0
soma = 0
for n in range(1, 99+1, 2):
    dem += 1
    div = n / dem
    soma += div
print(soma)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
12. Faça um programa que simule o lançamento de dois dados, d1 e d2, n vezes, e tenha como saída o resultado de cada
dado e a relação entre eles (>,<,=) de cada lançamento:

from random import randint
nmr = int(input('Informe quantas vezes você deseja jogar cada dado: \n'))
for n in range(0, nmr-1):
    d1 = randint(0, 6)
    d2 = randint(0, 6)
    if d1 > d2:
        print(f'D1 = {d1} é maior que D2 = {d2}')
    else:
        print(f'D2 = {d2} maior que D1 = {d1}')
    if d1 == d2:
        print(f'D1 = {d1} e D2 = {d2} Dados com valores iguais')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
13. Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros
naturais q são múltiplos de i ou de j ou de ambos

nmr = int(input('Quantos números impressos deseja ? \n'))
i = int(input('Informe o valor de I: \n'))
j = int(input('Informe o valor de J: \n'))
count = 0
qtd = nmr * 2
for n in range(0, qtd):
    if n % i == 0 or n % j == 0:
        count += 1
        if count <= nmr:
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
14.Faça um programa que calcule o menor numero divisivel entre 1 a 20

i = 1
count = 0
while count < 20:
    count += 1
    if i % count != 0:
        i += 1
        count = 1
        print(i)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
15.Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o valor
inicial e o valor final deste intervalo e o programa deve somar todos os valores impares

n1 = int(input('Informe um valor inicial :(Deve ser maior que o final) \n'))
n2 = int(input('Informe um valor final : (Deve ser menor que o inicial) \n'))
soma = 0
if n1 < n2:
    for n in range(n1, n2):
        imp = n % 2
        if imp != 0:
            soma += n
    print(soma)
else:
    print('Numero invalido!')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
16.Escreva um programa que verifique entre 1000 e 9999, quais números possuem a seguinte propriedade: A soma dos dois
primeiros character e os dois últimos elevados ao quadrado é igual ao próprio valor.

for n in range(1000, 9999+1):
    s = str(n)
    p1 = s[0:2]
    p2 = s[2:4]
    conta = (int(p1) + int(p2))**2
    if conta == n:
        print(n)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
17.Leia um número positivo do usuário, então, calcule e imprima a sequencia Fibonacci até o primeiro número superior
lido.

ni = int(input('Informe um valor positivo: '))
prox = 0
ant = 0
for n in range(0, ni):
    print(prox)
    prox += ant
    ant = prox - ant
    if prox == 0:
        prox += 1
    if n > ni:
        break
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
18.Faça um programa que converta Km/h para M/s vice-versa. O programa terá que ter as duas opções e enquanto o programa
não for encerrado deverá se repetir

loo = False
while not loo:
    n = input('Digite Km se deseja transformar Km/h em M/s ou Ms vice versa: ')
    if n.title() == 'Km':
        km = int(input('Informe quantos Km/h: '))
        kmm = km / 3.6
        print(f'"{km}Km/h" equivalem a "{round(kmm, 1)}"Ms/h')
    elif n.title() == 'Ms':
        ms = int(input('Informe quantos M/s'))
        mss = ms * 3.6
        print(f'"{ms}M/s" equivalem a "{mss}"Km/h')
    elif n == 'ex':
        break
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
19.Faça um programa de chutes. Gere um número randómico e faça com que o usuário chute até acertar(De dicas se está
próximo ao valor, "maior" ou "menor"

from random import randint
n = randint(1, 1000)
print(n)
s = int(input('1. Chute um número e tente acertar: '))
t = 2
if s > n:
    print('Menor')
else:
    print('Maior')
while s != n:
    s = int(input(f'{t}. Chute um número e tente acertar: '))
    if s > n:
        print('Menor')
    else:
        print('Maior')
    if s == n:
        print(f'Acertou o porra... DEPOIS DE {t} TENTATIVAS... PQP EM')
        break
    t += 1
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
20. Chico tem 1.50 de altura e Ze tem 1.10, a cada ano que passa Chico cresce 2 CM e Ze 3 CM. Escreva um programa que
diga quantos anos será necessário para Ze chegar na altura de Chico.

c = 1.50
z = 1.10
cz = 0
zc = 0
while cz <= 100 or zc <= 99:
    cz += 2
    zc += 3
    dc = cz / 100
    dz = zc / 100
    cf = c + dc
    zf = z + dz
    if zf == cf:
        zc /= 3
        print(f'Z precisara de {round(zc)} anos par ter a mesma altura q C')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
21. Imprima um triangulo de froyd:

l = int(input('Informe um número: '))
i = 1
for n in range(1, l+1):
    for c in range(1, n+1):
        print(f'{i} ', end='')
        i += 1
    print()
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
22. Faça um programa que identifique se o numero é primo ou não:

p = int(input('Informe um numero: '))
if p == 2:
    p += 1
pn = 0
pc = 0
i = 1
for n in range(2, p):
    i += 1
    if p % i == 0:
        pn += 1
    else:
        pc += 1
    if i == (p - 1):
        if pn > 0:
            print('Não p')
        else:
            print('Primo')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
23.Faça um programa que conte quantos números primos existem entre a e b

p1 = int(input('Informe um numero: '))
p2 = int(input('Informe um outro numero: '))
pn = 0
pri = 0
for c in range(p1, p2+1):
    for n in range(2, c):
        if c % n == 0:
            pn += 1
        if n == (c - 1):
            if pn == 0:
                pri += 1
            pn = 0
print(f'Existem {pri+1} números primos entre {p1} e {p2}')
"""
