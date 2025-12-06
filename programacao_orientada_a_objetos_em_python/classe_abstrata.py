# Estudando e aplicando classes abstratas.
# Chamando os módulos para a criação da classe abstrata e seus métodos.
from abc import ABC, abstractmethod

# Criando a classe abstrata com seus métodos abstratos.
class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca():
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando!")
    def desligar(self):
        print("Desligando...")
    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado!")
    def desligar(self):
        print("Desligando o ar condicionado...")
    @property
    def marca(self):
        return "Daikin"

controle = ControleTV()
controle.ligar()
controle.desligar()