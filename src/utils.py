import re

import pandas as pd


def read_spreadsheets(tab):
    try:
        path = "./data/spreadsheets/Vendas.xlsx"
        data = pd.read_excel(path,sheet_name=tab)
        return data
    except FileNotFoundError:
        error_message = f"O arquivo de {tab} näo foi encontrado."
        print(error_message)
        raise FileNotFoundError(error_message)

def parse_to_number(comission):
    if isinstance(comission, (int, float)):
        return comission
    digits = re.findall(r"\d+", comission)
    joined_digits = "".join(digits)
    float_comission = int(joined_digits) / 100

    return float_comission





def separete_by_keyword(keyword):
    contract_path = "./data/contract/Partnership.txt"
    with open(contract_path, 'r') as file:
    # Read the content of the file
        content = file.read()
    
    document_lines= content.splitlines() #Cada linha do documento e separada
    all_lines = []
    for line in document_lines:
        linha = []
        if keyword in line:
            linha = [line]
            all_lines.append(linha)
    return all_lines

