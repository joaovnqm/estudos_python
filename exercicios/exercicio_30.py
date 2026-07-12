# Exercício 30 - Herança, Super e Sobreposição de Membros
# Desenvolvendo um sistema de estacionamento de exemplo com diferentes tipos de acesso.

class Pessoa:
    def __init__(self, nome, idade, placa_do_carro):
        self.nome = nome
        self.idade = idade
        self.placa_do_carro = placa_do_carro
    
    def bem_vindo(self):
        print(f"Bem-vindo {self.nome}, é bom ter você aqui!")

    def pagar_estacionamento(self):
        return

class Cliente(Pessoa):
    def __init__(self, nome, idade, placa_do_carro, forma_de_pagamento):
        super().__init__(nome, idade, placa_do_carro)
        self.forma_de_pagamento = forma_de_pagamento

    def pagar_estacionamento(self):
        print(f"O carro de placa: {self.placa_do_carro} está com o estacionamento pago.")

class Colaborador(Pessoa):
    def __init__(self, nome, idade, placa_do_carro, tempo_de_vinculo):
        super().__init__(nome, idade, placa_do_carro)
        self.tempo_de_vinculo = tempo_de_vinculo

    def pagar_estacionamento(self):
        print("O acesso ao estacionamento é gratuito para funcionários, prossiga.")

cliente_1 = Cliente("João", 22, "QYO2B98", "Cartão")
colaborador_1 = Colaborador("Marcos", 30, "QBO8X27" , 2)

cliente_1.bem_vindo()
cliente_1.pagar_estacionamento()
colaborador_1.bem_vindo()
colaborador_1.pagar_estacionamento()