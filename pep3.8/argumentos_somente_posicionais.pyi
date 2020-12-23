"""
Argumentos Somente Posicionais
"""
# valor = "67.7"
# print(float(valor))

"""
def cumprimenta(nome):
    return f"Olá {nome}"


print(cumprimenta("Geek"))
print(cumprimenta(nome="Geek"))
"""
"""
def cumprimenta_v2(nome, /):
    return f"Olá {nome}"


print(cumprimenta_v2("Geek"))
print(cumprimenta_v2(nome="Geek"))

"""
"""
def cumprimenta_v3(nome, /, mensagem="Olá"):
    return f"{mensagem} {nome}"


print(cumprimenta_v3("Geek"))
print(cumprimenta_v3("University", mensagem="Helo"))
print(cumprimenta_v3("University", "Bem-Vinda"))
print(cumprimenta_v3("University", nome="Teste"))
"""
"""
def cumprimenta_v4(*, nome):
    return f"Olá {nome}"


print(cumprimenta_v4(nome="Alison"))
print(cumprimenta_v4("Alison"))
"""
def cumprimentar_v5(nome, /, mensagem="Olá", *, mensagem2):
    return f"{mensagem} {nome} {mensagem2}"


print(cumprimentar_v5("Geek", mensagem="Heelo", mensagem2="tenha um bom dia"))

