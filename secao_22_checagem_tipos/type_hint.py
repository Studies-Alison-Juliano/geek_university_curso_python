# Definição do tipo de parâmetro recebido e tipo do dado retornado
def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}"


print(cumprimentar("Alison"))


def cabecalho(texto: str, alinhamento: bool =True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    return f" {texto.title()} ".center(50, "#")


print(cabecalho("Geek University"))
print(cabecalho("Geek University", alinhamento=False))
