# Exercício 24 - Salvando os dados de uma classe em um arquivo JSON e recriando a classe em outro arquivo python. 
import json

caminho = "A:\\Projetos\\Estudos\\estudos_python\\exercicios\\arquivos\\carro.json"

class Carro:
    def __init__(self, modelo, cor, marca):
        self.modelo = modelo
        self.cor = cor
        self.marca = marca

    def converter_em_json(self):
        with open(caminho, "w", encoding="utf8") as arquivo:
            json.dump(self.__dict__, arquivo, ensure_ascii=False, indent=2)
            return "Os dados da classes foram salvos em um arquivo JSON com sucesso!"

yaris = Carro("Yaris", "Prata", "Toyota")
print(yaris.converter_em_json())