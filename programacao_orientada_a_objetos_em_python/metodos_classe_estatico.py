# Aplicando métodos de classe e estáticos.
class Pessoa:
    def __init__(self , nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

pessoa = Pessoa("João", 21)
print(pessoa.nome, pessoa.idade)

pessoa_nova = Pessoa.criar_apartir_data_nascimento(2000, 5, 28, "Marcos")
print(pessoa_nova.nome, pessoa_nova.idade)

print(pessoa.maior_idade(18))