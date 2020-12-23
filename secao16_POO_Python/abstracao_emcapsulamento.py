"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> Cápsula

                classe
------------------------------------
|                                   |
|       atributos e métodos         |
|___________________________________|

# Relembrando: Atributos/Métodos privados em Python
Imagine que temos uma classe chamada "Pessoa" contendo um atributo privado chamado __nome e um método privado chamado
__falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe, mas Python não bloqueia este acesso fora da
classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de se acessar os elementos
privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._pessoa__nome
instancia._pessoa__falar()

Abstração, em POO, é o ato de expor dados relevantes de uma classe, escondendo atributos e métodos de usuário.


"""
class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor

        # 2 - Adicionar valor a conta de destino
        conta_destino.__saldo += valor


"""
# Testando class Conta com atributos públicos

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)

conta1.numero = 42
conta1.titular = "Xuxa"
conta1.saldo = 99999999999999999
conta1.limite = 9999999999999999999999999999999999
"""
"""
print(conta1._Conta__titular)  # Name Mangling
conta1._Conta__titular = "Angelina"
print(conta1.__dict__)
"""
conta1 = Conta("Angelina", 150.00, 1500)
conta1.extrato()
conta2 = Conta("Felicity", 300, 2000)
conta2.extrato()

conta1.depositar(150)
print(conta1.__dict__)

conta1.sacar(200)
print(conta1.__dict__)

conta2.transferir(100, conta1)
