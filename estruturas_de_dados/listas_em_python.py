# Aprendendo sobre listas em Python e alguns métodos úteis.
# Forma mais comum de declarar uma lista.
frutas = ["Laranja", "Pera", "Uva", "Maçã"]
frutas = [] # Lista vazia.

# Criando uma lista com o constrytor list().
letras = list("Python") # Esse método cria uma lista com cada caractere da string como um elemento.
numeros = list(range(5)) # Cria uma lista com números de 0 a 4.

# Criando uma lista com elementos de tipos diferentes.
carro = ["Wolkswagen", "Fusca", 1980, "Azul", 1.0]

# Exibindo valores através do acesso direto.
frutas = ["Laranja", "Pera", "Uva", "Maçã"]
print(frutas[0]) # Acessa o primeiro elemento.
print(frutas[-1]) # Acessa o último elemento.

# Criando listas aninhadas/bidimensionais/matrizes. (Listas dentro de listas)
matriz = [
    [1, "a", 3],
    ["b", 5, 6],
    [7, 8, "c"]
]
print(matriz) # Exibe a matriz completa.
print(matriz[1]) # Exibe a segunda lunha da matriz.
print(matriz[0][1]) # Acessa o elemento "a".
print(matriz[2][2]) # Acessa o elemento "c".

# Aplicando o fatiamento em listas.
print(frutas[2:]) # A partir do índice 2 até o final.
print(frutas[:3]) # Do início até o índice 3 (não incluso).
print(frutas[1:3]) # Do índice 1 até o índice 3.
print(frutas[-3:]) # Últimos 3 elementos.
print(frutas[0:3:2]) # Do índice 0 ao 3, pulando de 2 em 2.
print(frutas[::]) # Exibe a lista completa.
print(frutas[::-1]) # Inverte a lista.

# Iterando lista com loop for.
for fruta in frutas:
    print(fruta)

# Utilizando o enumerate para obter o índice e o valor.
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice} - Fruta: {fruta}")

# Usando listas para criar uma nova lista. (Versão 1)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Utilizando a compreensão de listas para criar uma nova lista. (Versão 2)
pares = [numero for numero in numeros if numero % 2 == 0]

# Modificando elementos da lista.
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

###### Métodos úteis para listas.
# lista.append(x) - Adiciona um item ao final da lista.
frutas.append("Banana")
print(frutas)

# lista.copy() - Retorna uma cópia rasa da lista.
frutas_nova = frutas.copy()
print(frutas_nova) # Exibe a cópia da lista frutas.

# lista.clear() - Remove todos os itens da lista.
frutas_exemplo = frutas_nova
frutas_exemplo.clear()
print(frutas_exemplo) # Exibe lista vazia.

# lista.count(x) - Retorna o número de vezes que o valor x aparece na lista.
numeros_exemplo = [1, 2, 2, 3, 4, 2, 5]
print(numeros_exemplo.count(2)) # Retorna 3.

# lista.extend(iterável) - Extende a lista adicionando todos os itens do iterável.
linguagens = ["Python", "Java"]
print(linguagens)
linguagens.extend(["C++", "JavaScript", "C#"])
print(linguagens)

# lista.index(x) - Retorna o índice do primeiro item cujo valor é x.
print(linguagens.index("JavaScript")) # Retorna 3.
print(linguagens.index("Python")) # Retorna 0.

# lista.insert(i, x) - Insere um item na posição i.
linguagens.insert(2, "Ruby") # Insere "Ruby" na posição 2.
print(linguagens)

# lista.pop([i]) - Remove o item na posição i e o retorna. Se nenhum índice for especificado, remove e retorna o último item.
linguagens.pop() # Remove o último item.
linguagens.pop(1) # Remove o item na posição 1 (Java).
print(linguagens)

# lista.remove(x) - Remove o primeiro item da lista cujo valor é x.
linguagens.remove("C++") # Remove "C++" da lista.
print(linguagens)

# lista.reverse() - Inverte os elementos da lista.
linguagens.reverse()
print(linguagens)
linguagens.reverse() # Voltando à ordem original.

# lista.sort(key = x, reverse = bool) - Ordena os itens da lista in place (no local).
mais_numeros = [5, 2, 9, 1, 5, 6]
mais_numeros.sort() # Ordena em ordem crescente.
print(mais_numeros)
mais_numeros.sort(reverse=True) # Ordena em ordem decrescente.
print(mais_numeros)
mais_numeros.sort(key=lambda x: len(x)) # Ordena pela quantidade de dígitos (caso sejam strings).
print(mais_numeros)
mais_numeros.sort(key=lambda x: len(x), reverse=True) # Ordena pela quantidade de dígitos em ordem decrescente.

# lista.len() - Retorna o número de itens na lista.
print(len(linguagens)) # Exibe o tamanho da lista linguagens.

# lista.sorted(iterável, key = x, reverse = bool) - Retorna uma nova lista ordenada a partir do iterável.
nova_ordenada = sorted(mais_numeros) # Ordena em ordem crescente.
print(nova_ordenada) # Funciona igual ao mais_numeros.sort(), mas retorna uma nova lista.