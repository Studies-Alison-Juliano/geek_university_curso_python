"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

OBS : O módulo Pickle não é seguro contra dados maliciosos e desta forma não se é recomendado trabalhar com arquivos
Pickle vindo de outras pessoas que você não conheça ou de fontes desconhecidas.


"""
import pickle

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f"{self.__nome} está comendo...")


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self._Animal__nome} está miando...")


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self._Animal__nome} está latindo...")


"""
felix = Gato("Felix")
pluto = Cachorro("Pluto")

# Escrita em arquivo pickle
with open("animais.pickle", "wb") as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""
# Leitura de dados em um arquivo Pickle
with open("animais.pickle", "rb") as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f"O gato chamasse {gato._Animal__nome}")
    gato.mia()
    print(f"O tipo do gato é {type(gato)}")
    print(f"O cachorro chamasse {cachorro._Animal__nome}")
    cachorro.late()
    print(f"O tipo do cachorro é {type(cachorro)}")
