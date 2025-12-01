# Testando estruturas condicionais com múltiplas condições.
# Criando uma função chamada sacar que utiliza if, elif e else. Além de praticar as estrutura de identação corretas.
def sacar(valor:float):
    saldo = 300
    limite_saque = 500
    tem_credito = True
    conta_normal = True
    conta_universitaria = False
    if conta_normal:
        # Criando um "if" aninhado.
        if (saldo >= valor):
            return "Saque autorizado: Você possui saldo suficiente."
        elif (valor <= limite_saque and tem_credito == True):
            return "Saque autorizado: Você possui limite de saque e crédito disponível."
        else:
            return "Saque não autorizado: Saldo insuficiente e/ou limite de saque excedido."
    elif conta_universitaria:
        if (saldo >= valor):
            return "Saque autorizado: Você possui saldo suficiente."
        else:
            return "Saque não autorizado: Saldo insuficiente para conta universitária."
    else:
        return "Tipo de conta inválido. Entre em contato com o suporte."
    
# Testando a função sacar.
print(sacar(200))

# Aplicando if ternário.
valor_deposito = 150
print("Depósito bem-sucedido." if valor_deposito > 100 else "Depósito falhou.")