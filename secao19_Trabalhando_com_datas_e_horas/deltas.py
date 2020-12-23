"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yy 12:55:34.9939329
data_final = dd/mm/yy 13:34:23.0948464

delta = data_final - data_inicial
"""
import datetime

"""
data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2019, 3, 3, 0)
# calculando delta
tempo_para_evento = aniversario - data_hoje
print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)
print(f"Faltam {tempo_para_evento.days}, {tempo_para_evento.days // 60 // 60} horas...")
"""
data_da_compra = datetime.datetime.now()
print(data_da_compra)
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)
