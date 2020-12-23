"""
Funções com parâmetro padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional

# Exemplo de função onde a passagem de parâmetro seja opcional:
print('Geek University')
print()


# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2


print(quadrado(5))
print(quadrado())  # Type error

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def exponencial(numero=4, potencia=2):  # 4 e 2 são valores default
    return numero ** potencia


print(exponencial(3))  # Por padrão eleva ao quadrado
print(exponencial(3, 2))  # Numero elevado ao potencia(expoente) informado


# OBS: Se o usuário passar somente um argumento, este será atribuído ao parâmetro numero, e será calculado o quadrado
# deste numero;
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro numero e o segundo ao parâmetro potencia.
# Então será calculada a esta potencia

print(exponencial())
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 # OBS: Em funções Python, os parâmetros com valores default DEVEM sempre estar ao final da declaração

# ERRO!
def teste(num=2, potencia):
    return num ** potencia

print(teste(4))

# Outros exemplos

def soma(num1, num2):
    return num1 * num2


print(soma(4, 5))
print(soma(3))  # Type error
print(soma())   # Type error

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 # Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem Vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você fosse o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))  # True
print(mostra_informacao(nome='Estephany'))
print(mostra_informacao('Ozzy'))

# Caso a ordem não esteja igual aos parâmetros, o argumento deve informar a qual parâmetro o valor(qualquer tipo)recebe.

# Por que utilizar parâmetros com o valor default?

- Nos permite ser mais flexiveis nas funções:
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legiveis de código


# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funções, etc

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Escopo - Evitar problemas e confusões

# Variáveis Globais
# Variáveis Locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# Se tivermos uma variável local com o mesmo nome de uma variável global, a local tera preferência

def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Oi {prof}'


print(diz_oi())
print(prof)  # Name Error

# ATENÇÃO com variáveis globais. (Se poder evitar, evite!)
total = 0


def incrementa():
    total = total + 1  # UnboundLocalError (A variável local está sendo usada para processamento sem ter sido inicializada
    return total


print(incrementa())


# ATENÇÃO com variáveis globais. (Se poder evitar, evite!)
total = 0


def incrementa():
    global total  # Avisando que quermos utilizar a variável global
    total = total + 1  # UnboundLocalError (A variável local está sendo usada para processamento sem ter sido inicializada
    return total


print(incrementa())  # 1
print(incrementa())  # 2
print(incrementa())  # 3

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())  # 1
print(fora())  # 1
print(fora())  # 1



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""
# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())  # 1
print(fora())  # 1
print(fora())  # 1

