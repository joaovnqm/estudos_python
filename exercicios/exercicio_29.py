# Exercício 29
# Realizando o exercício proposto no curso do professor Luís Otávio Miranda, aula 220.

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome

    def exibir_dados_do_carro(self):
        print(self.nome, self.motor.nome, self.fabricante.nome)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

carro_1 = Carro("HB20")
motor_1 = Motor("Kappa 1.0")
fabricante_1 = Fabricante("Hyundai")

carro_1.motor = motor_1
carro_1.fabricante = fabricante_1
carro_1.exibir_dados_do_carro()

carro_2 = Carro("i20")
carro_2.motor = motor_1
carro_2.fabricante = fabricante_1
carro_2.exibir_dados_do_carro()