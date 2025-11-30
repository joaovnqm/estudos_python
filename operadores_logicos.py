# Nesse código, vou praticar o uso de operadores lógicos em Python.
saldo = 300
saque = float(input("Digite o valor que deseja sacar: "))
limite_saque = 500
tem_credito = True
if (saldo >= saque):
    print("Saque autorizado: Você possui saldo suficiente.")
elif (saque <= limite_saque and tem_credito == True):
    print("Saque autorizado: Você possui limite de saque e crédito disponível.")

# Algumas negações lógicas.
contatos_emergencia = []

not 1000 > 1500
print(not 1000 > 1500)
# Retorna true, porque a expressão 1000 > 1500 é falsa.

not contatos_emergencia
print(not contatos_emergencia)
# Retorna true, se a variável contatos_emergencia estiver vazia ou for None.

not "saque 1500"
print(not "saque 1500")
# Retorna false, porque a string "saque 1500" é considerada verdadeira em um contexto booleano.

not ""
print(not "")
# Retorna true, porque uma string vazia é considerada falsa em um contexto booleano.

