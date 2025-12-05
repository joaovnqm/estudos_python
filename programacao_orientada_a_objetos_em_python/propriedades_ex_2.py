# Estudando e aplicando as propriedades na classe Pessoa, que terá também propriedades computadas.
# que são atributos que não são armazenados diretamente no disco ou memória, mas calculados dinamicamente.
class Pessoa:
    def __init__(self, nome, ano_de_nascimento):
        self._nome = nome
        self._ano_de_nascimento = ano_de_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_de_nascimento
    
# Utilizando as propriedades e obtendo a idade do usuário através de cálculos dinâmicos, ou seja
# sem guarda-la na memória ou no disco.
pessoa = Pessoa("João", 2004)
print(pessoa.nome)
print(pessoa.idade)