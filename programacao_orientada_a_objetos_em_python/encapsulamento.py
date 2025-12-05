# Estudos de encapsulamento
# O encapsulamento do Python é realizado através da aplicação de convenções realizadas pela equipe de desenvolvimento
# que deve usar o "_" antes de variáveis que devem ser utilizadas no contexto privado.
# Aplicando o que foi aprendido em uma aplicação bancária.
# Criando a classe "Conta".
class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self.nro_agencia = nro_agencia
        self._saldo = float(saldo)
    
    # Criando métodos que acessem a variável "_saldo" que é privada por conta do uso do "_" dada a convenção.
    def mostrar_saldo(self):
        print(f"O seu saldo é de: R${self._saldo}")

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito no valor de: R${self._saldo} efetuado.")
    
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print("Saque efetuado.")
        else: 
            print("Saque indisponível, consulte seu saldo e tente novamente.")

conta = Conta("0001", 100)
conta.mostrar_saldo()
conta.depositar(400)
conta.mostrar_saldo()
conta.sacar(500)
conta.sacar(100)
