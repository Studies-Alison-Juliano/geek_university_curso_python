"""
Métodos de data e hora

# Com o now() podemos especificar um timezone
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))
"""
import datetime

"""
# Mudanças ocorrendo à meia-noite combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))
"""
"""
# Encontrar dia da semana. weekday()
# Os dias da semana do método weekday() começam em zero, sendo essa a segunda feira
# 0 - segunda-feira (Monday)
# 1 - terça-feira (Tuesday)
# 2 - quarta-feira (Wednesday)
# 3 - quinta-feira (Thursday)
# 4 - sexta-feira (Friday)
# 5 - sabado (Saturday)
# 6 - domingo (Sunday)
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())
"""
"""
aniversario = input("Qual sua data de nascimento: dd/mm/yy")
aniversario = aniversario.split("/")
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
if aniversario.weekday() == 0:
    print("Você nasceu em uma segunda-feira")
elif aniversario.weekday() == 1:
    print("Vc nasceu em uma terça feira")
elif aniversario.weekday() == 2:
    print("Vc nasceu em uma quarta feira")
elif aniversario.weekday() == 3:
    print("Vc nasceu em uma quinta feira")
elif aniversario.weekday() == 4:
    print("Vc nasceu em uma sexta feira")
elif aniversario.weekday() == 5:
    print("Vc nasceu em uma sabado")
elif aniversario.weekday() == 6:
    print("Vc nasceu em uma domingo")
"""
"""
def formata_data(data):
    if data.month == 1:
        return f"{data.day} de janeiro de {data.year}"
    elif data.month == 2:
        return f"{data.day} de fevereiro de {data.year}"
    elif data.month == 3:
        return f"{data.day} de março de {data.year}"
    elif data.month == 4:
        return f"{data.day} de abril de {data.year}"
    elif data.month == 5:
        return f"{data.day} de maio de {data.year}"
    elif data.month == 6:
        return f"{data.day} de junho de {data.year}"
    elif data.month == 7:
        return f"{data.day} de julho de {data.year}"
    elif data.month == 8:
        return f"{data.day} de agosto de {data.year}"
    elif data.month == 9:
        return f"{data.day} de setembro de {data.year}"
    elif data.month == 10:
        return f"{data.day} de outubro de {data.year}"
    elif data.month == 11:
        return f"{data.day} de novembro de {data.year}"
    elif data.month == 12:
        return f"{data.day} de dezembro de {data.year}"
        

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yy hora:minute
hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime("%d de %B de %Y")
print(hoje_formatado)
print(formata_data(hoje))
"""
"""
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yy hora:minute
hoje = datetime.datetime.today()
print(formata_data(hoje))
"""
"""
nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)
nascimento = input("Informe a data de nascimento: ")
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)
"""
"""
# Somente hora
almoco = datetime.time(12, 30, 0)
print(almoco)
"""
"""
import timeit

# Marcando tempo de execução do nosso código com timeit
# Loop for
tempo = timeit.timeit("'-'.join(str(n) for n in range(100))", number=10000)
print(tempo)
# List Comphension
tempo = timeit.timeit("'-'.join([str(n) for n in range(100)])", number=10000)
print(tempo)
# Map
tempo = timeit.timeit("'-'.join(map(str, range(100)))", number=10000)
print(tempo)
"""
import timeit, functools


def teste(n):
    soma = 0
    for num in range(n, 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))
