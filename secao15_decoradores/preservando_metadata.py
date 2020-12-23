"""
Preservando metadata com wraps

Metadatas -> São dados intrísecos em arquivos
wraps -> São funções que envolvem elementos com diversas finalidades.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        ""Eu sou uma função dentro de outra""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar()


@ver_log
def soma(a, b):
    ""Soma dois numeros""
    return a + b


# print(soma(10, 30))
print(soma.__name__)  # logar
print(soma.__doc__)  # Eu sou uma função dentro de outra
"""
# Resolução do Problema
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar()


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


# print(soma(10, 30))
print(soma.__name__)  # logar
print(soma.__doc__)  # Eu sou uma função dentro de outra
