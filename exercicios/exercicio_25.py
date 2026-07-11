# Exercício 25 - Métodos de Classe, Factory, Métodos Estáticos e Properties
# Criando uma classe de um sistema hipotético de cadastro
class Usuario:
    def __init__(self, nome, username, email):
        self.nome = nome
        self.username = username
        self.email = email
    
    @classmethod
    def usuario_anonimo(cls, username, email):
        return cls("Anonimo", username, email)

    @staticmethod
    def bem_vindo():
        return "Bem-vindo ao sistema!"
    
    # Usando uma property como um getter
    @property
    def nome(self):
        return self.nome

usuario_1 = Usuario("João", "joao.macedo97", "email@exemplo.com")
usuario_2 = Usuario.usuario_anonimo("OAnonimo", "anonimo@exemplo.com")

print(usuario_1.nome, usuario_1.bem_vindo())
print(usuario_2.nome, usuario_2.bem_vindo())