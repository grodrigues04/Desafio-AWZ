import pandas as pd

from src.sales import get_sales_employees_data

from src.payments import get_incorrect_payments

from src.contract import coletingMemberShares

def generateEmployeeCSV():
    df = pd.DataFrame(get_sales_employees_data())
    df_transposed = df.transpose()  # Coluna vira linha, e linha vira coluna
    df_transposed = df_transposed.rename_axis(
        "Nome do Vendedor"
    ).reset_index()  # Colocando nome a coluna que ficou em branco ao ser transpostada
    df_transposed.to_csv("./data/output-spreadsheets/VendasComissao.csv", index=False)


def generateComissionValidationCSV():
    df = pd.DataFrame(get_incorrect_payments())
    df_transposed = df.transpose()
    df_transposed = df_transposed.rename_axis("Nome do Vendedor").reset_index()
    df_transposed.to_csv("./data/output-spreadsheets/ComissaoCorreta.csv", index=False)

def generateTableOfShares():
    df = pd.DataFrame(coletingMemberShares())
    df_transposed = df.transpose()
    df_transposed = df_transposed.rename_axis("Nome do Sócio").reset_index()
    df_transposed.to_csv("./data/output-spreadsheets/Tabela de Socios.csv", index=False)

    
generateEmployeeCSV()
generateComissionValidationCSV()
generateTableOfShares()
