"""
Loop for

Loop -> Estrutura de repetição
For -> Uma das estruturas

Python

for item in inteirável:
    //execução do loop

Utilizamos loop para iterar sobre sequencia ou sobre valores iteráveis

Exemplo de iteráveis
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    números = range(1, 10)

///////////////////////////////////////////////////////////////////////////////////////////
# Exemplo de for 1 (Iterando uma string)

for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando uma lista)

    for numero in lista:
        print(numero)

# Exemplo de for 2 (Iterando um range)

    Range -> Valor inicial, valor final.

    OBS : Valor final não é inclusive.

        for numero in range(1, 10):
            print(numero)
///////////////////////////////////////////////////////////////////////////////////////////
enumerate :

 exemplo : (0, 'G'), (1, 'e'), (2, 'e'), (3, 'k')

for _, letra in enumerate(nome):
    print(letra)

OBS : Quando não precisamos de um valor utilizamos o underline (_)
///////////////////////////////////////////////////////////////////////////////////////////
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)
///////////////////////////////////////////////////////////////////////////////////////////

qtd = int(input('Quantas vezes esse loop deve rodar :'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} :'))
    soma += num
print(f'Soma dos números : {soma}')

///////////////////////////////////////////////////////////////////////////////////////////

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

 ///////////////////////////////////////////////////////////////////////////////////////////

    for n in range(1, 11):
        print(f'\U0001F602' * n)
"""
p = int(input('Informe um numero: '))
if p == 2:
    p += 1
pn = 0
i = 1
for n in range(2, p):
    i += 1
    if p % i == 0:
        pn += 1
    if i == (p - 1):
        if pn > 0:
            print('Não p')
        else:
            print('Primo')
