"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita. Apenas ler. Da mesma forma, se abrirmos um
arquivo para escrita, não podemos lelo, somente escrever

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no SO

Para escrever dados em um arquivo, após abrir o arquivo utilizamos a função write(). Está função recebe uma string como
parâmetro. Caso contrario teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado, caso ele ja exista, o anterior
sera apagado e um novo sera criado. Dessa forma, todo o conteudo anterior é perdido.

# Exemplo de escrita - modo 'w' - write
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito facil. \n')
    arquivo.write('Podemos escrever quantas linhas quisermos. \n')
    arquivo.write('Esta é a ultima linha. \n')

# Forma não Pythonica de escrita em arquivo
arquivo = open('mais.txt', 'w')

arquivo.write('Texto do caraio')
arquivo.write('Texto')

arquivo.close()

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek' * 1000)

with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite "sair": ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
"""

