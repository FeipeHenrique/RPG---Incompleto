from util import *

def capitulo1():
    limpar_tela()
    print(f"{ciano}=== Capítulo 1 - A floresta misteriosa ==={reset}")
    animacao("Você acorda em uma floresta densa e misteriosa. O sol mal consegue penetrar pelas copas das árvores, e o ar está cheio de um cheiro estranho.")
    animacao("Você não tem ideia de como chegou ali, mas sabe que precisa encontrar uma saída.")
    animacao("Enquanto explora a floresta, você encontra um caminho bifurcado.")
    input(f"{amarelo}[Enter] para continuar >> {reset}")
    limpar_tela()
    print("1 - Seguir o caminho da esquerda")
    print("2 - Seguir o caminho da direita")
    escolha = input(f"{amarelo}Escolha uma opção: {reset}")
    if escolha == "1":
        limpar_tela()
        animacao("Você segue o caminho da esquerda e encontra uma cabana abandonada. A porta está entreaberta, e você pode ouvir sons estranhos vindo de dentro.")
        input(f"{amarelo}[Enter] para continuar >> {reset}")
        limpar_tela()
    elif escolha == "2":
        limpar_tela()
        animacao("Você segue o caminho da direita e encontra um rio caudaloso. A água é cristalina, mas você pode sentir algo estranho vindo dela.")
        input(f"{amarelo}[Enter] para continuar >> {reset}")
        limpar_tela()
    else:
        limpar_tela()
        capitulo1()  # Volta para o início do capítulo se a escolha for inválida