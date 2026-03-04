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

# Exercício de set comprehension.
# Criar um conjunto (set) com as letras únicas de uma frase, ignorando espaços.
frase = "Frase de exemplo do exercício de set comprehension."
set = {x for x in frase if x != " "}
print(set)
# A letra maiúscula e o acento são considerados caracteres diferentes de acordo com a tabela Unicode,
# por isso, aparecem dois "i"s, um com o acento agudo e outro sem acento. Poderia acontecer o mesmo caso
# existisse uma letra "f" minúscula na frase.

# Exercício utilizando generator
# Criar um generator que produza os números pares de 1 a 50.
def gerar_numeros_pares(limite):
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            yield numero

pares_generator = gerar_numeros_pares(50)
for par in pares_generator:
    print(par)
    input("Pressione Enter para ver o próximo número par...")