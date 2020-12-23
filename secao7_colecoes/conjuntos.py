"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a "teoria dos conjuntos" da matemática

- Aqui no Python os conjuntos são chamados de Sets.

Dito isso, da mesma forma que da matemática:

- Sets (conjuntos) não possuem valores duplicados
- Sets (conjuntos) não possuem valores ordenados
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados:

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles
quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os Sets (conjuntos) são referenciados em Python com chaves {}

Diferença entre conjuntos (sets) e mapas (dicionários)
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Definindo um conjunto

# Forma 1:
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare aqui que temos valores repetidos
print(s)
print(type(s))
# Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo será ignorado sem gerar erros e não fara
# parte do conjunto

# Forma 2: (Mais comum)
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Importante lembrar que, alem de não termos valores duplicados, não temos ordem
dados = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]

lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Assim como todo outro conjuntos Python podemos colocar todos os tipos de dados misturados em sets
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Uso interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes, em uma feira ou museu e os visitantes informam
# manualmente a cidade de onde vieram.

# Nos adicionamos cada cidade em uma lista Python, ja que em uma lista podemos adicionar novos elementos e ter repetição
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(f'{len(cidades)} cidades foram cadastradas')

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# O que você faria ? Faria um loop na lista... ?
# Podemos utilizar o set para isso:
print(f'{len(set(cidades))} cidades distintas')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não adicionado
print(s)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1:
s.remove(3)  # Não é índice! Informamos o valor a ser removido
print(s)
# OBS: Caso o valor não seja encontrado será gerado o erro "KeyError"

# Forma 2:
s.discard(2)
print(s)
# OBS: Se o valor não for encontrado, nenhum erro é gerado

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Copiando um conjunto para outro:
s = {1, 2, 3}
print(s)

# Forma 1: (Deep Copy)
novo = s.copy()
print(novo)

s.add(4)

print(s)
print(novo)

# Forma 2: Shallow Copy
novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Métodos matemáticos de conjunto

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudando do curso de Java
estudantes_python = {'Marcos', 'Patricia', 'Elen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjuntos com nomes de estudantes únicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos = estudantes_python.intersection(estudantes_java)
print(ambos)

# Forma 2 utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""

