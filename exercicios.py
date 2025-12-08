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