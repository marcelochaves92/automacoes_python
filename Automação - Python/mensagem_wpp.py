import pandas as pd
import urllib
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contatos_df = pd.read_excel(r"C:\Users\marce\OneDrive\Documentos\Automação - Python\Enviar.xlsx")

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)
    
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i,"Pessoa"]
    numero = contatos_df.loc[i,"Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
        
    navegador.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)