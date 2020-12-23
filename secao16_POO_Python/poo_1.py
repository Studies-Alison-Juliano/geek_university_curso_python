"""
Programação orientada a objetos - POO

- POO é um paradigma de programação que utiliza que mapeamento de objetos do mundo real para modelos computacionais.
- Paradigma de programação é a forma/metodologia utilizada para pensa/desenvolver sistemas.

Principais elementos Orientação a Objeto
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
- Atributo -> Características do objeto;
- Método -> Comportamento do objeto;
- Construtor -> Método especial utilizado para criar os objetos;
- Objeto -> Instância da classe.
"""
numero = 10
print(numero)
print(type(numero))

nome = "Geek"
print(nome)
print(type(nome))


class Produto:
    pass


ps4 = Produto()
# ps4 -> Objeto
# Produto -> Construtor
print(ps4)
print(type(ps4))  # Tipo Produto -> <class '__main__.Produto'>
