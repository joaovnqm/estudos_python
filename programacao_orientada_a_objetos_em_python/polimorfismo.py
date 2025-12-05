# Estudando e aplicando polimorfismo em herança.
class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

# Alterando o método "voar" na classe Avestruz.
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa.")

# Não utilizar classes com diferenças exageradas como Aviao e Passaro.
class Aviao(Passaro):
    def voar(self):
        print("O avião está decolando.")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(Aviao())