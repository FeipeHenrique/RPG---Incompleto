import json

def carregar():
    with open("save/save.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar(dados):
    with open("save/save.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)


def continuar():
    dados = carregar()
    return dados["capitulo"]


def comecar():
    dados = {
        "capitulo": 1
    }

    salvar(dados)
    return dados["capitulo"]