"""
1- https://i.imgur.com/HeUuFxx.png

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def info_pessoa(self):
        return f"Nome: {self.__nome}|Idade: {self.__idade}|Altura: {self.__altura}"

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, new):
        if new > 18:
            print("Maior de idade")
        self.__idade = new


user1 = Pessoa("Alison", "26", 1.80)
user1.idade = 20
print(user1.idade)
print(user1.info_pessoa())
"""


class Agenda:

    def __init__(self):
        self.__id = 1
        self.__clientes = {}

    def armazena_pessoa(self, nome, idade, altura):
        if "clientes" not in self.__clientes:
            self.__clientes["clientes"] = {self.__id: {"nome": nome, "idade": idade, "altura": altura}}
        else:
            self.__clientes["clientes"].update({self.__id: {"nome": nome, "idade": idade, "altura": altura}})
        self.__id += 1

    @property
    def clientes(self):
        return self.__clientes

    def remove_pessoa(self, nome):
        for k in list(self.__clientes["clientes"].keys()):
            if nome.title() in self.__clientes["clientes"][k]["nome"]:
                del self.__clientes["clientes"][k]

    def listagem_clientes(self):
        for k, v in self.clientes["clientes"].items():
            print(f"ID: {k} | Nome: {v['nome']} | Idade: {v['idade']} | Altura: {v['altura']}")

    def buscar_pessoa(self, nome):
        for k, v in self.clientes["clientes"].items():
            if nome in v["nome"]:
                print(f"ID: {k} | Nome: {v['nome']} | Idade: {v['idade']} | Altura: {v['altura']}")


db = Agenda()
db.armazena_pessoa("Alison", "26", 1.80)
db.armazena_pessoa("Santos", "20", 1.50)
db.armazena_pessoa("Juliano", "18", 1.67)
db.armazena_pessoa("Alison", "18", 1.67)
db.remove_pessoa("Santos")
print(db.clientes)
print("Listagem de clientes..")
db.listagem_clientes()
print("Buscando pessoa(s)...")
db.buscar_pessoa("Alison")
