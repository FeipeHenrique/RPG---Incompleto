import sys
sys.dont_write_bytecode = True # isso faz com que pare de aparecer aquelas pastas "py__pycache_" 

from util import *
from save import continuar, comecar
from capitulos.cap1 import cap1
from capitulos.cap2 import cap2


while True:
    limpar()
    print("Menu")
    print("1. Continuar\n2. Novo Jogo\n3. Sair")

    c = int(input(">> "))
    if c == 1:
        capitulo = continuar()
    elif c == 2:
        capitulo = comecar()
    elif c == 3:
        print("Saindo...")
        break
    else:
        continue

    if capitulo == 1:
        cap1()
    elif capitulo == 2:
        cap2()
    break