"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão:
    - Permissão de leitura -> Para de ler o arquivo.
    - Permissão de escrita -> Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.
"""
# Primeiro fazemos o import
from io import StringIO
mensagem = 'Essa é apenas uma string normal'

# Podemos criar um arquivo em memória ja com uma string inserida, ou mesmo vazio para inserir texto depois.
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')
# Agora tendo o arquivo, podemos utilizar tudo que ja sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)
print(arquivo.read())
