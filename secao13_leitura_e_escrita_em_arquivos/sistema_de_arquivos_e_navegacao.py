"""
Sistema de arquivos e navegação

Para fazer o uso de manipulação de arquivos do SO, precisamos importar e fazer uso do módulo os.

os -> Sistema Operacional

# Fazer import
import os

# getcwd() -> Pega o current work directory
# Retorna o Path (caminho) absoluto
print(os.getcwd())  # C:\Users\aliso\PycharmProjects\guppe

# Para mudar o diretório podemos usar chdir()
os.chdir('..')
print(os.getcwd())  # C:\Users\aliso\PycharmProjects

os.chdir('..')
print(os.getcwd())  # C:\Users\aliso

os.chdir('..')
print(os.getcwd())  # C:\Users

os.chdir('..')
print(os.getcwd())  # C:\

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Fazer import
import os

# Podemos checar se um diretório é absoluto ou relativo
print(os.path.isabs('C:/Users/aliso'))  # True

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())  # Se for usuário Linux/Mac
print(os.name)  # Se for o usuário for Windows

import sys
print(sys.platform)  # win32
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print(os.getcwd())  # C:\Users\aliso\PycharmProjects\guppe
tes = os.path.join(os.getcwd(), 'Geek', 'university')
os.chdir(tes)
print(os.getcwd())  # C:\Users\aliso\PycharmProjects\guppe\Geek\university

# Veja que os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que sera
# juntado ao atual
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir('C:/'))
"""
# Fazer import
import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()
scanner = os.scandir()
arquivos = list(scanner)
print(arquivos)
print(dir(arquivos[0]))
print(arquivos[0].inode())
print(arquivos[0].is_dir())  # é um diretório ? False
print(arquivos[0].is_file())  # é um arquivo ? True
print(arquivos[0].is_symlink())  # é um link simbólico ? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatísticas

# Quando utilizamos a função scandir() precisamos fechá-la assim quando abrimos um arquivo

scanner.close()
