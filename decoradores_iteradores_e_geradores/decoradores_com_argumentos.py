# Criando um decorador com argumentos.
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar.")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar.")
    
    return envelope

@meu_decorador
def ola_mundo(nome, idade):
    print(f"Olá {nome}, você tem {idade} anos!")

ola_mundo("João", 21)