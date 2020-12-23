"""
Nasted List (listas aninhadas)

- Algumas linguagens de programação possuem estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as listas

numeros = [1, 'b', 3.313, True, 5]

# Exemplo
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)
print(type(list))

# Como fazemos para acessar os dados
print(listas[0][1])  # 2
print(listas[2][1])  # 8

# Iterando com loops em uma lista aninhada
for l in listas:
    print(l)
    for n in l:
        print(n)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

"""
# Outros exemplos
# Gerando um tabuleiro/matriz 3 x 3
tabuleiro = [[valor_coluna for valor_coluna in range(1, 4)] for linha in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para jogo da velha
velha = [['X' if valor_coluna % 2 == 0 else '0' for valor_coluna in range(1, 4)] for linha in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
