# Exercício do livro: Entendendo Algoritmos.
# Questão 4.1 - Escreva um código para a função soma (Uma função recursiva que some cada elemento do array).
def soma(array):
    if len(array) <= 1:
        return array[0]
    
    else:
        return array.pop() + soma(array)

print(soma([5, 10, 25, 37]))

# Questão 4.2 - Escreva uma função recursiva que conte o número de itens de uma lista.
def conta_lista(lista):
    if len(lista) <= 1:
        return 1

    else:
        lista.pop()
        return 1 + conta_lista(lista)

print(conta_lista(["a", "b", "c", "d", "e", "f"]))

# Questão 4.3 - Encontre o valor mais alto em uma lista.
def valor_mais_alto(lista, valor_alto=0):
    if len(lista) <= 1:
        valor = lista.pop()
        if valor > valor_alto:
            return valor

        else: 
            return valor_alto

    else:
        valor = lista.pop()
        if valor > valor_alto:
            valor_alto = valor
            return valor_mais_alto(lista, valor_alto)

        else:
            return valor_mais_alto(lista, valor_alto)

print(valor_mais_alto([50, 100, 60, 600, 80, 20, 602, 850, 10, 30, 900, 30, 70, 50]))
