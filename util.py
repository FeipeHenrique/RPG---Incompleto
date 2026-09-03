import os, time

RED = '\033[31m'     # Terror, suspense.
GREEN = '\033[32m'   # Itens
YELLOW = '\033[33m'  # Para perguntas
BLUE = '\033[94m'    # Cartas, bilhetes etc.
MAGENTA = '\033[35m' # Game Over
CYAN = '\033[36m'    # Títulos
GRAY = '\033[90m'    # Indisponível
RESET = '\033[0m'    # Branco / Narração

def centralizar_texto(texto):
    linhas = texto.split('\n')
    largura_terminal = os.get_terminal_size().columns
    return '\n'.join(linha.center(largura_terminal) for linha in linhas)

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def animar_texto(texto, delay=0.05):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()

def suspense(pontos=3, delay=0.5):
    for _ in range(pontos):
        print('.', end='', flush=True)
        time.sleep(delay)
    print('\n')