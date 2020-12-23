"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais
    - Variáveis globais sao reconhecidas, ou seja, se o escopo compreende todo o programa

2 - Variáveis locais
    - São reconhecidas apenas nos blocos onde foram declaradas, ou seja, seu escopo está limitado
    ao bloco onde foi declarada.

Para declarar variáveis em python, fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável nos não colocamos
o tipo de dado dela. Esse tipo é inferido ao atribuirmos o valor a mesma

Exemplo em java:
int numero = 42;
"""
numero = 41
print(numero)
print(type(numero))

if numero < 42:
    novo = numero + 10  # A variável 'novo' está declarada localmente dentro do bloco IF, por tanto é local
    print(novo)
