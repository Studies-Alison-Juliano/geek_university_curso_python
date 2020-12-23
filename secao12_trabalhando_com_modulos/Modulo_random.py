"""
Modulo random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos em Python

Módulo Random -> Possui varias funções para geração de números pseudo-aleatórios.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# OBS: Existem duas formas de se utilizar um módulo deste
# Forma 1 - Importando todo o módulo (Não recomendado).

import random

# random() Gera um número real pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do
# módulo ficarão disponíveis(Ficarão em memória). Caso você saiba quais funções você precisa utilizar deste módulo,
# então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na forma 2

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função separadas
# por ponto

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas uma
# função dentro do módulo random
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Forma 2 - Importando uma função especifica do módulo

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# uniform() -> Gerar um numero real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# randint() -> Gera valores inteiros pseudo-aleatórios entre valores estabelecidos.
from random import randint

# Gerador de aposta para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

from random import choice
print(choice('Geek University'))
"""
# shuffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']
print(cartas)
shuffle(cartas)
print(cartas)
print(cartas.pop())
