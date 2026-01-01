# Resolvendo exercícios do curso de Python do professor Otávio Miranda.
# Exercício envolvendo o "set" da aula 133. O primeiro número que é repetido em uma lista de inteiros deve ser retornado.
# Caso não haja números repetidos, deve ser retornado -1.

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def primeiro_duplicado(lista_de_argumentos):
    for lista in lista_de_argumentos:
        valores_unicos = set(lista)
        repeticoes = dict.fromkeys(valores_unicos, 0)
        ciclos = 0
        for valor in lista:
            ciclos += 1
            repeticoes[valor] += 1
            if repeticoes[valor] > 1:
                print(f"O número {valor} foi o primeiro a se repetir.")
                break
            elif ciclos == len(valores_unicos):
                print("Não há números repetidos na lista. Retorno: -1")
                break
        
primeiro_duplicado(lista_de_listas_de_inteiros)