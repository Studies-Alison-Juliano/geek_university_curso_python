"""
Saindo de loops com break

Funciona da mesma form que nas linguagens c ou java.

Utilizamos o break para sair de loop de maneira projetada.

# exemplo 1

for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print('Fora do Loop!')

"""
# exemplo 2
while True:
    commando = input('Digite "sair" para parar: ')
    if commando == 'sair':
        break
