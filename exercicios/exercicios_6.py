# Exercícios de Python do curso do professor Otávio Miranda.
# Exercício: Utilizando os métodos split, join e strip em strings.

frase = "Um feliz Natal e um próspero 2026 para todos!"
lista_palavras = frase.split()
print(frase, lista_palavras)
# Agora, usando uma vírgula para separar.
frase_2 = "Viva o Natal, Cristo nasceu!"
lista_palavras_2 = frase_2.split(",")
lista_palavras_2_modificada = []
print(frase_2, lista_palavras_2)
# Agora, usando o strip ainda na frase 2.
for i, frase in enumerate(lista_palavras_2):
    lista_palavras_2_modificada.append(lista_palavras_2[i].strip())
    print(lista_palavras_2[i].strip())
# Agora, utilizando o join.
frases_unidas = '-'.join(lista_palavras_2_modificada)
print(frases_unidas)