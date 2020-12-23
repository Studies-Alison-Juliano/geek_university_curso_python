"""
Tipo booleano

Algebra booleana criada por George Boole
 2 Constantes, verdadeira ou falsa:
 True -> Verdadeira
 False -> Falso

 OBS: Sempre com a inicial maiúscula
"""
ativo = False
print(ativo)


"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação se o valor booleano for verdadeiro o resultado será falso.
Se for falso o resultado será verdadeiro
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binaria ou seja, depende de dois valores ou um ou outro devem ser verdadeiro:
 True or True = True
 True or False = True
 False or True = True
 False or False = False
"""
print(ativo or logado)

# E (and)
"""
Também é uma operação binaria, ou seja, depende de dois valores, ambos os valores devem ser verdadeiros
 True and True = True
 True and False = False
 False and True = False
 False and False = False
"""
