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