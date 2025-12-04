# É um conjunto não ordenado de pares chave-valor, onde as chaves são únicas em uma dada instância
# do dicionário. Eles são delimitados por chaves {} e contém uma lista de pares chave:valor serapada por vírgulas.
# Guarda valores mutáveis ou imutáveis de qualquer tipo, mas as chaves devem ser imutáveis.
# Exemplo de dicionário 1:
pessoa = {"nome": "João", "idade": 21, "cidade": "Recife"}

# Exemplo de dicionário 2:
pessoa = dict(nome="João", idade=21, cidade="Recife")

# Adicionando valores no dicionário.
pessoa["telefone"] = "123456789"

# Acessando valores no dicionário.
print(pessoa["nome"])  # Resultado: João

# Dicionários também podem ser aninhados, ou seja, um dicionário conter outr dicionário.
contatos = {
    "pessoa1": {"nome": "João", "telefone": "123456"},
    "pessoa2": {"nome": "Maria", "telefone": "987654"},
    "pessoa3": {"nome": "Pedro", "telefone": "456789"},
}

# Acessando valores em dicionários aninhados.
print(contatos["pessoa2"]["telefone"])  # Resultado: 987654

# Iterando sobre chaves e valores do dicionário.
for chave in contatos:
    print(chave, contatos[chave])

# Forma alternativa de iterar sobre chaves e valores do dicionário.
for chave, valor in contatos.items():
    print(chave, valor)

# Métodos úteis para o dicionário.
# dict.copy() - Retorna uma cópia rasa do dicionário.
exemplo_pessoa_1 = pessoa.copy()

# dict.clear() - Remove todos os itens do dicionário.
exemplo_pessoa_1.clear()

# dict.fromkeys() - Cria um novo dicionário com chaves de um iterável e valores padrão.
exemplo_pessoa_2 = dict.fromkeys(["nome", "idade", "cidade"]) # Valores padrão são None.
print(exemplo_pessoa_2)  # Resultado: {'nome': None, 'idade': None, 'cidade': None}
exemplo_pessoa_3 = dict.fromkeys(["nome", "idade", "cidade"], "Desconhecido") # Valores padrão são "Desconhecido".
print(exemplo_pessoa_3)  # Resultado: {'nome': 'Desconhecido', 'idade': 'Desconhecido', 'cidade': 'Desconhecido'}

# dict.get() - Retorna o valor para a chave especificada. Se a chave não existir, retorna None (ou valor padrão se fornecido).
# Caso peça dados de uma chave não existente como no seguinte comando: print(pessoa[email])
#, ocorrerá um erro. Já com o get(), não ocorrerá erro.
print(pessoa.get("nome"))  # Resultado: João
print(pessoa.get("email"))  # Resultado: None
print(pessoa.get("email", "Chave não encontrada"))  # Resultado: Chave não encontrada

# dict.items() - Retorna uma visão dos pares chave-valor do dicionário.
print(contatos.items())

# dict.keys() - Retorna uma visão das chaves do dicionário.
print(contatos.keys())

# dict.pop() - Remove a chave especificada e retorna o valor correspondente.
resultado = pessoa.pop("idade")
print(resultado)  # Resultado: 21
resultado = pessoa.pop("idade", "Chave não encontrada")  # A chave "idade" já foi removida.
print(resultado)  # Resultado: Chave não encontrada

# dict.popitem() - Remove e retorna um par chave-valor arbitrário do dicionário.
par_removido = pessoa.popitem()
print(par_removido)  # Resultado: ('cidade', 'Recife') (pode variar)

# dict.setdefault() - Retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor padrão fornecido.
idade = pessoa.setdefault("idade", 30)  # A chave "idade" não existe mais, então será adicionada.
print(idade)  # Resultado: 30

# dict.update() - Atualiza o dicionário com pares chave-valor de outro dicionário ou de um iterável de pares.
pessoa.update({"cidade": "São Paulo"})  # Atualiza o valor da chave "cidade".
print(pessoa)  # Resultado

# dict.values() - Retorna uma visão dos valores do dicionário.
print(pessoa.values())

# Verificando a existência de uma chave no dicionário.
resultado = "nome" in pessoa
print(resultado)  # Resultado: True
resultado = "email" in pessoa
print(resultado)  # Resultado: False

# Retirando valores do dicionário com o método del.
del pessoa["cidade"] # Remove a chave "telefone" do dicionário.
del contatos["pessoa3"] # Remove o dicionário associado à chave "pessoa3".
print(contatos)