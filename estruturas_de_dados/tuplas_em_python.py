# Estudando e praticando tuplas em Python.
# Tuplas são estruturas de dados imutáveis que podem armazenar múltiplos valores. Ou seja, são constantes.
frutas = tuple(['maçã', 'banana', 'laranja']) # Criando uma tupla usando o construtor tuple().
mais_frutas = ("abacaxi", "uva", "manga",) # Criando uma tupla usando parênteses.
letras = tuple("Python") # Tupla com cada caractere da string como um elemento.
pais = ("Brasil",) # Tupla com um único elemento (vírgula é obrigatória).

# Acessando elementos da tupla.
print(frutas[0]) # Acessa o elemento na posição 0, que é a "maçã".
print(mais_frutas[-1]) # Acessa o último elemento, que é a "manga".

# Tuplas aninhadas (tuplas dentro de tuplas). Tuplas podem armazenar todos os tipos de dados, inclusive outras tuplas.
matriz = (
    ("a", 1, 2),
    (3, "b", 4),
    (5, 6, "c"),
)
print(matriz[1]) # Exibe a segunda linha da matriz.
print(matriz[0][1]) # Acessa o elemento "1".

# Aplicando fatiamento em tuplas. (igual às listas)
print(frutas[1:]) # A partir do índice 1 até o final.
print(mais_frutas[:2]) # Do início até o índice 2 (não incluso).
print(mais_frutas[1:3]) # Do índice 1 até o índice 3 (não incluso).

# Iterando tuplas com loop for. (Ou seja, percorrendo cada elemento da tupla)
for fruta in frutas:
    print(fruta)

# Utilizando o enumerate para obter o índice e o valor.
for indice, fruta in enumerate(mais_frutas):
    print(f"Índice: {indice} - Fruta: {fruta}")

# Como as tuplas são imutáveis, o número de métodos disponíveis é limitado.
###### Métodos úteis para tuplas.
# tupla.count(x) - Retorna o número de vezes que o valor x aparece na tupla.
numeros = (1, 2, 2, 3, 4, 2, 5,)
print(numeros.count(2)) # Exibe 3, pois o número 2 aparece 3 vezes na tupla.

# tupla.index(x) - Retorna o índice da primeira ocorrência do valor x na tupla.
print(numeros.index(3)) # Exibe 3, que é o índice do número 3 na tupla.

# tupla.len() - Retorna o número de elementos na tupla.
print(len(frutas)) # Exibe 3, que é o número de elementos na tupla frutas.


