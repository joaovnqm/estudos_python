#Criando uma lista de compras para ajudar o Renato

lista_compras = []
while True:
    i = 0
    resposta = input("Deseja adicionar um item? (s/n): ").lower().strip()
    if resposta == "s":
        item = input("Digite o nome do item: ")
        lista_compras.append(item)
        i += 1
        break

    elif resposta == "n":
        break
    else: 
        print("Opção inválida! Por favor, digite 's' para sim ou 'n' para não. ")

if i >= 1:
    while True:
        resposta = input("Deseja adicionar outro item? (s/n): ").lower().strip()
        if resposta == "s":
            item = input("Digite o nome do item: ")
            lista_compras.append(item)
            i += 1
        else: 
            break