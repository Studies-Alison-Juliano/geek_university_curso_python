"""
Decoradores com diferentes assinaturas



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar  # "saudacao" entra como argumento na def gritar. O parâmetro "arg1" entra como argumento na def aumentar
def saudacao(arg1):
    return f'Ola, eu sou o {arg1}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}'


# Testando
print(saudacao('Angelina'))
print(ordenar("Picanha", "Batata Frita"))  # TypeError, pois estamos passando 2 argumentos e a def aumentar apenas tem 1 parâmetro

# Para resolver utilizamos um padrão de projeto chamado Decorator Pattern
A assinatura de uma função é representada pelo seu retorno, nome e parâmetro de entrada.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Refatorando com a Decorator Pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(arg1):
    return f'Olá, eu sou o/a {arg1}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento} por favor'


print(saudacao("Felicity"))
print(ordenar("Picanha", "Batata Frita"))


@gritar
def lol():
    return 'lol'


print(lol())
# OBS: Vale lembrar que podemos utilizar parâmetros nomeados
print(ordenar(acompanhamento="Batata Frita", principal="Picanha"))  # Nomeando e direcionando argumentos
"""
# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('Pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10, 12))  # 22
print(soma_dez(1, 12))  # Valor incorreto! Primeiro argumento precisa ser 10

print(comida_favorita("Pizza", "Churrasco"))
print(comida_favorita("sanduiche", "Churrasco"))  # Valor incorreto! Primeiro argumento precisa ser Pizza
