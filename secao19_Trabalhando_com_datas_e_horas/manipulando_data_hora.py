"""
Manipulando data & hora

Python tem um módulo built-in para se trabalhar com data e hora chamado datetime
"""
import datetime

"""
# print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2020-11-29 00:43:44.830891
# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

inicio = datetime.datetime.now()
print(inicio)
# Alterando o horário
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)
"""

"""
nascimento = input("Informe sua data de nascimento (dd/mm/yy): ")
print(nascimento)
nascimento = nascimento.split("/")
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
"""
evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
