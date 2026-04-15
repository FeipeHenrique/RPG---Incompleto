import json, cap1
from util import *

with open("save.json", "r") as f:
    save_data = json.load(f)

print(f"{ciano}=== Menu ==={reset}")
input(f"{amarelo}[ENTER] para jogar >> {reset}")

if save_data["capitulo"] == 1:
    cap1.capitulo1()