# Exercício 36 - Aplicando Polimorfismo.
# Aula 234 do curso do professor Otávio Miranda.
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print("Notificação por E-mail: ", self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print("Notificação por SMS: ", self.mensagem)
        return False # Exemplo de que a notificação não está conseguindo ser enviar.

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificação enviada.")

    else:
        print("Notificação não enviada.")

notificacao_email = NotificacaoEmail("Testando o e-mail.")
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS("Testando o SMS.")
notificar(notificacao_sms)