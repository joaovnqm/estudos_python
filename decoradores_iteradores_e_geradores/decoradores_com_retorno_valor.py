# Criando um decorador com retorno.
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar.")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar.")
        return resultado
    return envelope

@meu_decorador
def ola_mundo(nome, idade):
    print(f"Olá {nome}, você tem {idade} anos.")
    return nome.upper()

resultado = ola_mundo("João", 21)
print(resultado)
