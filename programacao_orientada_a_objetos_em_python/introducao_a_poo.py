# Desenvolvendo o desafio proposto pelo professor Guilherme da DIO.
# Criando a "class" da bicicleta.
class Bicicleta:
    # Construtor do objeto bicicleta.
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Destrutor do objeto bicicleta. Bom para melhorar a eficiência do programa, já que libera a memória utilizada pelo objeto.
    # Porém não é obrigatório já que o próprio Python lida com a memória quando determinada referência não é utilizada.
    # O "Garbage Collection" cuida disso. 
    def __del__(self):
        print("Destruindo a instância...")
    
    # Métodos do objeto bicicleta.
    def buzinar(self):
        print("Plim plim!")

    def parar(self):
        print("Parando a bicicleta.")
        print(f"Bicicleta {self.modelo} parada.")
    
    def correr(self):
        print("Acelerandooooo!")
    
    #def __str__(self): # Forma possível de apresentar o valores mas que exige um maior cuidado na manutenção do código.
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor
        in self.__dict__.items()])}" # Forma ideal para uma melhor manutenção do código.
    
# Criando um objeto bicicleta.
b1 = Bicicleta("Vermelha", "Caloi", 2025, 2000)
b1.buzinar() # = Bicicleta.buzinar(b1)
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Criando outro objeto bicicleta.
b2 = Bicicleta("Azul", "KSW", 2023, 1400)
Bicicleta.correr(b2)
print(b2.cor, b2.modelo, b2.ano, b2.valor)
print(b1.__str__())
