"""
Lendo arquivos CSV

CSV - Comma Separated Values

# Separador por virgula
1, 2, 3, 4, 5, 6

# Separador por ponto e virgula
1; 2; 3; 4; 5; 6

# Separador por espaço
1 2 3 4 5 6

http://dados.gov.com.br/dataset

# Possível de se trabalhar mas não o ideal (trabalhoso)
with open("lutadores.csv") as arquivo:
    dados = arquivo.read()
    # print(type(dados)) -> str
    dados = dados.split(",")[2:]
    print(dados)

A linguagem Python possuem duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas:
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts:
"""
"""
# Reader
from csv import reader

with open("lutadores.csv") as arquivo:
    leitor_csv = reader(arquivo)  # Iterator
    next(leitor_csv)  # Pular uma linha
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f"{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros")
"""
# DictReader
from csv import DictReader

with open("lutadores.csv") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=",")  # delimiter seleciona o separador especifico do arquivo
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
