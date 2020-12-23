"""
Definindo funções

Funções são pequenas partes de códigos que realizam tarefas especificas
Pode ou não receber entradas de dados e retornar uma saída de dados
Muito uteis para execultar procedimentos similares por repetidas vezes

Obs: Se vc escrever uma função que realiza varias tarefas dentro dela, é bom fazer uma verificação para que a função
seja simplificada

Ja utilizamos varias funções desde que iniciamos este curso:
- print
- len
- max
- min
- e muitas outras

"""
# Exemplo de utilização de funções

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do python print()

# print(cores)

# curso = 'Programação Python: Essencial'

# print(curso)

# cores.append('roxo')

# print(cores)

# DRY - Don't repeat yourself

# Como definir funções

"""
Em Python, a forma geral de definir uma função é:

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função
        
Onde :
nome_da_funcao -> sempre com letras minúsculas, e se for nome composto, separado por underline (Snake Case);
parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou n retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo
uma função. Também abrimos o bloco de código com o ja conhecido dois pontos: Que é utilizado para definir blocos

"""
# Definindo a primeira função

# Definição
def diz_oi():
    print('oi')


"""
OBS:

1 - Veja que dentro das nossas funções podemos utilizar outras funções:
2 - Veja que nossa função só executa uma tarefa, ou seja, a unica coisa que elas faz é dizer 'oi'
3 - Veja que está função não recebe nenhum parâmetro de entrada
4 - Veja que está função não retorna nada
"""
# Utilizando funções:

# Chamada de execução
# diz_oi()

"""
Atenção! Nunca esqueça de utilizar o parênteses ao executar uma função

Exemplo:
# Errado
diz_oi 

# Certo
diz_oi()
"""
# Exemplo 2


def cantar_parabens():
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()

# Em Python, podemos exclusive criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens

canta()
