# Nesse exercício, irei praticar o uso de funções de entrada e saída em Python.
NOME = input("Digite seu nome: ")
idade = input("Agora, digite sua idade: ")
print(f"Olá, {NOME}! Você tem {idade} anos. Seja bem-vindo ao nosso sistema.")

# Contruindo um exemplo de calculadora simples.
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."

print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")

#Utilizando o end e o sep no print.
print(NOME, idade, resultado, sep=" - ", end="\n-FIM DO PROGRAMA-\n")