import primeiro as pr


def funcao2():
    pr.funcao1()
    print(pr.__name__)

if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente')
else:
    print(f'segundo.py foi importado {__name__}')
