"""
1. Peça para usuário 3 valores inteiros e imprima a soma deles

n1 = input('Informe um valor : ')
n2 = input('Informe um valor : ')
n3 = input('Informe um valor : ')
soma = int(n1)+int(n2)+int(n3)
print(soma)
"""
"""
2. Imprima o quadrado de um numero real

n1 = input('Informe um numero real : ')
soma = float(n1) ** 2
print(soma)
"""
"""
3. Leia um numero real e imprima a quinta parte deste numero

n1 = float(input('Informe um numero real : '))
resultado = n1 / 5
print('Quinta parte do numero informado é:', resultado)
"""
"""
4. Leia uma temperatura em graus celsius e apresente-a de forma convertida Fahrenheit. A formula de conversão é :
F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C em celsius

c = int(input('Qual a temperatura em C° ?\n'))
f = float(c*(9.0/5.0)+32.0)
print('Temperatura convertida em Fahrenheit é de :\n', f)
"""
"""
5. Leia uma letra maiúscula e a transforme em minúscula utilizando a tabela ASCII.

char = input('Informe uma letra maiúscula :')
minus = ord(char) + 32  # ord -> Mostra em formatado unicode ASCII o character inserido
mai = chr(minus)        # chr -> Transforma um unicode ASCII em um character
print(mai)
"""
seg = int(input('Informe os segundos :'))
totalmin = int(seg/60)
hra = int(totalmin/60)
minutos = totalmin % 60
segundos = seg % 60
print('Horas ', hra, ':', minutos, ':', segundos)
