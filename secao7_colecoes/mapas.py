"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

# Iterar sobre dicionário
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Acessando as chaves:

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
val = receita.values()
print(val)
print(type(val))

for valor in receita.values():
    print(valor, end=' ')

# Desempacotamento de dicionários
print(receita.items())

for chave, valor in receita.items():
    print(f'chaves={chave} e valor={valor}')
"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Soma*, Valor max*, valor min*, tamanho:
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


