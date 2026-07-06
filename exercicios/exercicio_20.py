# Exercício 20 - Função Recursiva
# Realizando o texte de funções recursivas com números fatoriais.
def calcula_fatorial(numero):
    if numero <= 1:
        return 1
    
    return numero * calcula_fatorial(numero - 1)

print("O fatorial de 4! é:", calcula_fatorial(4))