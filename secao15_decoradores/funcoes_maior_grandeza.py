"""
Funções de maior grandeza - Higher order functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis do tipo
de funções nos nossos programas.

OBS: Na seção de funções nós utilizamos isso.

Em Python, as funções são Cidadões de primeira classe, first class citizen
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Exemplos - Definindo as funções


def soma(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções
print(calcular(4, 3, soma))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Nasted Functions - Funções aninhadas

# Em Python podemos também ter funções dentro de funções, que são conhecidas como Nasted Functions ou também Inner Func

# Exemplo
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai', 'Suma daqui', 'Gosto muito de você'))
    return humor() + pessoa


# Teste
print(cumprimento('Angelina'))
print(cumprimento('Felicity'))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Retornando funções de outras funções
from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahahha', 'kkkkkkkkkk', 'jajajajajajaja'))
    return rir


# Testando
rindo = faz_me_rir()
print(rindo)

"""
# Inner Functions (Funções Internas / Nasted Functions) podem acessar o escopo de funções mais externas.
from random import choice


def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice(('hahahahahahha', 'kkkkkkkkkkkk', 'jajajajajajaja'))
        return f'{risada} {pessoa}'
    return dando_risada


# Testando
rindo = faz_me_rir('Fernanda')
print(rindo())
print(rindo())
print(rindo())
