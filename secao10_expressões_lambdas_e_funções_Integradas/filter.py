"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')
# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))
print(f'Novamente: {list(res)}')
# OBS: Assim como na função map(), após ser utilizados os dados de filter(), eles são excluidos da memória
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
paises = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
print(list(res))

paises = ['', 'Argentina', '', 'Brazil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# A diferença entre map() e filter():

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do
iterável

# filter() - Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de
acordo com a função

Ou seja, filter() apenas retorna valores true ou false conforme a função e map() devolve todos os valores
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Exemplos mais complexos
usuarios = [
    {'username': 'samue', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff1', 'tweets': []},
    {'username': 'bob12', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorro', 'Vou sair hoje']},
    {'username': 'gall1', 'tweets': []}
]

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
"""
# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria', 'Lia']
# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
