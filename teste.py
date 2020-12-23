import random

SEED = 1234
random.seed(SEED)
lista = {"1": ["a", "z", "x"], "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i", "10": "j", "11": "k"}
PONTUACAO_FINAL = ".?!"
teste = "1"

print(lista.get(teste))

"""if i == len(lst_element) - 1:
    break
if lst_element.count(e) == 1:
    dic[e] = [lst_element[i + 1]]
else:
    dic[e] = []
    for i1, e1 in enumerate(lst_element):
        if i1 == len(lst_element) - 1:
            break
        if e1 == e:
            dic[e].append(lst_element[i1 + 1])"""
