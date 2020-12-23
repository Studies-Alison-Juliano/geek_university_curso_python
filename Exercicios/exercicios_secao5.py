"""
1 . Informe dois números e diga qual é maior

n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))

if n1 > n2:
    print('O primeiro numero é maior que o segundo')
else:
    print('O segundo numero é maior meu parceiro')
"""
"""
2 . Informe um numero, se for positivo faça raiz quadrada se não informe que é negativo

n1 = int(input('Informe um numero: '))

if n1 < 0:
    print('Numero é negativo')
else:
    raiz = float(n1) ** 0.5
    print(f'Raiz quadrada do numero inserido é : {raiz}\n')
"""
"""
3 . Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior do que 20% do
salário imprima : Empréstimo reprovado! caso contrario aprovado

salario = float(input('Informe um numero :'))
emprestimo = float(input('Informe um numero :'))

if salario * .2 < emprestimo:
    print(f'Empréstimo reprovado! O empréstimo requerido é {(emprestimo / salario) * 100}% maior de que seu salário')
else:
    print(f'Empréstimo aprovado! O empréstimo requerido significa somente {(emprestimo / salario) * 100}% de seu salário')
"""
"""
4 . Leia a altura e o sexo da pessoa e imprima qual deve ser seu peso ideal:

sexo = input('Olá! Poderia me informar seu sexo ? (Responda com "Fem" para feminino e "Masc" para masculino) : \n')
altura = float(input('Poderia me informar sua altura ? \n'))

if sexo.title() == 'Masc':
    print(f'Seu peso ideal para uma vida saudável deve ser de : {round((72.7*altura) - 58, 2)}\n')
elif sexo.title() == 'Fem':
    print(f'Seu peso ideal para uma vida saudável deve ser de : {round((62.1*altura) - 44.7, 2)}\n')
"""
"""
5 . Leia um numero e some todos os seus algoritmos :

num = (input("digite um número"))
if int(num) < 0:
    print("num invalido")
else:
    num = list(map(int, num))
    print(sum(num))
"""
"""
5 . Faça um programa q leia horas de chegada de um veiculo, horas de saída e calcule quanto o motorista deve pagar
seguindo uma tabela de preços

chegada = input('Informe o horário em que veículo chegou (Hora + Min) : \n')
saida = input('Informe a hora em que o veículo deixou o local (Hora + Min) : \n')
hra = int(chegada[0:2])
min = int(chegada[3:5])
hras = int(saida[0:2])  # Horas saída
mins = int(saida[3:5])  # Min saída

hraf = 0
minf = min + mins
sobra = 0
if hra < hras:
    hraf = hras - hra
elif hras < hra:
    hraf = hra - hras

minhra = 0
if minf >= 60:
    minhra = minf / 60
    sobra = minf % 60
    minf += sobra

resultado = hraf + minhra
if resultado < 2 or resultado == 2 and minf <= 0:
    taxa = 1.0
elif resultado == 2 and minf > 0:
    taxa = 1.40

elif resultado < 3 or resultado == 4 and minf <= 0:
    taxa = 1.40
elif resultado == 4 and minf > 0:
    taxa = 2.0

elif resultado >= 5:
    taxa = 2.0

print(f'Você passou {resultado} horas e {minf} minutos fora, portanto deve pagar R${taxa}')
"""

