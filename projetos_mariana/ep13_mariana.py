# ------------------------------------------------------------------
# MODULOS A SEREM UTILIZADOS NO PROGRAMA
import random  # para random.choice(lista) na função gere_frase()

# ------------------------------------------------------------------
# CONSTANTES

# ponto final, ponto de interrogação, ponto de exclamação
# não consideraremos reticências "..."
PONTUACAO_FINAL = ".?!"

# vírgula, ponto e vírgula, dois pontos, fecha parênteses
# não devem ser precedidos de espaço na frase gerada
PONTUACAO_SEM_ESPACO = ',;:)' + PONTUACAO_FINAL

# travesão, aspas, abre chaves
# devem ser precedidos de espaço na frase gerada
PONTUACAO_COM_ESPACO = '—"('

# todas juntas (reticências foram desconsideradas)
PONTUACAO = PONTUACAO_SEM_ESPACO + PONTUACAO_COM_ESPACO

# usado na função insira espacos
ESPACO = ' '

# semente para o gerador aleatório com o objetivo de reprodutibilidade
SEED = 1234


# ------------------------------------------------------------------
#
def main():
    '''(None) -> None

    Para testar as funções juntas. Esta função não será avaliada, entretanto
    ela __não__ deve gerar erro de execução ou sintático.
    Modifique-a se desejar.
    '''
    # Para efeitos de reprodutibilidade
    random.seed(SEED)

    print('ESCREVENDO "como" MACHADO DE ASSIS!\n')

    # 1 leia nome do arquivo
    nome = input("Digite o nome do arquivo com o texto: ")

    # 2 leia o corpus
    try:
        with open(nome, "r", encoding="utf-8") as arq:
            texto = arq.read()
    except:
        print(f"main(): Erro na leitura do arquivo '{nome}'")
        return None

    # 3 insira espaços antes de pontuações
    texto = insira_espacos(texto)

    # 5 construa dicionario de sucessores
    dicio = dicio_sucessores(texto)
    print(dicio)
    print(len(dicio))

    # 6 quantidade de frases que devem ser geradas
    n = int(input("Digite o numero de frases que devem ser geradas: "))

    # 7 gere as frase
    for i in range(n):
        # gere i-ésima frase
        print("---")

        # 7.1 pegue palavra inicial da frase a ser gerada
        palavra_inicial = input(f"Digite a palavra inicial da frase {i + 1}: ")

        # 7.2 gere uma frase começando com palavra_inicial
        frase = gere_frase(palavra_inicial, dicio)
        print("Frase gerada:", frase)

    print("\nFIM")


# ------------------------------------------------------------------
def insira_espacos(txt):
    '''(str) -> str

    RECEBE uma string `txt`.
    RETORNA a string resultante da inserção de um ESPACO antes e depois de
    __cada sinal__ em PONTUACAO que estiver em texto.
    '''
    lista_char = []
    for l in txt:
        lista_char.append(l)
        if l in PONTUACAO:
            lista_char.insert(len(lista_char)-1, ESPACO)
            lista_char.insert(len(lista_char)+1, ESPACO)

    return "".join(lista_char)


# ------------------------------------------------------------------
def dicio_sucessores(lst):
    '''(list) -> dict

    RECEBE uma lista `lst`.
    RETORNA um dicionário em que

        - as __chaves__ são os itens que ocorrem em lst e
        - o  __valor__ associado a cada chave é a lista dos
          itens que ocorrem imediatamente após a chave na lista lst.

    Por convenção a lista correspondente ao valor do último item
    na lst (=lst[-1]) contém o primeiro item da lista (=lst[0]).

    Se a `lst` é a lista vazia a função deve retornar o dicionário vazio.
    '''
    lst_element = insira_espacos(lst).split()
    dic = {}

    # Adicionando primeiro elemento do dicionario a partir do ultimo elemento da lst_element
    if lst_element.count(lst_element[-1]) == 1:
        dic[lst_element[-1]] = [lst_element[0]]
    else:
        dic[lst_element[-1]] = [lst_element[0]]
        for i, e in enumerate(lst_element):
            if i == len(lst_element) - 1:
                break
            elif e == lst_element[-1]:
                dic[lst_element[-1]].append(lst_element[i + 1])

    # Resto do dicionario
    for i, e in enumerate(lst_element):
        if i == len(lst_element) - 1:
            break
        if lst_element.count(e) == 1:
            dic[e] = [lst_element[i + 1]]
        elif lst_element.count(e) > 1 and dic.get(e) is None:
            dic[e] = []
            for i1, e1 in enumerate(lst_element):
                if i1 == len(lst_element) - 1:
                    break
                if e1 == e:
                    dic[e].append(lst_element[i1 + 1])

    return dic


# ------------------------------------------------------------------
def gere_frase(p_inicial, dicio):
    '''(str, dict) -> str

    RECEBE uma palavra `p_inicial` e um dicionário `dicio`.

    O dicionário foi criado a partir de um texto com uma ou
    mais frase; como nos textos de Machado de Assis.

    Cada chave do dicionário é um item (str). O valor no dicionário
    correspondente a uma chave é uma lista (list) de itens (str).

    RETORNA uma string representando uma frase.

    A frase retornada deve começar com a string p_inicial e ser gerada
    segundo o __processo aleatório__ descrito no enunciado.

    Os itens na frase devem ser precedidos de um ESPACO, exceto:

        - a palavra inicial e
        - e os sinais de pontuação na string PONTUACAO_SEM_ESPACO.

    Se p_inicial não está no dicionário a função deve retornar a string vazia.
    '''
    teste_p_inicial = dicio.get(p_inicial)
    lst_texto = []
    text = ""

    while teste_p_inicial:
        rdn_c = random.choice(teste_p_inicial)
        teste_p_inicial = rdn_c
        if "".join(teste_p_inicial) in PONTUACAO_FINAL:
            rdn_c = random.choice(teste_p_inicial)
            teste_p_inicial = rdn_c
            if len(lst_texto) <= 1:
                text = f"{p_inicial}" + " ".join(lst_texto) + teste_p_inicial
            else:
                text = f"{p_inicial} " + " ".join(lst_texto) + teste_p_inicial
            break
        lst_texto.append(teste_p_inicial)
        teste_p_inicial = dicio.get(teste_p_inicial)

    return text


#######################################################
###                 FIM                             ###
#######################################################
#
# Não modifique as linhas abaixo
#
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático
# COMENTE as linhas a seguir durante os testes das suas
# funções no Python Shell

if __name__ == '__main__':
    main()
