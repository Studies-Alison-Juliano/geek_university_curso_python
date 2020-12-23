"""
Tipo String

Em Python, um dado é considerado String sempre que:

-Estiver entre aspas simples => 'uma string', '234', 'a', 'True', '43.3'
-Estiver entre aspas duplas => "
-Estiver entre aspas simples triples => '''
-Estiver entre aspas duplas triplas =>

nome = 'Angelina \nJolie'   # \n no caso está pulando uma linha
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"   # '\' character de escape
print(nome)
print(type(nome))

nome = "Angelina Jolie"
print(nome)
print(nome.split())  # Transforma em uma lista de strings

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13 ]
# ['A', 'n', 'g', 'e', 'l', 'i', 'n', 'a', ' ', 'J', 'o', 'l', 'i', 'e']
nome = "Angelina Jolie"
print(nome[0:8])  # Slice de string

# [    0    ,    1    ]
# ['Angelina', 'Jolie']
print(nome.split()[0])
"""

nome = 'Angelina Jolie'
"""
::-1 -> comece do primeiro elemento, vá ate o ultimo elemento e inverta
"""
print(nome[::-1])  # Inverssão da string
