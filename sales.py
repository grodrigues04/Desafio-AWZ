import pandas as pd
from settings import get_settings

path_sales = "./data/spreadsheets/Vendas - Vendas.csv"
df_sales = pd.read_csv(path_sales)
#dataframe = varias series formam um dataframe
#series = itens associados a colunas (1,y)

sales_employees_data = {}

#commission
for index, row in df_sales.iterrows(): #para cada linha, nome da coluna e valor das linhas x's
    sales_data = row["Data da Venda"]
    seller_name = row["Nome do Vendedor"]
    
    if seller_name not in sales_employees_data:
        sales_employees_data[seller_name] = {
            "Comissão Total": 0,
            "Comissão a Receber": 0 
        }
    sale_value = row["Valor da Venda"]
    sale_value_int = (int(sale_value.replace("R$","").replace(" ","").replace(",","").replace(".","")))/100
    sales_channel = row["Canal de Venda"]
    raw_commission = sale_value_int * get_settings().employee_commission #Total commission
    manager_commission = 0
    marketing_commission = 0
    sales_employees_data[seller_name]["Comissão Total"] += raw_commission
    
    if raw_commission >= get_settings().manager_commission:
        manager_commission = raw_commission * get_settings().manager_commission
    
    if sales_channel == "Online": 
        marketing_commission = raw_commission * get_settings().marketing_commission

    commission_fee = manager_commission + marketing_commission
    commission = raw_commission - commission_fee
    
    sales_employees_data[seller_name]["Comissão a Receber"] += commission
    
#Colocar uma coluna para marketing, e uma para manager separado das outras. Acho que fica mais claro dessa maneira