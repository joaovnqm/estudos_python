# Estruturando funções em Python
def saudacao(nome, cidade): # Essa função irá exibir uma saudação personalizada com base nos valores inseridos.
    print(f"Olá, meu nome é {nome} e moro em {cidade}.")

saudacao("João", "Recife") # Chamada da função.

# Função com valor padrão para o parâmetro idade.
def apresentacao(nome, idade=18):
    print(f"Meu nome é {nome} e tenho {idade} anos.")
apresentacao("Maria", 25) # Chamada da função com idade personalizada.
apresentacao("Pedro") # Chamada da função com idade padrão.

# Função retornando um valor.
def soma(a, b):
    return a + b
total = soma(5, 7)
print(f"A soma é: {total}")

# Função que chama outra função.
def resultado(a, b, operacao):
    resultado_novo = operacao(a, b)
    print(f"O resultado da operação é: {resultado_novo}")

# Aumentando a precisão dos valores inseridos por meio de argumentos nomeados.
def meu_carro(marca, modelo, ano, placa):
    print(f"Meu carro é um {marca} {modelo}, ano {ano}, com placa {placa}.")
meu_carro(marca="Toyota", modelo="Corolla", ano=2020, placa="ABC-1234") # Chamada da função com argumentos nomeados.

# Função com args e kwargs.
def detalhes_pessoa(nome, *args, **kwargs):
    cpf_pessoal = "\n".join(args)
    dados_adicionais = "\n".join([f"{chave}: {valor}" for chave, valor in kwargs.items()])
    print(f"Nome: {nome}\nCPF:\n{cpf_pessoal}\nCaracterísticas:\n{dados_adicionais}")
detalhes_pessoa("Lucas", "123.456.789-00", cabelo = "Cabelo castanho", idade = 30, cidade = "São Paulo")

# Função com parâmetros posicionais obrigatórios.
def meu_carro_novo(modelo, ano, placa, /, cor, marca, combustivel):
    print(f"Meu carro é um {marca} {modelo} {cor}, ano {ano}, com placa {placa} e combustível {combustivel}.")
meu_carro_novo("Civic", 2021, "XYZ-9876", cor="Preto", marca="Honda", combustivel="Gasolina")

# Função com parâmetros somente nomeados.
def informacoes_pessoais(*, nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")
informacoes_pessoais(nome="Ana", idade=28, cidade="Rio de Janeiro")