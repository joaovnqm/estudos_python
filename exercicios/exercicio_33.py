# Exercício de Pilhas passado pelo professor Cícero Garrozi.

def verificar_casamento(string):
    pilha = []
    for caractere in string:
        if caractere == "(" or caractere == "[" or caractere == "{":
            pilha.append(caractere)
        
        elif caractere == ")" or caractere == "]" or caractere == "}":
            try:
                valor = pilha.pop()

            except:
                return "casamento imperfeito"
            
            if caractere == ")" and valor == "(":
                continue

            elif caractere == "]" and valor == "[":
                continue

            elif caractere == "}" and valor == "{":
                continue
            
            else:
                return "casamento imperfeito"

    if pilha != []:
        return "casamento imperfeito"
        
    return "casamento perfeito"

string = input()
print(verificar_casamento(string))