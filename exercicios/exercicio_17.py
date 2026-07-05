# Exercício 17 - Função map
# Nesse exercício, irei aplicar a função map para alterar os preços de uma lista de produtos, aplicando um aumento de 10% no valor de cada produto.
from dados_exercicios.produtos import produtos

def mudar_preco_de_produto(produto):
    return {
        **produto, 'preco': aumentar_dez_porcento(produto['preco'])
    }

def aumentar_dez_porcento(produto):
    return round(produto * 1.1, 2)

produtos_com_desconto = list(map(mudar_preco_de_produto, produtos))

for produto in produtos_com_desconto:
    print(produto['nome'], produto['preco'])