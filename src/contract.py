from src.utils import separete_by_keyword
import re
cpf = separete_by_keyword("portador")

member_actions = {}

def coletingMemberShares():
    for line in cpf:
        mainLine = line[0]
        comma_of_name = mainLine.find(",") #Virgula que vem logo apos o nome
        dot_of_name = mainLine.find(".") #Ponto depois dos numeros das listas
        name = mainLine[dot_of_name+2:comma_of_name:1]
        shares = r'(\d+)\s+cota'
        matches_share = re.findall(shares, mainLine)
        member_actions[name] = {
            "cotas" : matches_share[0]
        }
    return member_actions

