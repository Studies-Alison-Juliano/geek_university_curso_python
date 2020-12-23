"""
Decoradores (Decorator)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de higher order functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar)


|------------------------------------------------------------------------|
|                           Function Decorator                           |
|------------------------------------------------------------------------|


|-----------------------------------------------------------------------------------|
|    |------------------------------------------------------------------------|     |
|    |                           Função decorada                              |     |
|    |------------------------------------------------------------------------|     |
|-----------------------------------------------------------------------------------|

# Decorators como funções (Sintaxe não recomendada)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) a Geek University')


# Testando 1
teste = seja_educado(saudacao)
teste()

# Testando 2


def raiva():
    print('Eu te odeio!')


raiva_educada = seja_educado(raiva)
raiva_educada()
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Decorators com Syntax Sugar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testeando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

|------------------------------------------------- |
| Home  | Serviços  | Produtos  | Administrativas  |
|--------------------------------------------------|

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/admin

# OBS: Não é código funcional. É APENAS EXEMPLO

def checa_login(request):  # recorator function
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')


def home(request):
    return 'Pode acessar home'

def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login  # @checa_login -> Decorator
def admin(request)
    return 'Pode acessar admin'
"""
# OBS: Não confunda decorator com decorator function


