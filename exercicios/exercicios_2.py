# Exercício sobre a aplicação do "Try" e do "Except" em Python.
try:
    numero_dobro = input("Insira um número qualquer e veja o seu dobro: ")
    print(f"O dobro do número {numero_dobro} é: {float(numero_dobro) * 2}")
except:
    print("O que você digitou não é um número e contém algum caractere não esperado como letras ou espaços. " \
    "Por favor, analise e tente novamente.")

# Exercício 1 da Aula 55 do Curso do Luiz Otávio Miranda.
numero_inteiro = input("Por favor, digite um número inteiro para saber se ele é par ou ímpar: ")
try:
    if int(numero_inteiro) % 2 == 0:
        print(f"O número: {numero_inteiro} é par.")

    elif int(numero_inteiro) % 2 != 0:
        print(f"O número: {numero_inteiro} é ímpar.")
        
except:
    print("O valor digitado não é um valor inteiro. Por favor, tente novamente.")

# Exercício 2 da Aula 55 do Curso do Luiz Otávio Miranda.
hora_dia = int(input("Por favor, informe a hora do dia: "))
try:
    if hora_dia < 12:
        print("Bom dia.")
    elif hora_dia < 18:
        print("Boa tarde.")
    elif hora_dia < 24:
        print("Boa noite.")
    else:
        print("Hora inválida.")
except:
    print("O valor digitado não é um valor inteiro. Por favor, tente novamente.")

# Exercício 3 da Aula 55 do Curso do Luiz Otávio Miranda.
nome_usuario = input("Por favor, escreva o seu nome: ")
if len(nome_usuario) <= 4:
    print("O seu nome é pequeno.")
elif len(nome_usuario) <= 6:
    print("O seu nome é normal.")
else:
    print("O seu nome é muito grande, uau!")