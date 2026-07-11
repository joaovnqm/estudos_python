# Exercício 26 - Relações entre classes: Associação
# Nesse exercício, vou associar duas classes, uma sendo a classe escritor e a outra sendo a ferramenta utilizada.

class Escritor:
    def __init__(self, nome):
        self._nome = nome
        self._ferramenta = None

    @property
    def nome(self):
        return self._nome
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @nome.setter
    def nome(self, nome):
        print("hey!")
        self._nome = nome

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

    def escrever(self):
        if self._ferramenta:
            print(f"{self._nome} está escrevendo com um(a) {self._ferramenta.nome}.")
        
        else:
            print(f"{self._nome} não tem uma ferramenta.")

class Ferramenta:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

escritor = Escritor("João")
computador = Ferramenta("Computador")
escritor.ferramenta = computador
print(escritor.nome, escritor.ferramenta.nome)
escritor.escrever()
