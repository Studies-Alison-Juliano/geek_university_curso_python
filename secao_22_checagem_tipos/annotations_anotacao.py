import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)  # {'raio': <class 'float'>, 'return': <class 'float'>}

nome: str = "Alison Juliano"
peso: float = 67.9
ativo: bool = True

print(__annotations__)


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:  # None -> Uma função que não retorna nada
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f"{self.__nome} está andando"


p = Pessoa(nome="Alison", idade=18, peso=80.5)
print(p.__dict__)
# print(p.__annotations__)  # Não temos __annotations__
print(p.andar.__annotations__)
print(p.__init__.__annotations__)
