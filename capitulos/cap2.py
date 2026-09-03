import sys
sys.dont_write_bytecode = True

import json

def cap2():
    print("Esse é o capitulo 2!!!!")

    with open("save/save.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    dados["capitulo"] = 2
    with open("save/save.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)