def funcao1(t):
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'{__name__}.py foi importado ')


x = funcao1()
print(x)
