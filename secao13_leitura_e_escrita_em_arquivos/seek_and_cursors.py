"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo

arquivo = open('texto.txt')
print(arquivo.read(), '\n')

# A função seek() e utilizada para movimentação do cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos
# colocar o cursor

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)
print(arquivo.read(), '\n')

arquivo.seek(22)
print(arquivo.read())
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
arquivo = open('texto.txt')
# readline() -> Função que le o arquivo linha a linha
print(arquivo.readline())
ret = arquivo.readline()
print(type(ret))
print(ret)
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
arquivo = open('texto.txt')
linhas = arquivo.readlines()
print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco e o nosso programa.
Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão. Para isso
utilizamos a função close()

Passos para se trabalhar com um arquivo:

1- Abrir um arquivo;
2- Trabalhar o arquivo;
3- Fechar o arquivo;

# 1- Abrir um arquivo;
arquivo = open('texto.txt')

# 2- Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed)  # False | Verifica se o arquivo está aberto ou fechado

# 3- Fechar o arquivo;
arquivo.close()

print(arquivo.closed)  # True

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError

"""
arquivo = open('texto.txt')
# Com a função read() podemos limitar a quantidades de caracteres lidos
print(arquivo.read(50))
