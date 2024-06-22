import pandas as pd

from sales import sales_employees_data, sales_directory_data
from payments import incorrect_payments

def generateEmployeeCSV():
    sales_employees_data["manager"] = sales_directory_data["manager"]
    sales_employees_data["marketing_team"] = sales_directory_data["marketing_team"]
    df = pd.DataFrame(sales_employees_data)
    df_transposed = df.transpose() #Coluna vira linha, e linha vira coluna
    df_transposed = df_transposed.rename_axis("Nome do Vendedor").reset_index() # Colocando nome a coluna que ficou em branco ao ser transpostada
    df_transposed.to_csv("./data/output-spreadsheets/VendasComissao.csv",index=False)

def generateComissionValidationCSV():
    df = pd.DataFrame(incorrect_payments)      
    df_transposed = df.transpose() 
    df_transposed = df_transposed.rename_axis("Nome do Vendedor").reset_index() 
    df_transposed.to_csv("./data/output-spreadsheets/ComissaoCorreta.csv",index=False)
    
generateEmployeeCSV()
generateComissionValidationCSV()

