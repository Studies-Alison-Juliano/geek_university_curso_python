"""
JSON e Pickle

JSON -> JavaScript Object Notation
API -> Meios de comunicação entre os serviços oferecidos por empresas (Twitter, YouTube, Facebook) e terceiros.

import json

ret = json.dumps(['Produto', {'PlayStation 4': ('2TB', 'Novo', "220V", 2340)}])
print(ret)
print(type(ret))

"""
"""
import json
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Viralata")
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)

ret1 = jsonpickle.encode(felix)
print(ret1)
"""
"""
# Escrevendo em arquivo JSON
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Viralata")
with open("felix.json", "w") as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""
# Lendo em arquivo JSON
import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open("felix.json", "r") as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
