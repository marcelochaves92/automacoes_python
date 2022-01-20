#netsh wlan show profiles
#netsh wlan show profile "Iphone do joaop" key = clear

import subprocess

informacoes = subprocess.check_output(["netsh","wlan","show","profiles"],encoding='cp860')
print(informacoes)

nome_wifi =  "Marcelo 5G"
informacoes = subprocess.check_output(["netsh","wlan","show","profile",nome_wifi,"key","=","clear"],encoding='cp858')
print(informacoes)

for linha in informacoes.split("\n"):
    if "Conteúdo da Chave" in linha:
        pos = linha.find(":")
        senha = linha[pos+2:]
        print(senha)