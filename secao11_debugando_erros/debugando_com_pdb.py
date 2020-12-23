"""
Debugando com PDB

PDB - Python Debugger
Bug - Inseto
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# A utilização do print para debugar código é uma pratica ruim

def dividir(a, b):
    print(f'A = {a} B = {b}')
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


print(dividir(4, 7))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Existem formas profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# o PDB - Python Debugger

# Exemplo com PyCharm


def dividir(a, b):
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


print(dividir(4, 7))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Exemplo 2 com PDB - Python Debugger
# Para utilizar o Python Debugger precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# Comandos básicos do pdb:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime váriavel)
# c (continua a execução - finaliza o debugging)

import pdb
nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'Faz o curso' + curso
print(final)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Exemplo 3 com PDB - Python Debugger
# Para utilizar o Python Debugger precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# Comandos básicos do pdb:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime váriavel)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'Faz o curso' + curso
print(final)

# Por que utilizar este formado?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de biblioteca no inicio do arquivo
# Por isso ao inves de colocar o import do PDB no inicio do arquivo, nos colocamos somente onde vamos debugar.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Exemplo 3 com PDB - Python Debugger
# Para utilizar o Python Debugger precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# * A partir do Python 3.7 não é mais necessário importar a biblioteca PDB, pois o comando de debug foi incorporado como
# função built-in chamada breakpoint()

# Comandos básicos do pdb:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime váriavel)
# c (continua a execução - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'Faz o curso' + curso
print(final)

# Por que utilizar este formado?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de biblioteca no inicio do arquivo
# Por isso ao inves de colocar o import do PDB no inicio do arquivo, nos colocamos somente onde vamos debugar.
"""
# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))
# Como os nomes das variáveis são os mesmos do PDB, devemos utilizar o comando p para imprimir as variáveis, ou seja:
# p nome_da_variavel

# Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos
