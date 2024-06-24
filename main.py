import pandas as pd

from src.sales import get_sales_employees_data

from src.payments import get_incorrect_payments

from src.contract import coletingMemberShares


def generateEmployeeCSV():
    print("Iniciando geração da planilha de comissão...")
    df = pd.DataFrame(get_sales_employees_data())
    df_transposed = df.transpose()  # Coluna vira linha, e linha vira coluna
    df_transposed = df_transposed.rename_axis(
        "Nome do Vendedor"
    ).reset_index()  # Colocando nome a coluna que ficou em branco ao ser transpostada
    df_transposed.to_csv("./data/output-spreadsheets/VendasComissao.csv", index=False)
    print("Planilha de comissões gerada com sucesso\n")


def generateComissionValidationCSV():
    print("Iniciando a geração da planilha de validação de pagamentos...")
    df = pd.DataFrame(get_incorrect_payments())

    df_transposed = df.transpose()
    df_transposed = df_transposed.rename_axis("Nome do Vendedor").reset_index()
    df_transposed.to_csv("./data/output-spreadsheets/ComissaoCorreta.csv", index=False)
    print("Planilha de validação de pagamentos gerada com sucesso\n")


def generateTableOfShares():
    print("Iniciando geração da planilha de quadro de socios...")
    df = pd.DataFrame(coletingMemberShares())
    df_transposed = df.transpose()
    df_transposed = df_transposed.rename_axis("Nome do Sócio").reset_index()
    df_transposed.to_csv("./data/output-spreadsheets/Tabela de Socios.csv", index=False)
    print("Planilha de quadro de socios gerada com sucesso\n")


def main():
    try:
        generateEmployeeCSV()
        generateComissionValidationCSV()
        generateTableOfShares()
    except Exception:
        print("Ocorreu um problema. Verifique seus arquivos")
        return
    print("Planilhas geradas com sucesso!")


if __name__ == "__main__":
    main()
