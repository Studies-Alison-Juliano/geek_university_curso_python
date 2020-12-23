"""
POO - Classes

Em POO, classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    -Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iriamos querer saber se a lâmpada é
    110 ou 220 volts, se ela é branca, vermelha, amarela ou outra cor, qual é a luminosidade dela e etc...

    -Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que esse objeto pode realizar no
    seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente iriamos querer
    representar no nosso sistema é o de ligar e desligar a mesma.


Em Python para definir uma classe utilizamos a palavra reservada class.

OBS: Quanto nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúsculo. Se o nome for
composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.

Dica Geek: Em computação não utilizamos: acentuação, caracteres especiais, espaços ou similares para nomes de classe,
atributos, método, arquivos, diretório e etc.

OBS: Quando estamos planejando um software e definimos quais classes que teremos que ter no sistema, chamamos estes
objetos que serão mapeados para classes de entidade.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


lamp = Lampada()
print(type(lamp))
