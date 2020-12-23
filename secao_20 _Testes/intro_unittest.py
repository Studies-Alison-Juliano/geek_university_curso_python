"""
Introdução ao módulo Unittest

Unittest -> Testes unitários

O que são testes unitários?

Teste unitário é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

#OBS: Teste unitário não é especifico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TesteCase e a partir de então ganhamos todos os
'Assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions

Doc unittest:
https://docs.python.org/3/library/unittest.html#unittest.TestCase

Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os teste com unittest no modo verbose

python nome_do_modulo -v

# Docstring nos testes

Podemos acrescentar (e é recomendado) docstrings nos nossos testes.
"""
# Pratica - Utilizando a abordagem TDD

