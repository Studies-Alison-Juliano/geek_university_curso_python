"""
POO - Method Resolution Order

Method Resolution Order, é a ordem de execução dos métodos (quem será executado primeiro).

Em Python a gente pode conferir a ordem de execução dos métodos (MRO) de três formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help()
"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f"Eu sou {self.__nome}"


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando."

    def cumprimenta(self):
        return f"Eu sou {self._Animal__nome} do mar"


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando"

    def cumprimenta(self):
        return f"Eu sou {self._Animal__nome} da terra"


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


# Testando
tux = Pinguim("Tux")
print(tux.cumprimenta())

"""
class Pinguim(Aquatico, Terrestre):
Eu sou Tux do mar

Pinguim(Terrestre, Aquatico)
Eu sou Tux da terra
"""