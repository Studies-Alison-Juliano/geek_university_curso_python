"""
Dicionários

Obs: Em algumas linguagens de programação os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

OBS: Sobre dicionários:
    - Chave e valor são separados por dois pontos "chave:valor";
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos Comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Acessando elementos

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 1: Acessando via chave da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# Caso tentamos fazer um acesso utilizando uma chave que não existe, termos o erro: "key error"

# Forma 2: Acessando via get - Recomendado
print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado o "Key error"
pais = paises.get('py')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('ru', 'Não encontrado')

print(pais)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    paises = paises['ru']

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Podemos utilizar qualquer tipo de dado, inclusive lista, tupla, como chaves de dicionário

# Tuplas por exemplo, são bastante interessantes para serem usadas como chave de dicionário, pois as mesmas são imutável
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.7128, 40.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em Sao Paulo'
}

print(localidades)
print(type(localidades))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1: (Mais comum)
receita['abr'] = 350
print(receita)

# Forma 2:
novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# CONCLUSÃO 2: Em dicionários não podemos ter chaves repetidas

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS 1: Aqui SEMPRE precisamos informar a chave, e caso não encontre o elemento, um KEYERROR é retornado
# OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado

# Forma 2:
del receita['fev']
print(receita)
# Se a chave não existir será gerado um KEY ERROR
# OBS: Neste caso o valor removido não é retornado

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Imagine que você tem um comercio eletronico, onde temos um carrinho no qual você adiciona produtos.

Carrinho de compras:

Produto 1
    nome;
    quantidade;
    preço;
Produto 2
    nome;
    quantidade;
    preço;

# 1 - Poderiamos utilizar uma lista para isso? Sim!
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# 2 - Poderíamos utilizar tupla para isso? Sim!
produto1 = ('Playstation', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# 3 - Poderíamos utilizar dicionário para isso? Sim!
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Deste forma facilmente adicionamos ou removemos produtos no carrinho, e em cada produto podemos ter a certeza sobre
cada informação

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Métodos de dicionário

# Limpar o dicionário
d.clear()

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
# Copiando um dicionário para outro

# Forma 1 -  Deep Copy
novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

"""
# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método "fromkeys" recebe dois parâmetros, um iteravel e um valor, ele vai gerar para cada valor iteravel uma chave e
# ira atribuir a está chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
