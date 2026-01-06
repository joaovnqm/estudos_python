# Resolvendo exercícios do curso de Python do professor Otávio Miranda.
# Exercício de list comprehension, onde devemos criar uma lista com os quadrados dos números pares de 1 a 20.
# Estou optando por inserir um "if" dentro da list comprehension para praticar seu uso nesse contexto. Estou ciente da possibilidade
# de resolver o exercício sem o "if", através da atualização do range para range(2, 21, 2).

lista = [x ** 2 for x in range(2,21) if x % 2 == 0]
print(lista)

# Exercício de dictionary comprehension.
# Criar um dicionário onde as chaves são números de 1 a 10 e os valores são os cubos desses números.
# "x" são as chaves e "y" são os valores.
dicionario = {x: x ** 3 for x in range(1, 11)}
print(dicionario)