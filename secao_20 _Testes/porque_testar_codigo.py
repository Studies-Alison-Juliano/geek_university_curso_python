"""
Por que testar nosso código ?

Testes automatizados!

            Aplicação Web
----------------------------------------------
|                                            |
|            frontend & backend              |
----------------------------------------------
|           Testes automatizados             |
----------------------------------------------

Por que testar nosso código ?
- Reduzir os bugs no código
- Testes garantem que novos recursos da sua aplicação não alterem recursos antigos

TDD - Test Driven Development

Com TDD é utilizado estágios de desenvolvimento
    - Você escreve o teste primeiro
    - Então você escreve o código mínimo suficiente para fazer o teste passar
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;

"""
class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f"{self.nome} está miando...")


felix = Gato("Felix")
felix.miar()
print(felix.nome)
