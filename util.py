import os, time
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def animacao(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()  # Pula para a próxima linha após a animação

vermelho = "\033[31m" # Para terror, suspense e momentos de tensão
ciano = "\033[36m" # Para titulos, locais e descrições
verde = "\033[32m" # Para a coleta de itens e progresso
amarelo = "\033[33m" # Para perguntas e escolhas
azul = "\033[34m" # Para sitações, cartas e mensagens importantes
roxo = "\033[35m" # Para o game over 
reset = "\033[0m" # Para resetar a cor após o uso