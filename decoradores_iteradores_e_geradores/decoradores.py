# Funções que chamam funções.
def mensagem(nome):
    print("Executando nome")
    return f"Oi {nome}."

def mensagem_longa(nome):
    print("Executando mensagem longa.")
    return f"Olá, tudo bem com você {nome}?"

def executar(funcao, nome):
    print("Executando função...")
    return funcao(nome)

print(executar(mensagem, "João"))
print(executar(mensagem_longa, "João"))

# Funções internas.
def principal():
    print("Executando a função principal.")

    def funcao_interna():
        print("Executando a função interna.")

    def funcao_interna_2():
        print("Executando a segunda função interna.")

    funcao_interna()
    funcao_interna_2()

principal()

# Retorno de função.
def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def subtracao(a, b):
        return a - b
    
    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b
    
    def potencia(a, b):
        return a ** b
    
    if operacao == "+":
        return soma
    elif operacao == "-":
        return subtracao
    elif operacao == "*":
        return multiplicacao
    elif operacao == "/":
        return divisao
    elif operacao == "**":
        return potencia
    
print(calculadora("*")(50000, 50000))

# Decoradores.
def meu_decorador(funcao):
    def envelope():
        print("Faz isso antes de executar.")
        funcao()
        print("Faz isso depois de executar.")

    return envelope

def ola_mundo():
    print("Olá mundo!")

# Decorando uma função em Python
@meu_decorador
def ola_mundo():
    print("Olá mundo!")
# Como pode ser feito de forma menos habilidosa: ola_mundo = meu_decorador(ola_mundo)
ola_mundo()