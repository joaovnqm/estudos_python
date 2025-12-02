# Praticando a interpolação de variáveis e fatiamento de strings em Python.
nome = "João Victor"
idade = 21
profissao = "Desenvolvedor"
linguagem = "Python"

dados = {"nome": nome, "idade": idade, "profissao": profissao, "linguagem": linguagem}

# Interpolação de variáveis usando diferentes métodos.
# Interpolação de um jeito antigo.
print("Nome: %s\nIdade: %d\nProfissão: %s\nLinguagem que estuda: %s" % (nome, idade, profissao, linguagem))

# Interpolação mais atual, porém não ideal.
print("Nome: {}\nIdade: {}\nProfissão: {}\nLinguagem que estuda: {}".format(nome, idade, profissao, linguagem))

# Interpolação com chaves porém mais organizada.
print("Nome: {0}\nIdade: {1}\nProfissão: {2}\nLinguagem que estuda: {3}".format(nome, idade, profissao, linguagem))

# Interpolação com chaves porém mais organizada e nomeada.
print("Nome: {nome}\nIdade: {idade}\nProfissão: {profissao}\nLinguagem que estuda: {linguagem}".format(
    nome=nome, idade=idade, profissao=profissao, linguagem=linguagem
))

# Interpolação com dicionário.
print("Nome: {nome}\nIdade: {idade}\nProfissão: {profissao}\nLinguagem que estuda: {linguagem}".format(**dados))

# Interpolação ideal com f-strings.
print(f"Nome: {nome}\nIdade: {idade}\nProfissão: {profissao}\nLinguagem que estuda: {linguagem}")

# Fatiamento de strings.
nome_completo = "João Victor Macêdo"

# Primeiro caractere.
print([nome_completo[0]])

# Do índice 0 ao 3.     
print(nome_completo[:4])

# Do índice 5 ao fim.
print(nome_completo[5:])

# Do índice 5 ao 10.
print(nome_completo[5:11])

# Do índice 5 ao 10 com passo 2.
print(nome_completo[5:11:2])

# Retorna a string normal.
print(nome_completo[:])

# Retorna a string de trás para frente.
print(nome_completo[::-1])

# Outra forma de fatiamento de trás para frente, do índice -1 ao -5.
print(nome_completo[0:-1])

# Strings de Mútiplas Linhas ou Triplas.
print(f"""Olá, meu nome é {nome}.
Tenho {idade} anos
Estou aprendendo {linguagem}.""")