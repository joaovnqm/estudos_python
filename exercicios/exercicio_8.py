# Resolvendo exercícios do curso de Python do professor Otávio Miranda.
# Desenvolvendo um jogo de perguntas e respostas

perguntas = [
    {
        "Pergunta": "Quanto é 5 + 7?",
        "Opcoes": ["10", "11", "12", "13"],
        "Resposta": "12"
    },
    {
        "Pergunta": "Quem foi o primeiro presidente do Brasil?",
        "Opcoes": ["Deodoro da Fonseca", "Getúlio Vargas", "Juscelino Kubitschek", "Pedro II"],
        "Resposta": "Deodoro da Fonseca"
    },
    {
        "Pergunta": "Qual é a capital da França?",
        "Opcoes": ["Berlim", "Madrid", "Paris", "Lisboa"],
        "Resposta": "Paris"
    }
]

acertos = 0

for pergunta in perguntas:
    print(pergunta["Pergunta"])
    for i, opcao in enumerate(pergunta["Opcoes"]):
        print(f"{i + 1}. {opcao}")
    alternativa = int(input("Qual é a opção correta? ")) - 1
    resposta = pergunta["Opcoes"][alternativa]

    if resposta == pergunta["Resposta"]:
        acertos += 1
        print("Parabéns! Você acertou!")
    else:
        print("Oops, você errou...")

if acertos == 0:
    print("Que pena, você não acertou nenhuma pergunta.")
    
elif acertos == len(perguntas):
    print("Incrível! Você acertou todas as perguntas!")

else:  
    print(f"Yaaay! Você terminou o jogo com {acertos} acertos de {len(perguntas)} perguntas.")