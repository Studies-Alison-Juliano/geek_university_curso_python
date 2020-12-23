"""
Estrutura logica : And, or, not, is

Operadores unário:
    not
Operadores binário:
    and, or, is

if ativo or logado:
    print('Bem vindo(a) usuário!')
else:
    print('Você precisa ativar sua conta. Pf verifique seu email')

Regras de funcionamento:
Para o "and" ambos valores precisam ser True
Para o "or" um ou outro precisa ser True
Para o "not" o valor bollean é invertido, ou seja, se for true vira false vice-versa
Para o "is" o valor é comparado com o segundo

ex

n1 = float(input('Informe um numero :'))
n2 = float(input('Informe um numero :'))
media = (n1 + n2) / 2

if n1 > 10 or n2 > 10:
    print('Informação invalida! Nota do aluno precisa ser dentre 0 e 10')
elif n1 < 0 or n2 < 0:
    print('Informação invalida! Nota do aluno precisa ser dentre 0 e 10')
else:
    print(f'Media do aluno é de : {float(media)}')
"""
ativo = True
logado = True

if not ativo:
    print('Você precisa ativar sua conta')
else:
    print('Bem vinda usuária')
