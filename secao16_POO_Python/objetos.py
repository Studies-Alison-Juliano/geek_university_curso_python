"""
POO - Objetos

Objetos -> São instancias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma class
como variáveis do tipo definido na classe
"""
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampda(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def nome(self):
        return self.__nome


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f"O cliente é {Cliente.nome(self.__cliente)}")

    def diz(self):
        print(f"O cliente {Cliente.nome(self.__cliente)} diz oi")

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


"""
# Instâncias/objetos

lamp1 = Lampada("Branca", 110, 60)
lamp1.ligar_desligar()
print(f"A lampada está ligada ? {lamp1.checa_lampda()}")
cc1 = ContaCorrente(5000, 20000)
user1 = Usuario("Felicity", "Jones", "felicity@gmail.com", "123456")
"""
cli1 = Cliente("Felicity Jones", "123.456.789.99")
cc = ContaCorrente(5000, 10000, cli1)
cc.mostra_cliente()
cc.diz()
