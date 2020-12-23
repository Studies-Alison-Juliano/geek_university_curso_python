"""
Modulo Collections - Deque

Podemos dizer que deque é uma lista de alta performance.


"""
# Import
from collections import deque
deq = deque('geek')
print(deq)

# Adicionando elementos no deque
deq.append('y')  # Adiciona no final
print(deq)

deq.appendleft('k')
print(deq)  # Adiciona no começo da lista

# Remover elementos
print(deq.pop())  # Remove e retorna o ultimo elemento
print(deq.popleft())  # Remove e retorna o primeiro elemento
