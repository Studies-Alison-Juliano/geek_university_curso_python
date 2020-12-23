"""
Escrevendo em arquivos CSV

writerow() -> Escreve uma linha
"""
"""
# writer() - > Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos este método writerow() para
# escrever cada linha. Este método recebe uma lista.

from csv import writer

with open("filmes.csv", "w") as arquivo:
escritor_csv = writer(arquivo)
filme = None
escritor_csv.writerow(['Titulo', 'Genero', 'Duração'])
while filme != "sair":
    filme = input("Informe o nome do filme: ")
    if filme != "sair":
        genero = input("Informe o genero: ")
        duracao = input("Informe o tempo de duração: ")
        escritor_csv.writerow([filme, genero, duracao])
"""
# DictWriter
# OBS: As chaves do dicionario devem ser as mesmas utilizadas como cabeçalho

from csv import DictWriter

with open("filmes.csv", "w") as arquivo:
    cabecalho = ["Titulo", "Genero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("Informe o genero: ")
            duracao = input("Informe o tempo de duração: ")
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duração": duracao})
