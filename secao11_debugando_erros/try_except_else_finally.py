"""
Try, except, else e finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA:

OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> é executado somente se não ocorrer o erro
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Vc digitou {num}')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Finally
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor invalido')
else:
    print(f'Vc digitou {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado, independente se ouve exceção ou não

# O finally é geralmente utilizado para fechar ou desalocar recursos
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Exemplo mais complexo ERRADO


def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro numero: '))
try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('Valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Exemplo mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções


def dividir(a, b):
    try:
        return a / b
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possivel realizar uma divisão por 0'


num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

print(dividir(num1, num2))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Exemplo mais complexo - Genérico
# OBS: Você é responsável pelas entradas das suas funções


def dividir(a, b):
    try:
        return a / b
    except:
        return 'Ocorreu um problema'


num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

print(dividir(num1, num2))
"""
# Exemplo mais complexo - Genérico
# OBS: Você é responsável pelas entradas das suas funções


def dividir(a, b):
    try:
        return a / b
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

print(dividir(num1, num2))
