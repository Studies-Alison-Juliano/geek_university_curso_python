"""
Recebendo dados do usuário

Input() -> Todo dado recebido do via input é do tipo String

Em Python, String é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;
"""
# Entrada de dados [1]
# print('Qual seu nome ?') => forma antiga
nome = input('Qual seu nome ?')

# Saída de dados [1]
# print('Seja bem vindo(a) %s' % nome) => forma antiga
print(f'Seja bem vindo(a) {nome}')

# Entrada de dados [2]
idade = int(input('Qual sua idade ?'))

# Saída de dados [2]
print(f'O(a) {nome} tem {idade} anos')
print(f'O(a) {nome} nasceu em {2020 - idade}')

"""
Int(Idade) => Cast
 
Cast é a conversão de um tipo de dado para outro
"""
