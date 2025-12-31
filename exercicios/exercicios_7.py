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

# Realizando outro exercício:
# Função que duplica, triplica e quadruplica um número utilizando closures.
def criar_multiplicador(multiplicador):
    def multiplicar_numero(numero):
        return numero * multiplicador
    return multiplicar_numero

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))