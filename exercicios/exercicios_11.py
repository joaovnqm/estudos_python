# Resolvendo exercícios do curso de Python do professor Otávio Miranda.
# Importando dados de exemplo.
from copy import deepcopy
from dados_exercicios import produtos

# Aumente os preços dos produtos em 10%
# Gere novos_produtos por deep copy (cópia profunda) e atualize os preços utilizando list comprehension.

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} for p in deepcopy(produtos)
]

print(*novos_produtos, sep='\n', end='\n \n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

novos_produtos.sort(key=lambda item: item['nome'], reverse=True)
print(*novos_produtos, sep='\n', end='\n \n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos.sort(key=lambda item: item['preco'])
print(*novos_produtos, sep='\n', end='\n \n')

# Exercício - Adiando execução de funções
def criar_funcao(funcao, x):
    def funcao_interna(y):
        return funcao(x, y)
    return funcao_interna

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10), multiplica_por_dez(10))

# Refatorando o exercício anterior utilizando o @ (decoradores) com parâmetros.
def criar_decorador(x):
    def criar_funcao(funcao):
        def funcao_interna(y):
            return funcao(x, y)
        return funcao_interna
    return criar_funcao

@criar_decorador(5)
def soma(x, y):
    return x + y

@criar_decorador(10)
def multiplica(x, y):
    return x * y

soma_com_cinco = soma(10)
multiplica_por_dez = multiplica(10)

print(soma_com_cinco, multiplica_por_dez)