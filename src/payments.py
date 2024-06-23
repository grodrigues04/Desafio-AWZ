import pandas as pd
from src.sales import get_sales_employees_data


def get_incorrect_payments():
    path_payments = "./data/spreadsheets/Vendas - Pagamentos.csv"
    df_payments = pd.read_csv(path_payments)

    incorrect_payments = {}

    for index, row in df_payments.iterrows():
        seller_name = row["Nome do Vendedor"]
        preliminary_commission = row["Comissão"]
        preliminary_commission_int = (
            int(
                preliminary_commission.replace("R$", "")
                .replace(" ", "")
                .replace(",", "")
                .replace(".", "")
            )
        ) / 100
        oficial_comission = get_sales_employees_data()[seller_name]["Comissão a Receber"]
        if oficial_comission != preliminary_commission_int:
            incorrect_payments[seller_name] = {
                "Valor recebido": f"{preliminary_commission}",
                "Valor Correto": f"R${oficial_comission}",
            }
    return incorrect_payments
