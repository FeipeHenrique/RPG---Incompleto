import json

def cap1():
    print("Esse é o capitulo 1!!!!")

    with open("save/save.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    dados["capitulo"] = 2
    with open("save/save.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)