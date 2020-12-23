"""
POO - O Método super()

O método super() se refere a super classe.


"""
class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} animal faz: {som}")


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        self.__raca = raca


felix = Gato("Felix", "Felino", "Angorá")
felix.faz_som("miau")
