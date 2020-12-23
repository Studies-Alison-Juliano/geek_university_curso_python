"""
Módulos externos

Utilizamos o gerenciados de pacotes Python chamado Pip - Python Installer Package

Você pode conhecer todos os pacotes externos oficiais em: http://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo:

pip install nome_modulo
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Instalando pacote colorama

pip install colorama

# Utilizando o pacote instalado
from colorama import init, Fore
init()
print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')

import pdfkit
pdfkit.from_string('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial</strong>', 'out.pdf')

"""

