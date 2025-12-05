# Estudando herança múltipla criando classes.
class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
    def __str__(self):
        return f"{self.__class__}: {", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"

# Criando classe filha.
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

# Classes Mixins que não afetam diretamente as classes filhas.
class MiarMixin:
    def miar(self):
        return "Miau!"

# Criando classe com herança múltipla. 
class Gato(Mamifero, MiarMixin):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

gato = Gato(nro_patas = 4, cor_pelo = "Branco")
print(gato)
print(gato.miar())

ornitorrinco = Ornitorrinco(cor_pelo = "Vermelho", cor_bico = "Laranja", nro_patas = 2)
print(ornitorrinco)