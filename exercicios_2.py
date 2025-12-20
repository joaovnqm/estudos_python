# Exercício sobre a aplicação do "Try" e do "Except" em Python.
try:
    numero_dobro = input("Insira um número qualquer e veja o seu dobro: ")
    print(f"O dobro do número {numero_dobro} é: {float(numero_dobro) * 2}")
except:
    print("O que você digitou não é um número e contém algum caractere não esperado como letras ou espaços. " \
    "Por favor, analise e tente novamente.")