# Exercício 15 - Combinations, Permutations e Product
# Dados com base na sorveteria, vamos criar algumas combinações, permutações e produtos de sabores de sorvete.
from itertools import combinations, permutations, product
from dados_exercicios.sorveteria import sabores, tamanhos, calda

# Função para imprimir os elementos de um iterador
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# Combinations: combinações de 2 sabores
print_iter(combinations(sabores, 2))

# Permutations: permutações de 2 sabores
print_iter(permutations(sabores, 2))

# Product: produto cartesiano de sabores, tamanhos e caldas
print_iter(product(*[sabores, tamanhos, calda]))