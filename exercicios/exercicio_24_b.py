# Exercício 24 - Salvando os dados de uma classe em um arquivo JSON e recriando a classe em outro arquivo python.
import json

caminho = "A:\\Projetos\\Estudos\\estudos_python\\exercicios\\arquivos\\carro.json"

class Carro:
    def __init__(self, modelo, cor, marca):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca

def recebe_json():
    with open(caminho, "r", encoding="utf8") as arquivo:
        return json.load(arquivo)


yaris = Carro(**recebe_json())
print(yaris.__dict__)