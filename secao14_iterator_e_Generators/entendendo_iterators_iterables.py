"""
Entendendo Iterators e Iterables

Iterator ->
        - Um objeto que pode ser iterado.
        - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterable ->
        - Um objeto que irá retornar um iterator e função iter() for chamada.


"""
nome = 'Geek'  # É um iterable mas não é um iterator
numeros = [1, 2, 3, 4]  # É um iterable mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))  # G
print(next(it1))  # e
print(next(it1))  # e
print(next(it1))  # k

print(next(it2))  # 1
print(next(it2))  # 2
print(next(it2))  # 3
print(next(it2))  # 4
