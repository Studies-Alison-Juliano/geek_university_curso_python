"""
O operador Walrus permite fazer a atribuição e o retorno de valor em uma única expressão

variável := expressão
"""
"""
nome = "Geek University"
print(nome)

print(nome := "Geek University")
"""
"""
# Python 3.7
cesta = []
fruta = input("Informe a fruta: ").title()
while fruta != "Jaca":
    cesta.append(cesta)
    fruta = input("Informe a fruta: ")
"""
# Python 3.8
cesta = []
while fruta := input("Informe a fruta").title() != "Jaca":
    cesta.append(fruta)
