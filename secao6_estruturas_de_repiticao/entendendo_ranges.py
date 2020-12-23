"""
Ranges

-Precisamos conhecer o loop for para usar os ranges
-Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória mas sim de maneira especificada.

Formas gerais :

# forma 1
range(valor_de_parada)

OBS : valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)
# exemplo:
for num in range(11):
    print(num)

# forma 2:
range(valor_de_inicio, valor_de_parada)

OBS : valor_de_parada não inclusive (inicio especificado, e passo de 1 em 1)
# exemplo:
for num in range(1, 11):
    print(num)

# forma 3:
range(valor_de_inicio, valor_de_parada, passo)

OBS : valor_de_parada não inclusive (inicio especificado, e passo especificado pelo usuário)
# exemplo:
for num in range(1, 11, 2):
    print(num)

# forma 4 (inversa):
range(valor_de_inicio, valor_de_parada, passo)

OBS : valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo especificado pelo usuário)
#exemplo
for num in range(10, -1, -1):
    print(num)
"""
