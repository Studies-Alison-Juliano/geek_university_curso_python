"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem python

A ideia da PEP8 é para que possamos escrever codígos pythonicos.

    [1] Utilize camel case para nome de classes.

        class Calculadora:
        pass


        class CalculadoraCientifica:
        pass

    [2] Utilizar nomes em minúsculo, separados por underline para funções e variáveis.

        def soma():
        pass


        def soma_dois():
        pass


        numero = 4

        numero_impar = 4

    [3] Utilize 4 espaços para indentação! (Não utilize tab)

        if 'a' in 'banana':
            print('tem')

    [4] Linhas em branco (Parágrafos em branco)

     -Separar funções e definições da classe com 2 parágrafos (2 linhas em branco)
     -Métodos dentro de uma classe devem ser separados por apenas 1 parágrafo

    [5] Imports:

     -Imports devem sempre ser feitos em linhas separadas:
            # Import errado

                import sys, os

                # Import certo

                import sys
                import os

            # Não há problemas em utilizar:

                from types import StringType, ListType

            # Caso tenha muitos imports de um mesmo pacote, recomenda-se:

                from types import (
                    StringType,
                    ListType,
                    SetType,
                    outrotype
                )

            # Imports devem ser sempre colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
            # e antes de constantes ou variáveis globais.

     [6] Espaços em instruções e expressões:
            # Não correto:
                spam( ham[ 1 ], { eggs: 2 } )
                algo (1)

            # Correto
                spam(ham[1], {eggs: 2})
                algo(1)

     [7] Termine sempre uma instrução com uma nova linha
"""
