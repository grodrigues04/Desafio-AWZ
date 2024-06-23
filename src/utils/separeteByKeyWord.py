contract_path = "data\contract\Partnership.txt"

with open(contract_path, 'r') as file:
    # Read the content of the file
    content = file.read()

document_lines= content.splitlines() #Cada linha do documento e separada
def sepateByKeyWord(keyword):
    all_lines = []
    for line in document_lines:
        linha = []
        if keyword in line:
            linha = [line]
            all_lines.append(linha)
    return all_lines