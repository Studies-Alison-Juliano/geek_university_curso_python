"""
Unittest - Antes e após hooks

hooks -> São os testes em si. Ou seja, as execução dos testes.

setup() -> é executado antes de cada método de teste. É util para criarmos instâncias de objetos e outros dados;
tearDown() -> é executado ao final de cada método de teste. É util para excluir dados ou fechar conexões de banco de
dados.


"""
import unittest


class ModuloTest(unittest.TestCase):

    def setup(self):
        # Configurações do setup
        pass

    def test_primeiro(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar após o teste
        pass

    def test_segundo(self):
        # setup vai rodar antes do teste
        # tearDown vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
