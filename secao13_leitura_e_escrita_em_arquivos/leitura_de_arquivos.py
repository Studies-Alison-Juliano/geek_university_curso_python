"""
Leitura de Arquivos

Para abrir o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'

open() -> Na forma mais simples de utilização nos passamos apenas um parâmetro de entrada, que neste caso é o caminho
para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

http://docs.python.org/3/library/functions.html#open

# OBS: Por padrão a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro
FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> Modo de leitura. r -> read() -> ler
"""
# Exemplo
arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

ret = arquivo.read()
print(type(ret))
print(ret)
print(arquivo.read())
# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamados cursor. Esse cursor, funciona como o cursor
# quando estamos escrevendo.

print(arquivo.read())

# OBS: A função read() le todo o conteúdo do arquivo
