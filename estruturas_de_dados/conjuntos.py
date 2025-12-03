# Eliminando registros duplicados com o método set().
numeros = set([1, 2, 2, 3, 4, 4, 5]) # Resultado: {1, 2, 3, 4, 5}
print(numeros)

frutas = set(["maçã", "banana", "laranja", "maçã", "uva", "banana"])
print(frutas) # Resultado: {'maçã', 'banana', 'laranja', 'uva'}

carros = set(["Celta", "Gol", "Fusca", "Celta", "Palio"])
print(carros) # Resultado: {'Celta', 'Gol', 'Fusca', 'Palio'}

linguagens = {"Python", "Java", "C++", "Python", "JavaScript"} # Outra forma de criar um conjunto.
print(linguagens) # Resultado: {'Python', 'Java', 'C++', 'JavaScript'}

# Iterando sobre um conjunto com loop for.
for fruta in frutas:
    print(fruta)

# Usando o enumerate para obter índice e valor.
for indice, linguagem in enumerate(linguagens):
    print(f"Índice: {indice} - Linguagem: {linguagem}")

# Utilizando métodos de conjuntos (sets).
# {}.union() - Retorna a união de dois conjuntos.
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
uniao = conjunto_a.union(conjunto_b)
print(uniao) # Resultado: {1, 2, 3, 4,

# {}.intersection() - Retorna a interseção de dois conjuntos.
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao) # Resultado: {3}

# {}.difference() - Retorna a diferença entre dois conjuntos.
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca) # Resultado: {1, 2}

# {}.symmetric_difference() - Retorna a diferença simétrica entre dois conjuntos.
diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica) # Resultado: {1, 2, 4, 5}

# {}.issubset() - Verifica se um conjunto é subconjunto de outro.
print({1, 2}.issubset(conjunto_a)) # Resultado: True
print({4, 5}.issubset(conjunto_a)) # Resultado: False

# {}.issuperset() - Verifica se um conjunto é superconjunto de outro.
print(conjunto_a.issuperset({1, 2})) # Resultado: True
print(conjunto_a.issuperset({4, 5})) # Resultado: False

# {}.isdisjoint() - Verifica se dois conjuntos são disjuntos (não possuem elementos em comum).
print(conjunto_a.isdisjoint(conjunto_b)) # Resultado: False
print({6, 7}.isdisjoint(conjunto_a)) # Resultado: True

# {}.add() - Adiciona um elemento ao conjunto.
conjunto_a.add(6)
conjunto_a.add(3) # Adicionando um elemento já existente não altera o conjunto.
print(conjunto_a) # Resultado: {1, 2, 3, 6}

# {}.copy() - Retorna uma cópia do conjunto.
copia_conjunto = conjunto_a.copy()
print(copia_conjunto) # Resultado: {1, 2, 3, 6}

# {}.remove() - Remove um elemento do conjunto. Gera erro se o elemento não existir.
conjunto_a.remove(2)
print(conjunto_a) # Resultado: {1, 3, 6}

# {}.discard() - Remove um elemento do conjunto. Não gera erro se o elemento não existir.
conjunto_a.discard(4) # O 4 não existe, mas não gera erro.

# {}.clear() - Remove todos os elementos do conjunto.
conjunto_b.clear()
print(conjunto_b) # Resultado: set()

# {}.pop() - Remove o primeiro elemento do conjunto e o retorna.
elemento_removido = conjunto_a.pop()
print(elemento_removido) # Exibe o elemento removido.
print(conjunto_a) # Exibe o conjunto após a remoção.

# {}.len() - Retorna o número de elementos no conjunto.
print(len(frutas)) # Exibe o número de elementos no conjunto frutas.

# {}.sorted() - Retorna uma lista com os elementos do conjunto ordenados.
print(sorted(linguagens)) # Exibe a lista ordenada das linguagens.

# {}.in() - Verifica se um elemento está presente no conjunto.
print("maçã" in frutas) # Resultado: True