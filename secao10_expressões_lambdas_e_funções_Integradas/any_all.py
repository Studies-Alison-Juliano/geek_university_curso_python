"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False! o valor 0 é False
print(all([]))  # Todos os números são verdadeiros? True! Um iterável vazio é True usando a função all()
print(all('Geek'))  # Todos os números são verdadeiros? True!

nomes = ['Leidy', 'Larla', 'Larissa', 'Lucas']
print(all(nome[0] == 'L' for nome in nomes))  # True

print(all([letra for letra in 'eio' if letra in 'aeiou']))  # True

print(all([num for num in [4, 2, 10, 6, 8, 0] if num % 2 == 0]))  # Retorna um False pois existe um 0 no iterável
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

print(any([0, False, {}, [], 4]))  # True!
print(any([0, False, {}, [], ()]))  # False!

nomes = ['Leidy', 'Larla', 'Larissa', 'Lucas', 'Alison']
print(any([nome[0] == 'L' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 0] if num % 2 == 0]))  # True

"""
print(any([num for num in [4, 2, 10, 6, 8, 0] if num % 2 == 0]))
