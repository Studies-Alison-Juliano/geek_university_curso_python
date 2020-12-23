"""
Funções com retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop {ret_pop}')

ret_pr = print(numeros)
print(f'Retorno de print {ret_pr}')

OBS: Em Python quando uma função não retorna nenhum valor, o retorno é none

OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada "return"

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução
para outras funções ou mesmo para o print

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Vamos refatorar esta função para que ela retorno o valor


def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')
print(f'Retorno {quadrado_de_7()}')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Refatorando a primeira função


def diz_oi():
    return 'Oi '


alguem = 'Pedro!'
print(diz_oi() + alguem)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

OBS: Sobre a palavra reservada return:

1 - Ela finaliza a função, ou seja, ela sai da execução da função;

# Exemplo 1


def diz_oi():
    print(f'Estou sendo executado antes um retorno...')
    return 'Oi '
    print(f'Estou sendo executado apos um retorno...')


print(diz_oi())

                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
2 - Podemos ter em uma função diferentes returns;

# Exemplo 2


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores

# Exemplo 3


def outra_funcao():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_funcao()
# print(num1, num2, num3, num4)
print(outra_funcao())
print(type(outra_funcao()))
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Vamos criar uma função para jogar uma moeda

from random import random


def joga_moeda():
    # Gera um numero pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'cara'
    return 'coroa'


print(joga_moeda())

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""
#

