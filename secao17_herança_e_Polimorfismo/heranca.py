"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós estendemos outra classe que passa a herdar atributos e métodos
da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

Pergunta: Existe alguma entidade generica o suficiente para encapsular atributos e métodos comum a outras entidades ?

OBS: Quando uma classe herda de outra classe, ela herda todos os atributos e métodos da classe herdada

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe base;
    - Classe Genérica
Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe específica;

# Sobrescrita de método (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe ou em classes filhas
"""
#######################################################################################################################
"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    # Cliente herda de Pessoa
    def __init__(self, renda, nome, sobrenome, cpf):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa
    def __init__(self, matricula, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula


cliente1 = Cliente("Angelina", "Jolie", "123.456.789-00", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987.654.321-11", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self.cpf)
        return f"Funcionario: {self.__matricula} | Nome: {self.nome}"


# Sobrescrita de método (Overriding)

cliente1 = Cliente("Angelina", "Jolie", "123.456.789-00", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987.654.321-11", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
