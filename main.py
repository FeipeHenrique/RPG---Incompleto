import os, json
from capitulos.cap1 import cap1

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
with open("save/save.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

while True:
    limpar()
    print('Menu')
    print('1. Jogar!\n2. Começar!')
    c = int(input('>>'))
    if c == 1:
        if dados["capitulo"] == 1:
            cap1()
            break
        else: 
            print('Arquivo não encontrado')
    else:
        dados["capitulo"] = 1
        with open("save/save.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4)