# Exercício 28 - Composição
# Criando um exemplo de uma relação entre uma pessoa e seu endereço.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

pessoa_1 = Pessoa("João")
pessoa_1.inserir_endereco("Avenida Brasil", 123)
pessoa_1.inserir_endereco("Avenida Boa Viagem", 456)
pessoa_1.listar_enderecos()