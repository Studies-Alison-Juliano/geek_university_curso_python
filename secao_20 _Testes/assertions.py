"""
Assertions

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é valida ou não. Se a expressão for verdadeira o assert
retorna None e se é falsa levanta um erro do tipo AssertionError.

# OBS: Nós podemos especificar opcionalmente um segundo argumento ou mesmo uma mensagem de erro personalizada.
# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente nos
testes.

# ALERTA: Cuidado ao utilizar "assert"
Se um programa Python for executado com parâmetro -O, nenhum assertion será validado. Ou seja, todas suas validações
ja eram
"""
def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, "Ambos numeros precisam ser positivos"
    return a + b


ret = soma_numeros_positivos(-2, 4)  # AssertionError
ret1 = soma_numeros_positivos(2, 4)  # 6


def comer_fast_food(comida):
    assert comida in [
        "pizza",
        "sorvete",
        "doces",
        "batata frita",
        "cachorro-quente"
    ], "Comida precisa ser fast-food"
    return f"Eu estou comendo {comida}"


comida = input("Informe a comida: ")
print(comer_fast_food(comida))



