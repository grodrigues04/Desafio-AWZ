contract_path = "data\contract\Partnership.txt"

with open(contract_path, 'r') as file:
    # Read the content of the file
    content = file.read()
    
owners_group = {}
document_lines= content.splitlines() #Cada linha do documento e separada


    
