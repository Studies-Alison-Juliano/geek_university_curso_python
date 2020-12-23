"""
Generators Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension.... Por que elas se chamam Generators

nomes = ['Leidy', 'Larga', 'Larissa', 'Lucas', 'Alison']

print(any([nome[0] == 'L' nome in nomes]))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Poderiamos ter feito utilizando Generators
nomes = ['Leidy', 'Larga', 'Larissa', 'Lucas', 'Alison']
print(any(nome[0] == 'L' for nome in nomes))

# Como list comprehension
res = [nome[0] == 'L' for nome in nomes]
print(type(res))
print(res)

# Generator (Preferível caso não vá usar os dados, pois não ocupa espaço em memória, apenas um object)
res = (nome[0] == 'L' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof() ? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(9265498485416))
print(getsizeof(True))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from sys import getsizeof
# Gerando uma lista de números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com generator comprehension
generator = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {generator} bytes')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Eu posso iterar no Generator Expression

gen = (x * 10 for x in range(1000))
print(gen)

for num in gen:
    print(num)
"""
from sys import getsizeof
# Gerando uma lista de números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com generator comprehension
generator = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {generator} bytes')
