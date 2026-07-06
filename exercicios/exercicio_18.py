# Exercício 18 - Filter
# Utilizando os dados dos produtos como referência.
from dados_exercicios.produtos import produtos

# Utilizando a função filter para gerar uma nova lista de produtos filtrados com base em seu preço.
novos_produtos = filter(lambda produto: produto['preco'] > 15, produtos)

# Consome o iterador retornado por filter(), exibindo um produto por vez.
for produto in novos_produtos:
    print(f"O produto: {produto['nome']} tem um valor de: ${produto['preco']}")
    input("Pressione enter para exibir o valor do próximo produto.")

novos_produtos = filter(lambda produto: produto['preco'] > 15, produtos)

# Outra forma de exibir os valores do iterador retornado pelo filter(), exibindo em lista.
print(list(novos_produtos))
