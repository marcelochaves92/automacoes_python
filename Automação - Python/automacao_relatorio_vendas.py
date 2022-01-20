from IPython import display
import pandas as pd
import pyautogui
import pyperclip
import time
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=742, y=50)
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.doubleClick(x=330, y=295)
time.sleep(2)

pyautogui.click(x=385, y=290)
pyautogui.click(x=1165, y=189)
pyautogui.click(x=967, y=600)

time.sleep(5)

tabela = pd.read_excel(r"C:\Users\marce\Downloads\Vendas - Dez.xlsx")

faturamento = tabela["Valor Final"].sum()
qntd_produtos = tabela["Quantidade"].sum()

pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=87, y=202)
pyautogui.write("9marceli@gmail.com")
pyautogui.press("enter")
pyautogui.press("tab")

pyperclip.copy("Relatório de Vendas - Dezembro")
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")

texto = f"""Prezados, bom dia.

O faturamento de ontem foi de R$:{faturamento:,.2f}
A quantidade de produtos vendidos foi de:{qntd_produtos:,}

Att.
Marcelo Chaves"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")

pyautogui.hotkey("ctrl","enter")