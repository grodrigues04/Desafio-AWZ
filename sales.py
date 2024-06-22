import pandas as pd

path_sales = "./data/spreadsheets/Vendas - Vendas.csv"
df_sales = pd.read_csv(path_sales)
#dataframe = varias series formam um dataframe
#series = itens associados a colunas (1,y)

sales_team_data = {
    "marketing_team":0,
    "manager":0
}
#commission
for index, row in df_sales.iterrows(): #para cada linha, nome da coluna e valor das linhas x's
    sales_data = row["Data da Venda"]
    seller_name = row["Nome do Vendedor"]
    
    if seller_name not in sales_team_data:
        sales_team_data[seller_name] = {
            "Comissão Total": 0,
            "Comissão a Receber": 0 
        }
    sale_value = row["Valor da Venda"]
    sale_value_int = (int(sale_value.replace("R$","").replace(" ","").replace(",","").replace(".","")))/100
    sales_channel = row["Canal de Venda"]
    commission = sale_value_int*0.1 #Total comission
    #print(commission)
    sales_team_data[seller_name]["Comissão Total"] += commission
    if commission >= 1.500:
        manager_commission = commission*0.1
        discounted_commission = commission - manager_commission
        sales_team_data["manager"] += manager_commission
    
    if sales_channel == "Online": 
        marketing_comission = commission*0.2
        discounted_commission = commission - marketing_comission
        sales_team_data["marketing_team"] += marketing_comission

    sales_team_data[seller_name]["Comissão a Receber"] += discounted_commission
    
    
df = pd.DataFrame(sales_team_data)

df_transposed = df.transpose() #Coluna vira linha, e linha vira coluna
df_transposed = df_transposed.rename_axis("Nome do Vendedor").reset_index() # Colocando nome a coluna que ficou em branco ao ser transpostada
df_transposed.to_csv("./data/output-spreadsheets/VendasComissao.csv",index=False)