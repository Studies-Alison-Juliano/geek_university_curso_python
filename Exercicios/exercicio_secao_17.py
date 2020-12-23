class Pessoa:

    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def exibe(self, idade):
        if idade == 1:
            return f"{self.__codigo}. Nome: {self.__nome}, Idade: {self.__idade}"
        return f"{self.__codigo}. Nome: {self.__nome}"


x = Pessoa(100, "Alison", 18)
print(x.exibe(0))
