import pandas as pd
from src.sales import get_sales_employees_data
from src.utils.converterToInt import converterToInt

def get_incorrect_payments():
    try:
        path_payments = "./data/spreadsheets/Vendas - Pagamentos.csv"
        df_payments = pd.read_csv(path_payments)
    except FileNotFoundError:
        print('O arquivo de pagamentos näo foi encontrado.')
        return

    incorrect_payments = {}
    try:
        for index, row in df_payments.iterrows():
            seller_name = row["Nome do Vendedor"]
            preliminary_commission = row["Comissão"]
            preliminary_commission_int = converterToInt(preliminary_commission)
            oficial_comission = get_sales_employees_data()[seller_name]["Comissão a Receber"]
            if oficial_comission != preliminary_commission_int:
                incorrect_payments[seller_name] = {
                    "Valor recebido": f"{preliminary_commission}",
                    "Valor Correto": f"R${oficial_comission}",
                }
    except KeyError as e:
        print(f"Coluna nâo encontrada: {e}")
        print("Verifique as colunas da planilha de pagamentos")
        return 
    return incorrect_payments
