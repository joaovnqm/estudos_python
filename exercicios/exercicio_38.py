# Exercício 38 - Funções decoradoras e decoradores com classes - Baseado na aula do curso do professor Otávio Miranda.
def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr

def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls

def minha_cidade(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'Recife' in resultado:
            return 'Você está em casa.'

        return resultado
    
    return interno
@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Cidade:
    def __init__(self, nome):
        self.nome = nome

    @minha_cidade
    def falar_nome(self):
        return f'O nome da cidade é: {self.nome}'

brasil = Time('Brasil')
argentina = Time('Argentina')
recife = Cidade('Recife')
sao_paulo = Cidade('São Paulo')

print(brasil)
print(argentina)
print(recife)
print(sao_paulo)

print(recife.falar_nome())
print(sao_paulo.falar_nome())