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
print()

# Desenvolvendo uma calculadora com as 4 operações básicas.
while True:
    valor_1 = input("Digite o primeiro valor: ")
    valor_2 = input("Digite o segundo valor: ")
    valor_1 = float(valor_1)
    valor_2 = float(valor_2)

    try:
        operacao = input("Digite a operação desejada: ")
        if operacao == "+":
            print("O resultado é:", valor_1 + valor_2)
        
        elif operacao == "-":
            print("O resultado é:", valor_1 - valor_2)
        
        elif operacao == "*":
            print("O resultado é:", valor_1 * valor_2)

        elif operacao == "/":
            print("O resultado é:", valor_1 + valor_2)
        
        else:
            print("Hmmm... Acho que você inseriu uma operação inválida.")
    
    except:
        print("Hmmm... Acho que você digitou algum número inválido.")
    
    sair = input("Você deseja [s]air?").lower().startswith("s")
    if sair:
        print("Programa finalizado, obrigado!")
        break