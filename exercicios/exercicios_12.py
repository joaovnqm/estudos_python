# Realizando o exercício de unir listas em Python da aula 171 do curso do professor Luiz Otávio Miranda 
cidades = ["Recife", "São Paulo", "Porto Alegre", "Manaus"]
estados = ["PE", "SP", "RS", "AM", "MT"]
def zipper(lista1, lista2):
    intervalo = min(lista1, lista2)
    return [(lista1[i], lista2[i]) for i in range(intervalo)]

print(zipper(cidades, estados))