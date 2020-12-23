"""
Levantando o próprio erro com raise

raise -> Lança exceções

OBS: raise não é uma função, é uma palavra reservada, assim como def ou qualquer outra em Python

Para simplificar, pense no raise como sendo util para que possamos criar nossas próprias exceções e mensagens de erro

A forma geral de utilização é :

raise TipoDoErro('Mensagem do erro')

# Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    return f'O texto {texto} será impresso na cor {cor}'


colore('Geek', 4)

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')

OBS: O raise finaliza a função, ou seja, nada após o raise é executado

"""
# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')
