"""
Documentando funções com Docstring

OBS: Podemos ter acesso a documentação de uma função em Python utilizando o método especial:__doc__

Podemos ainda fazer acesso a documentação com a função help()
"""
# Exemplos


def diz_oi():
    """Uma função simples que retorna a string oi"""
    return 'oi'


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia

