# Exercício 21 - Arquivos e Context Manager
# Criando arquivos e manipulando-os
caminho_arquivo = "A:\\Projetos\\Estudos\\estudos_python\\exercicios\\arquivos\\"
caminho_arquivo += 'primeiro_arquivo.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    print("Olá mundo! Oops, quero dizer... Olá arquivo!")
    arquivo.write("Essa é a linha 1.\n")
    arquivo.write("Já essa, é a linha 2.")

with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    print(arquivo.read())