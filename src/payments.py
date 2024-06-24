from src.sales import get_sales_employees_data
from src.utils import parse_to_number, read_spreadsheets


def get_incorrect_payments():
    df_payments = read_spreadsheets("Pagamentos")

    incorrect_payments = {}

    for index, row in df_payments.iterrows():
        seller_name = row["Nome do Vendedor"]
        preliminary_commission = row["Comissão"]
        preliminary_commission_number = parse_to_number(preliminary_commission)
        oficial_comission = get_sales_employees_data()[seller_name][
            "Comissão a Receber"
        ]
        if oficial_comission != preliminary_commission_number:
            incorrect_payments[seller_name] = {
                "Valor recebido": f"{preliminary_commission_number}",
                "Valor Correto": f"R${oficial_comission}",
            }
    return incorrect_payments
