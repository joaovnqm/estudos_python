# Nesse arquivo, vou praticar a aplicação de heranças.
# Criando a classe veículo.
class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas
    
    def ligar_motor(self):
        print("Ligando o motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_de_rodas, carregado):
        super().__init__(cor, placa, numero_de_rodas)
        self.carregado = carregado
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} estou carregado.")

moto = Motocicleta("Preta", "ABC-12D4", 2)
moto.ligar_motor()

carro = Carro("Branco", "EFG-12H4", 4)
carro.ligar_motor()

caminhao = Caminhao("Roxo", "IJK-12L4", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
