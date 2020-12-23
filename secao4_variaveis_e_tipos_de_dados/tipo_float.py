"""
Tipo float

Real decimal

Obs: O separador de casas decimais na programação é ponto e não virgula.
    valor = 1.44
    print(valor)
    print(type(valor))
"""
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44.6
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um valor float para inteiro
"""
Perdemos precisão ao transformar valores, pois eles são arredondados
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
