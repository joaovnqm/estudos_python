# Exercícios de Python do curso do professor Otávio Miranda.
# Exercício: Exibindo os índices da lista.

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