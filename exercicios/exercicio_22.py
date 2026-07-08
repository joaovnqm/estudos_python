# Exercício 22 - Utilizando JSON
# Utilizando JSON para salvar dados em um arquivo.
import json
caminho_arquivo = 'A:\\Projetos\\Estudos\\estudos_python\\exercicios\\arquivos\\'
caminho_arquivo += 'pessoa.json'

# Criando um dicionário que contém os dados de uma pessoa.
pessoa = {
    "name": "João",
    "age": 22,
    "nationality": "Brazilian",
    "state": "Pernambuco",
    "city": "Recife",
    "addresses": [
        {"address 1": "Rua dos Limões"},
        {"address 2": "Número 8"},
    ],
    "height": 1.85,
    "is_developer": True
}

# Passando os dados do dicionário para um arquivo .json
with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

# Lendo os dados do arquivo .json e imprimindo o nome da pessoa.
with open(caminho_arquivo, "r", encoding="utf8") as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa["name"])