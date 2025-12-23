# Exercícios de Python do curso do professor Otávio Miranda.
# Exercício: Exibindo os índices da lista.

# Exibindo o índice através de um método rudimentar.
lista = ["João Victor", "Rafael", "Anna", "Marcos"]
indice = 0

for nome in lista:
    print(indice, " - ", nome)
    indice += 1

# Exibindo o índice através de um método melhorado.
indices = range(len(lista))

for i in indices:
    print(i, " - ", lista[i])
    
# Exibindo o índice através de um método eficiente.

for novo_indice, nome in enumerate(lista):
    print(novo_indice, " - ", nome)