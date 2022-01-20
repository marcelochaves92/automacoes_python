from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dolar")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação euro")
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",",".")


tabela = pd.read_excel(r"C:\Users\marce\OneDrive\Área de Trabalho\Intensivão de Python - Hashtag\Aula 3\Produtos.xlsx")
tabela.loc[tabela["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro","Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro","Cotação"] = float(cotacao_ouro)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela.to_excel(r"C:\Users\marce\OneDrive\Área de Trabalho\Intensivão de Python - Hashtag\Aula 3\Tabela com preço atualizado.xlsx", index=False)