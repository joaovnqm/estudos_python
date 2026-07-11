# Exercício 27 - Agregação
# Usando uma relação entre um carrinho de compras e uma lista de produtos.

class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.valor for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.valor)
        
        print()
    
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

carrinho = CarrinhoDeCompras()
produto_1, produto_2 = Produto("Lápis", 3), Produto("Resma de Papel", 10)
carrinho.inserir_produtos(produto_1, produto_2)
carrinho.listar_produtos()
print(carrinho.total())