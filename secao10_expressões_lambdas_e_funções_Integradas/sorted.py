"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que ja estamos em listas. O sort() só funciona em listas

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar

OBS: O sorted(), SEMPRE retorna uma LISTA com os elementos do iterável ordenados
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Exemplo
numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros))  # Ordenar do menor para o maior
print(numeros)

numeros = [6, 1, 8, 2]
print(set(sorted(numeros)))
# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'username': 'samue', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Amo meu gato']},
    {'username': 'jeff1', 'tweets': []},
    {'username': 'bob12', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'doggo', 'tweets': ['Gosto de cachorro', 'Vou sair hoje']},
    {'username': 'gall1', 'tweets': [], 'cor': 'preto', 'musica': 'rock'}
]

print(usuarios)
# Ordenando pelo tweets
print(sorted(usuarios, key=lambda tweet: tweet.get('tweets')))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda numero_tweet: len(numero_tweet['tweets'])))
"""
# Ultimo exemplo

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock, to yong to die', 'tocou': 32}
]

# Ordena da menos tocada para mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Ordena da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
