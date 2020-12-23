"""
1 - https://i.imgur.com/7YUyEGs.png

def caracteristicas(**kwargs):
    '''
    Função que guarda informações características de cada habitante
    '''
    lista_habitantes.append(kwargs)
    if len(lista_habitantes) == 5:
        contador = 1
        for h in lista_habitantes:
            print(f'Habitante numero {contador}: Sexo: {h.get("sexo")} | Cor dos Olhos: {h.get("cor_olhos")} | Cor do Cabelo: {h.get("cor_cabelo")} | Idade: {h.get("idade")}')
            contador += 1


def media_idade():
    '''
    Função que faz uma média da idade entre pessoas com cabelo preto e castanho
    '''
    soma_cabelo = 0
    media = 0
    for h in lista_habitantes:
        if h['cor_cabelo'] == 'castanho' or h['cor_cabelo'] == 'preto':
            soma_cabelo += h['idade']
            media += 1
    media_final = soma_cabelo / media
    return f'Media de idade entre pessoas com cabelo preto e castanho: {media_final}'


def maior_idade():
    '''
    Função que devolve a maior idade dentre os habitantes
    '''
    maior = 0
    for h in lista_habitantes:
        if maior < h['idade']:
            maior = h['idade']
    return f'O habitante mais velho tem: {maior} anos de idade'


lista_habitantes = []
for n in range(1, 5+1):
    print(f'=-=-=-=-=-= Habitante {n} =-=-=-=-=-=')
    sexo = input('Sexo: ')
    cor_olhos = input('Cor dos olhos: ')
    cor_cabelo = input('Cor do cabelo: ')
    idade = int(input('Idade: '))
    caracteristicas(sexo=sexo, cor_olhos=cor_olhos, cor_cabelo=cor_cabelo, idade=idade)

# Print da media de idade entre pessoas com cabelo preto e castanho:
print(media_idade())

# Print do habitante mais velho:
print(maior_idade())

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
2.

def data(dia, mes, ano):
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
             9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    if int(mes) > 9:
        return f'Dia {dia} de {meses.get(int(mes))} do ano {ano}'
    return f'Dia {dia} de {meses.get(int(mes.split("0")[1]))} do ano {ano}'


informe_data = input('Informe a data:').split('/')
print(data(informe_data[0], informe_data[1], informe_data[2]))
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
3.

nomes = ['Alison', 'Juliano', 'Rafael']
print(list(map(lambda nome: f'Sr.{nome}', nomes)))

nomes = ['Alison Santos', 'Juliano Alvoro Cabral', 'Rafael Mate Martins Moreira']
print(list(map(lambda esp: f'{esp}, contem {esp.count(" ")} espaço(s)', nomes)))

numeros = [-1, 2, 3.4, 99, -45, 7, 8, 9, 10, -2, -3]
print(list(filter(lambda n: n < 0, numeros)))

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                                          =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
4.
Em MAC0110 o DV de um número inteiro não-negativo será formado por um par dv1 e dv2 de dígitos verificadores. Os dígitos
dv1 e dv2 serão algarismos entre 0 e 9 calculados como descrito a seguir.

Para determinar o valor dv1 de um número inteiro n = d1d2…dk − 1dk, onde di é um dígito entre 0 e 9, devemos primeiro
calcular a soma 1 × d1 + 2 × d2 + 3 × d3 + ⋯ + k × dk. O dígito verificador dv1 será o resto da divisão dessa soma por
11. Se esse resto for 10, então dv1 será 0.

Por exemplo, para o número n=280012386 temos que a soma acima é
1 × 2 + 2 × 8 + 3 × 0 + 4 × 0 + 5 × 1 + 6 × 2 + 7 × 3 + 8 × 8 + 9 × 6 = 174, e portanto dv1 é 9.

O dígito verificador dv2 será determinado de maneira semelhante. Primeiro calculamos uma soma levemente diferente da
anterior 0 × d1 + 1 × d2 + 2 × d3 + 3 × d4 + ⋯ + (k − 1) × dk + k × dv1. O dígito dv2 será o resto da divisão dessa
soma por 11. Se esse resto for 10, então dv2 será 0.

Continuando o exemplo para o número n=280012386, essa nova soma é
0 × 2 + 1 × 8 + 2 × 0 + 3 × 0 + 4 × 1 + 5 × 2 + 6 × 3 + 7 × 8 + 8 × 6 + 9 × 9 = 225, e portanto dv2 é 5.

Dessa forma, o DV de MAC0110 para o número 280012386 será o par 9 5.
R.

n_inicial = list(input('n: '))
c1 = [n * int(n_inicial[n-1]) for n in range(1, 9+1)]
dv1 = sum(c1) % 11
print(dv1)

c2 = [n * int(n_inicial[n]) for n in range(9)]
dv2 = (sum(c2) + (9 * dv1)) % 11
print(dv2)
"""

