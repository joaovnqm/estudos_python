# Criando um "for" para iterar sobre cada letra de um texto fornecido pelo usuário.
texto = input("Digite um texto: ")
VOGAIS = "aeiouAEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    else: print()

# Utilizando o range em um "for" para exibir números de 1 a 100 em mútiplos de 5.
for numero in range(5, 101, 5):
    print(numero, end=" ")

# Utilizando o while em um contexto de uma máquina bancária.
opcao = -1
saldo = 1000
while opcao != 0:
    opcao = int(input("\nDigite a opção desejada:\n1 - Ver saldo\n2 - Fazer saque\n0 - Sair\n"))
    if opcao == 1:
        print(f"Seu saldo é R$ {float(saldo)}")
    elif opcao == 2:
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")
else:
    print("Obrigado por utilizar nosso sistema bancário. Até logo!")

for numero in range(10000):
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")
    
    
    