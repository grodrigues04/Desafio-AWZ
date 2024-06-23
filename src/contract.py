from src.utils.separeteByKeyWord import sepateByKeyWord
import re
cpf = sepateByKeyWord("CPF")

member_actions = {}

for line in cpf:
    mainLine = line[0]
    comma_of_name = mainLine.find(",") #Virgula que vem logo apos o nome
    dot_of_name = mainLine.find(".") #Ponto depois dos numeros das listas
    name = mainLine[dot_of_name+2:comma_of_name:1]
    
    shares = r'(\d+)\s+cotas'
    matches = re.findall(shares, mainLine)
    shares = [int(match) for match in matches]
    member_actions[name] = shares

