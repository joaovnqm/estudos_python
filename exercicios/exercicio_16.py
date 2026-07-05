# Exercício 16 - Groupby
# Nesse exercício, vamos utilizar a função groupby do módulo itertools para agrupar alunos de uma universidade com base em suas notas.
from itertools import groupby
from dados_exercicios.alunos_universidade import alunos

# Criando uma função para ordenar os alunos por nota
def ordenar_por_nota(aluno):
    return aluno['nota']

# Agrupando os alunos por nota através da função groupby. É necessário ordenar os alunos antes de agrupá-los.
alunos_agrupados = sorted(alunos, key=ordenar_por_nota)
grupos = groupby(alunos_agrupados, key=ordenar_por_nota)

# Imprimindo os alunos por grupo de nota.    
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno['nome'])