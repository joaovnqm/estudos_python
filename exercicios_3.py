# Realizando exercícios de Python. (Laços de Repetição)
linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        if linha != coluna:
            print("*", end="")
        else:
            print("#", end="")
        coluna += 1
    linha += 1
    print("", end="\n")
    coluna = 1

# Realizando outro exercício de laços de repetição. (Iterando os caracteres de um nome)
nome = "João Victor"
comprimento_nome = len(nome)
indice = 0
print(f"O nome escrito é: {nome}")
while indice < comprimento_nome:
    print(f"*", nome[indice], sep="", end="")
    indice += 1