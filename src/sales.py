from src.config.settings import get_settings
from src.utils import parse_to_number, read_spreadsheets


def get_sales_employees_data():
    df_sales = read_spreadsheets("Vendas")
    sales_employees_data = {}
    # commission
    try:
        for index, row in df_sales.iterrows():
            seller_name = row["Nome do Vendedor"]

            if seller_name not in sales_employees_data:
                sales_employees_data[seller_name] = {
                    "Comissão Total": 0,
                    "Comissão a Receber": 0,
                }
            sale_value = row["Valor da Venda"]
            sale_value_number = parse_to_number(sale_value)
            sales_channel = row["Canal de Venda"]
            raw_commission = (
                sale_value_number * get_settings().employee_commission
            )  # Total commission
            manager_commission = 0
            marketing_commission = 0
            sales_employees_data[seller_name]["Comissão Total"] += raw_commission

            if raw_commission >= get_settings().manager_commission:
                manager_commission = raw_commission * get_settings().manager_commission

            if sales_channel == "Online":
                marketing_commission = (
                    raw_commission * get_settings().marketing_commission
                )

            commission_fee = manager_commission + marketing_commission
            commission = raw_commission - commission_fee

            sales_employees_data[seller_name]["Comissão a Receber"] += commission
    except (KeyError, TypeError) as e:
        error_message = f"Coluna não encontrada: {e}"
        print(error_message)
        raise KeyError(error_message)
    return sales_employees_data
