# Exercícios de Python do curso do professor Otávio Miranda.
# Exercício: Utilizando os métodos split, join e strip em strings.

frase = "Um feliz Natal e um próspero 2026 para todos!"
lista_palavras = frase.split()
print(frase, lista_palavras)

# Agora, usando uma vírgula para separar.
frase_2 = "Viva o Natal, Cristo nasceu!"
lista_palavras_2 = frase_2.split(",")
lista_palavras_2_modificada = []
print(frase_2, lista_palavras_2)

# Agora, usando o strip ainda na frase 2.
for i, frase in enumerate(lista_palavras_2):
    lista_palavras_2_modificada.append(lista_palavras_2[i].strip())
    print(lista_palavras_2[i].strip())
    
# Agora, utilizando o join.
frases_unidas = '-'.join(lista_palavras_2_modificada)
print(frases_unidas)

# Exercício da aula 99. Gerando o primeiro dígito de um CPF.
cpf_fornecido = input("Por favor, digite o número do CPF: ")
conjuntos_numeros_cpf = cpf_fornecido.replace("-", ".").split(".")
cpf_modificado = ""
soma = 0
valor_regressivo = 10
for trinca in conjuntos_numeros_cpf[:3]:
    cpf_modificado += trinca

for digito in cpf_modificado:
    soma += (int(digito) * valor_regressivo)
    valor_regressivo -= 1

primeiro_digito = (soma * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

print(primeiro_digito)

resultado_1 = cpf_modificado + str(primeiro_digito)

# Exercício da aula 101. Gerando o segundo dígito de um CPF. (Utilizando os dados do exercício anterior.)
novo_valor_regressivo = 11
nova_soma = 0
for digito in resultado_1:
    nova_soma += (int(digito) * novo_valor_regressivo)
    novo_valor_regressivo -= 1

segundo_digito = (nova_soma * 10) % 11

segundo_digito = segundo_digito if segundo_digito <= 9 else 0

print(segundo_digito)

resultado_2 = resultado_1 + str(segundo_digito)

print(f"O CPF completo retornado é: {resultado_2} logo o número fornecido é de um CPF válido.")