# Exercício 19 - Reduce
# O reduce() faz a redução de um iterável em um valor.
from functools import reduce
from dados_exercicios.produtos import produtos

# Função que será utilizada para reduzir a lista de produtos em um valor total
def funcao_soma_valor_total(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

# Reduzindo a lista de produtos em um valor total
total = reduce(funcao_soma_valor_total, produtos, 0)

print('O total é: ', total)