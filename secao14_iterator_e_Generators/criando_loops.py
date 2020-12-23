"""
Criando sua própria versão de loop

for n in [1, 2, 3, 4, 5]:
    print(n)

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])
iter('Geek University')
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)
