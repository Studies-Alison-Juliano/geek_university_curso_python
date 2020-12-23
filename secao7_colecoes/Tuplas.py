"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma
nova tupla

# CUIDADO 1 - As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2 - Tuplas com 1 elemento
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

# Conclusão: Podemos concluir que tuplas são definidas pela virgula e não pelos parênteses

(4) -> Não é tupla
(4,)-> É tupla
4,  -> É tupla

# Podemos gerar uma tupla dinâmica com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)
tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2  # Tupla são imutáveis mas podemos subscrever seus valores
print(tupla3)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Verificar se determinado elemento está contido na tupla
tupla = (1, 2, 3)

print(3 in tupla)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for i, n in enumerate(tupla):
    print(i, n)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Contando elementos em uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'd')

print(tupla.count('c'))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar dados contidos em uma coleção

# Exemplo 1:
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Mario', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso a elementos de uma tupla é semelhante a de uma lista
print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual índice um elemento está na tupla
print(meses.index('Junho'))

# Caso elemento não existe, será gerado erro
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Por que utilizar tuplas:

# - Tuplas são mais rápidas do que lista
# - Tuplas deixam seu código mais seguro

# Na tupla não temos o probleme de shallow copy
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
t = [('q', 1.0), ('w', 2.0), ('e', 3.0), ('r', 4.0), ('t', 5.0), ('y', 6.0), ('u', 7.0), ('i', 8.0), ('o', 10.0), ('a', 11.0)]
es = []
for n in t:
    es.append(n[1])
print(es)
print(es.index(max(es)))
