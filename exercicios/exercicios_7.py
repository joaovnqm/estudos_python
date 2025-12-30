# Resolvendo exercícios de Python
# Exercício de funções com retorno, e argumentos não nomeados. Multiplicando argumentos e dizendo se o resultado é par ou ímpar.
def multiplicar(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    return "ímpar"

# Testando a função:
numeros = 2, 3, 4, 5
resultado = multiplicar(*numeros)
print(f"Os números fornecidos são: {numeros}. O resultado de sua multiplicação é: {resultado}, que é um número {par_ou_impar(resultado)}")