# Nesse arquivo, vou demonstrar alguns métodos úteis de manipulação de strings e fatiamento em Python.
curso = "pYTHon"

# Convertendo todas as letras em maiúsculas.
print(curso.upper())

# Convertendo todas as letras em minúsculas.
print(curso.lower())

# Deixando maiscúla apenas a primeira letra.
print(curso.title())

# Agora, eliminando espaços em branco em uma string.
curso = "  pYTHon  "

# Eliminando os espaços em branco.
print(curso.strip())

# Eliminando os espaços em branco apenas à direita.
print(curso.rstrip())

# Eliminando os espaços em branco apenas à esquerda.
print(curso.lstrip())

# Realizando junções e centralizações de strings.
curso = "Python"

# Centralizando a string com um total de 20 caracteres, preenchendo com "*".
print(curso.center(20, "*"))

# Realizando a junção.
print("-".join(curso))
