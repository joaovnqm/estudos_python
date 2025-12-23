# Exercícios de Python do curso do professor Otávio Miranda.
# Exercício: Exibindo os índices da lista.
import os

# Exibindo o índice através de um método rudimentar.
lista_1 = ["João Victor", "Rafael", "Anna", "Marcos"]
indice = 0

for nome in lista_1:
    print(indice, " - ", nome)
    indice += 1

# Exibindo o índice através de um método melhorado.
indices = range(len(lista_1))

for i in indices:
    print(i, " - ", lista_1[i])
    
# Exibindo o índice através de um método eficiente.

for novo_indice, nome in enumerate(lista_1):
    print(novo_indice, " - ", nome)

# Introdução ao empacotamento e ao desempacotamento.
lista_2 = ["João Victor", "Rafael", "Anna", "Marcos"]
nome_1, nome_2, nome_3, nome_4 = lista_2
print(nome_1)

# Exercício: Lista de compras com listas.
def exibir_lista(lista_compras):
    print("* * * * * * * * * * Minha Lista de Compras * * * * * * * * * *")
    for indice, nome_produto in enumerate(lista_compras):
        print(indice, nome_produto)

lista_compras = []
while True:
    opcao = input("Selecione uma opção: [I]nserir [A]pagar [L]istar ")

    if opcao == "I" or "i":
        os.system('cls')
        exibir_lista(lista_compras)
        nome_produto = input("Digite o nome do produto que você deseja inserir na lista de compras: ")   
        lista_compras.append(nome_produto)
    
    elif opcao == "A" or "a":
        os.system('cls')
        exibir_lista(lista_compras)
        nome_produto = input("Digite o nome do produto que você deseja apagar da lista de compras: ")
        lista_compras.remove(nome_produto)

    elif opcao == "L" or "l":
        os.system('cls')
        exibir_lista(lista_compras)
    else:
        print("Desculpe, você inseriu um caracterer incorreto, tente novamente.")