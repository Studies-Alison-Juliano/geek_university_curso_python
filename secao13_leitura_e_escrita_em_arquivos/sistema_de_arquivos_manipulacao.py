"""
Sistema de arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('texto.txt'))  # True

# Diretório

# Paths Relativos
print(os.path.exists('Geek'))  # True
print(os.path.exists('Geek/university'))  # True
print(os.path.exists('Geek/university/geek3.py'))  # True
print(os.path.exists('outro'))  # False

# Paths Absolutos
print(os.path.exists('C:/Geek/university'))  # False
print(os.path.exists('C:/Users/aliso/PycharmProjects'))  # True
print(os.path.exists('C:/Users/aliso/PycharmProjects/guppe/sistema_de_arquivos_manipulacao.py'))  # True
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', w) as arquivo:
    pass  # Pass -> Apenas executa o bloco. Caso não tenha pass obterá um SyntaxError

os.mknod('arquivoteste.txt', )  # mknod() -> Não funciona no Windows HOME. NÃO TESTADO -> Funciona apenas no Windows Professional
os.mknod('C:/Users/aliso/Desktop/Alison/Guppe Python/Seção 13 aula 95.txt')

# OBS: Se o arquivo ja existir teremos o erro FileExistError

os.open('arquivo-teste4.txt', 0o600)  #
os.open('C:/Users/aliso/Desktop/Alison/Guppe Python/Seção 13 aula 95.txt', 0o600)

# OBS: 0o600 chave de permissão
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Criando Diretórios - Únicos (Um a um)

# Path Relativo
os.mkdir('templates')
# OBS: A função mkdir() cria um diretório se esse não existir. Caso exista teremos um FileExistError

# Path Absoluto
os.mkdir('C:/Users/aliso/Desktop/Alison/Guppe Python/Seção 13')
# OBS: Se não tivermos permissão para criar um diretório teremos um PermissionError

# Criando multi-diretórios (Arvore de diretórios)
os.makedirs('templates/geek/university')
# OBS: Se já existir, teremos um FileExistError

os.makedirs('templates/geek/university', exist_ok=True)  # Caso ja exista tal diretório a segunda chave "exist_ok=True"
ira apenas ignorar e não dara erro

# Renomear arquivos e diretórios
os.rename('templates/geek', 'templates/geek2')
# OBS: Se o diretório não existir teremos um FileNotFoundError

# Arquivos
os.rename('templates/geek/university/teste.txt', 'templates/geek/university/geek.txt')
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ATENÇÃO: Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, ele ou eles não vão para a
# lixeira, eles somem!

# Removendo arquivos
os.remove('geek.txt')

# OBS: Se você estiver no windows e o arquivo que você for deletar estiver em uso, você terá um erro.
# OBS: Caso arquivo não existe, teremos NotFoundError
# OBS: Se você informar um diretório ao inves de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios
os.rmdir('templates')
# Se o diretório tiver qualquer conteúdo teremos um OSError
# Se o diretório não existir, teremos um FileNotFoundError

# Removendo uma arvore de arquivos:
for arquivos in os.scandir('templates'):
    if arquivos.is_file():
        os.remove(arquivos)

# Removendo uma arvore de diretório vazios:
os.removedirs('templates/geek2/university')
# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# Importando biblioteca send2trash (Envia arquivos e diretórios para lixeira)
from send2trash import send2trash

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!
send2trash('templates/geek2/university/geek.txt')  # Vai para lixeira e pode ser restaurado

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um arquivo temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University \n')

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto.
# No final usamos um input() só para mantermos os arquivos temporários vivos dentro dos blocos with

# OBS: Possivelmente, o código acima não ira funcionar se vc estiver utilizando o windows.

# Criando um arquivo temporário
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University \n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso utilizamos b''
"""
# Trabalhando com arquivos e diretórios temporários
import os
import tempfile


