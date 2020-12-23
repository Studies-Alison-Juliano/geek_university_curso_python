"""
Modulo Collection - Counter

https://docs.python.org/3/library/collections.html#collections.Counter

Collection -> High-Performance Container DateType

Counter -> Recebe um iteravel como parâmetro e cria um objeto do tipo collection counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrência desse
elemento.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Realizando o import Counter
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui utilizamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o counter
res = Counter(lista)
print(res)
print(type(res))

# ({1: 5, 3: 5, 5: 5, 2: 4, 4: 2, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2

print(Counter('Geek University'))
# ({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3
texto = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
make a type specimen book.'''

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))

"""
# Realizando o import Counter
from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34, 'faca']
print(Counter(lista))
