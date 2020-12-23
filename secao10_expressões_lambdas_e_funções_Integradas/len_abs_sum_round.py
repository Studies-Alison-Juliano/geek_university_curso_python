"""
Len, abs, sum, round

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável
print(len('Geek University'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# Por de baixo dos panos quando utilizamos a função len() o Python faz o seguinte:
# Dunder len
print('Geek University'.__len__())

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal/
# Exemplo Abs
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos,
incluindo o valor inicial

#OBS: o valor inicial default = 0

# Exemplos Sum
print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3, 4, 5], 5))  # 20

# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo da entrada

# Exemplos Round
print(round(10.2))  # 10
print(round(10.5))  # 10
print(round(10.6))  # 11
print(round(1.2121212121, 2))  # 1.21
print(round(1.219999999, 2))  # 1.22
"""


