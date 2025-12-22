# Nesse código, eu farei uma atividade proposta no curso de Python do professor Otávio Miranda.
# Laços de Repetição.
import os

palavra_secreta = "perfume"
letras = ""
tentativas = 0
print(
    "Olá, bem-vindo ao jogo da Palavra Secreta. " \
    "Tente adivinhar a palavra secreta inserindo cada letra por vez. " \
    "Bom jogo!")
 
while True:
    letra = input("Qual a letra que você quer tentar? ")
    if len(letra) == 1:
        tentativas += 1

        if letra in letras:
            print("Você já descobriu essa letra, tente novamente.")

        elif letra in palavra_secreta:
            letras += letra
            palavra_formada = ""
            for letra_na_palavra in palavra_secreta:
                if letra_na_palavra in letras:
                    palavra_formada += letra_na_palavra
                    print(letra_na_palavra, sep="", end="")
                else:
                    palavra_formada += "*"
                    print("*", sep="", end="")
            print("")

            if palavra_formada == palavra_secreta:
                print(f"Parabéns! Você descobriu a palavra secreta: {palavra_secreta}"\
                      f"O seu número de tentativas foi: {tentativas}")
                input("Aperte 'Enter' para jogar novamente.")
                os.system('cls')
                tentativas = 0
                letras = ""
                palavra_formada = ""

        else:
            print("Oops, essa letra não está presente na palavra secreta, tente novamente.")
            tentativas += 1
    
    else:
        print("Por favor, digite apenas uma letra.")