"""
Escrevendo um Iterator customizado

"""


class Contador:
    def __init__(self, menor, maior):
        self.maior = maior
        self.menor = menor

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


con = Contador(1, 61)
for n in Contador(1, 61):
    print(n)
