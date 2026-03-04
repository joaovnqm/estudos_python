# Realizando o exercício de somar listas em Python da aula 173 do curso do professor Luiz Otávio Miranda 

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma_listas(lista_1, lista_2):
    intervalo = min(len(lista_1), len(lista_2))
    return [(lista_1[i] + lista_2[i]) for i in range(intervalo)]

print(soma_listas(lista_a, lista_b))

# Também pode ser construído através de List Comprehension
soma_lista = [x + y for x, y in zip(lista_a, lista_b)]
print(soma_lista)