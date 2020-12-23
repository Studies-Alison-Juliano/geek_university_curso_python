"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu
sistema.

Em Python dividimos os métodos em dois grupos: Métodos de instância e Métodos de classe.

# Métodos de instância

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir um objeto a partir
da classe.

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhado! Python possuí vários
métodos com esta forma de nomenclatura que pode ser que mudemos o comportamento dessas funções mágicas internas da
linguagem. Evite ao máximo!

OBS: Métodos são escritos em letra minúscula. Se o nome for composto, será separado por underline

# Métodos de classe em Python são conhecidos como métodos estáticos em outras linguagens
"""
class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f"Classe: {cls}")
        print(f"Temos {cls.contador} usuários no sistema")

    @classmethod
    def ver(cls):
        print("Teste")

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f"Usuário criado: {self.__gera_usuario()}")

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split("@")[0]

"""
nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o email: ")
senha = input("Informe o senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print("Usuario criado com sucesso")
else:
    print("Senha não confere...")
    exit(1)

senha = input("Informe a senha para acesso: ")

if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")

print(f"Senha User Criptografada: {user._Usuario__senha}")  # Acesso errado
"""
#######################################################################################################################
"""
# Método de classe

user = Usuario("Felicity", "Jones", "felicity@gmail.com", "654321")
Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta
"""
# Método estático
print(Usuario.contador)
print(Usuario.definicao())
user = Usuario("Felicity", "Jones", "felicity@gmail.com", "123456")
print(user.contador)
print(user.definicao())
