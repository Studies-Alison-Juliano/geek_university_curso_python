# CONSTANTES
ESPACO = ' '
BRANCO = ["\\n", "\t", "\v", "\r", "\f"]


# ------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo outros testes.
    '''

    # 1. leia o limite de caracteres por linha
    k = int(input("Digite o no. de colunas por linha (> 0): "))

    # 2. leia o texto de um arquivo
    # 2.1 leia o nome do arquivo
    nome = input("Digite o nome do arquivo: ")
    # 2.2 "abra" o arquivo
    arquivo = open(nome, 'r', encoding='utf-8')
    # 2.3 leia o conteudo do arquivo e chame de txt
    txt = arquivo.read()
    # 2.4 feche o arquivo
    arquivo.close()

    # 3. faça uma reguinha
    # reguinha = s[:k]
    reguinha = " " + ((k // 5 + 1) * '....*')[:k]  # reguinha

    # 4. exiba o texto original
    print("Texto original: ")
    print(reguinha)
    print(txt + '\n')  # '\n' para mudar de linha

    # 5. ajuste o limite da coluna
    # de txt para uma lista de strings k-ajustadas à esquerda
    print(f"Texto com linhas {k}-ajustadas à esquerda: ")
    lst_str_esq = ajuste_esquerda(txt, k)
    print(reguinha)
    for linha in lst_str_esq:
        print('|' + linha + '|')
    print()

    # 6. ajuste o limite da coluna
    # de lista de strings k-ajustadas à esquerda para k-ajustadas completas
    print(f"Texto linhas {k}-ajustadas completamente: ")
    lst_str_comp = ajuste_completo(lst_str_esq, k)
    print(reguinha)
    for linha in lst_str_comp:
        print("|" + linha + "|")


# --------------------------------------------------------
def ajuste_esquerda(txt, k):
    '''(str, int) -> list de str

    RECEBE  uma string `txt` e um inteiro `k`.
    RETORNA A lista de strings k-ajustadas à esquerda que representa `txt`.
    '''
    for c in BRANCO:
        txt = txt.replace(c, " ")
    split_palavra = txt.split()  # String Methods
    lista_alinhada_esquerda = []
    l1 = []
    sum_len = 0
    for p in split_palavra:
        if len(p) <= k:
            sum_len += len(p)

            if sum_len < k - (len(l1) - 1):
                l1.append(p)
            else:
                frase = " ".join(l1)
                lista_alinhada_esquerda.append(frase)
                l1.clear()
                l1.append(p)
                sum_len = len(p)

            if sum_len == k - (len(l1) - 1):  # espaco (" ") = 1..N
                frase = " ".join(l1)
                lista_alinhada_esquerda.append(frase)
                sum_len = 0
                l1.clear()

            if p == split_palavra[len(split_palavra)-1]:
                if sum_len < k - (len(l1) - 1):
                    frase = " ".join(l1)
                    lista_alinhada_esquerda.append(frase)
        else:
            lista_alinhada_esquerda.append(p)
    return lista_alinhada_esquerda


# --------------------------------------------------------
def ajuste_completo(lst_str, k):
    '''
    (list de str, int) -> list de str

    RECEBE  uma lista de strings `lst_str` e um inteiro `k` tais que cada string na
       lista é `k`-ajustada à esquerda.
    CRIA e RETORNA A lista com as strings em `lst_str` k-ajustadas completamente.
    '''
    lista_ajuste_completo = []
    l1 = []
    for elemento in lst_str:
        if len(elemento) == k:
            lista_ajuste_completo.append(elemento)
        elif len(elemento) < k:
            l1.append(elemento)

    l2 = []
    for elemento in l1:
        espaco = k - len(elemento)
        contador = 0
        for p1 in elemento.split():
            l2.append(p1)
            if " ".join(l2) == elemento:
                while contador < espaco:
                    for p2 in l2:
                        if len(l2) == 1:
                            if contador < espaco:
                                l2[l2.index(p2)] = p2 + " "
                                contador += 1
                        else:
                            if contador < espaco:
                                if p2 != l2[len(l2) - 1]:
                                    l2[l2.index(p2)] = p2 + " "
                                    contador += 1
                lista_ajuste_completo.append(" ".join(l2))
                l2.clear()
    return lista_ajuste_completo


#######################################################
###                 FIM                             ###
#######################################################
#
# Esse if serve para rodar a main() dentro do Spyder.
if __name__ == '__main__':
    main()
