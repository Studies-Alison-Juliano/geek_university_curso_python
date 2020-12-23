"""
Geradores

Geradores (Generator) são iterators

OBS: O contrario não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com expressões geradoras;

Diferenças entre funções e Generator Functions

------------------------------------------------------------------------------
| Funções                            | Generator Funcions                     |
------------------------------------------------------------------------------
| utilizam return                    | utilizam yield                         |
| retorna uma vez                    | podem utilizar yield múltiplas vezes   |
| quando executada, retorna um valor | quanto executada retorna um generator  |
------------------------------------------------------------------------------
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Exemplo de Generator Function


def conta_ate(valormaximo):
    contador = 1
    while contador <= valormaximo:
        yield contador
        contador = contador + 1
# OBS: Uma Generator Function não é um Generator. Ela gera um generator


gen = conta_ate(5)
# print(type(gen)) -> Generator
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)
for num in gen:
    print(num)

print(next(gen))
print('For: ')
for num in gen:
    print(num)

"""
# Exemplo de Generator Function


def conta_ate(valormaximo):
    contador = 1
    while contador <= valormaximo:
        yield contador
        contador = contador + 1
# OBS: Uma Generator Function não é um Generator. Ela gera um generator


gen = list(conta_ate(10))
print(gen)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
