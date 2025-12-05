# Estudando e praticando atributos de classe.
class Estudante:
    escola = "Escola Einstein" # É um atributo de classe.

    def __init__(self, nome, matricula):
        self.nome = nome # É um atributo de instância.
        self.matricula = matricula # É um atributo de instância.

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno_1 = Estudante("João", 1)
aluno_2 = Estudante("Erika", 2)

mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Escola Tesla" # Modifica o valor do atributo em todos os objetos dessa classe.

aluno_3 = Estudante("Everton", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)