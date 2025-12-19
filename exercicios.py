# Contruindo uma calculadora de multiplicação:
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

valores = input("Insira os números separados por espaços:")
numeros = [int(numero) for numero in valores.split()]
resultado = multiplicacao(*numeros)
print(resultado)

# Construindo uma aplicação que diz se o número é par ou ímpar:
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("O número é par")
    elif numero % 2 != 0:
        print("O número é ímpar")
    
valor = input("Insira o número:")
par_ou_impar(int(valor))

# Exercício de Cálculo de IMC
nome = "João Victor"
altura = 1.86
peso = 74
imc = peso / altura ** 2

# A seguinte string é uma f-string, pode incluir variáveis dentro dela através do uso das chaves.
print(f"O indivíduo de nome: {nome}, de altura: {altura} e de peso: {peso}, tem um IMC de: {imc:.2f}")

# Outro exercício:
primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor = {primeiro_valor} é maior do que o segundo valor = {segundo_valor}.")

elif segundo_valor > primeiro_valor:
    print(f"O segundo valor = {segundo_valor} é maior do que o primeiro valor = {primeiro_valor}.")

elif primeiro_valor == segundo_valor:
    print(f"O primeiro valor: {primeiro_valor} e o segundo valor: {segundo_valor} são iguais.")

else:
    print("Um ou os dois valores inseridos são inválidos.")

# Exercício de formatação e fatiamento de Strings.
nome_usuario = input("Por favor, digite o seu nome: ")
idade_usuario = input("Por favor, digite a sua idade: ")

if (nome_usuario and idade_usuario) != None:
    print(f"Seu nome é: {nome_usuario}")
    print(f"Seu nome invertido é: {nome_usuario[::-1]}")
    if " " in nome_usuario:
        print("O seu nome contém espaço(s)")
    else:
        print("O seu nome não contém espaços.")
    print(f"O seu nome contém {len(nome_usuario)} letras e espaços.")
    print(f"A primeira letra do seu nome é: {nome_usuario[0]}")
    print(f"A última letra do seu nome é: {nome_usuario[-1]}")
else:
    print("Desculpe, você deixou um ou os dois campos vazios.")