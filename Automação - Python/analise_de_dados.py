import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r"C:\Users\marce\OneDrive\Área de Trabalho\Intensivão de Python - Hashtag\Aula 2\telecom_users.csv")

tabela = tabela.drop("Unnamed: 0", axis = 1)

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis = 1)
tabela = tabela.dropna(how="any", axis = 0)

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize = True).map("{:.1%}".format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color = "Churn")
    grafico.show()
    
    
#Escreva aqui suas conclusões:
#- Pessoas com familias menores tem mais chance de cancelar
#    - Podemos criar um plano familia para diminuir a taxa de cancelamento
#- Estamos perdendo muitos clientes nos primeiros meses
#    - Tem alguma ação promocional que está trazendo muito cliente desqualificado
#    - Podemos pensar em dar bônus para o cliente nos primeiros meses
#    - A 1ª experiência do cliente pode estar sendo muito ruim
#- Estamos com algum problema na fibra(taxa de cancelamento muito alta)
#- Quanto mais serviços o cliente tem, menor a chance dele cancelar 
#    - Podemos criar uma promoção dando serviço pro cliente ou cobrar muito barato
#- Quase todo cancelamento está no contrato mensal
#    - Dar desconto no contrato anual
#- Evitar boleto eletrônico, dar desconto nas outras opções