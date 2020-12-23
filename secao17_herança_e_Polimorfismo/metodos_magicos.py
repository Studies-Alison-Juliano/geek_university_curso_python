"""
POO - Métodos Mágicos

Métodos mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__()

dunder repr -> Representação do objeto


"""
################################################ EXEMPLOS #############################################################

"""
class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f"{self.titulo} escrito por {self.autor}"


livro1 = Livro("Python Rocks!", "Geek University", 400)
livro2 = Livro("Inteligência Artificial com Python", "Geek University", 350)

print(livro1)
print(livro2)
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):  # __str__ prioridade na função print() -> __str__ > __repr__
        return self.titulo

    def __repr__(self):  # __rept__ -> Representation
        return f"{self.titulo} escrito por {self.autor}"

    def __len__(self):  # Deve retornar um inteiro (int)
        return self.paginas

    def __del__(self):  # Overriding (Polimorfismo) del
        print("Um objeto do tipo Livro foi deletado da memória")  # Mensagem de erro apos ser usado o del

    def __add__(self, other):  # Overriding add (+)
        return f"{self} - {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro("Python Rocks!", "Geek University", 400)
livro2 = Livro("Inteligência Artificial com Python", "Geek University", 350)

print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)
