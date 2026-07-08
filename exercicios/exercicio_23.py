# Exercício 23 - Criando uma lista de tarefas que pode desfazer e refazer ações.
# Atividade proposta no curso de Python do professor Luís Otávio Miranda
import json

caminho_json = "A:\\Projetos\\Estudos\\estudos_python\\exercicios\\arquivos\\lista_de_tarefas.json"
tarefas_adicionadas = []
tarefas_removidas = []

def escrever_tarefa(tarefa):
    try:
        with open(caminho_json, "r", encoding="utf8") as arquivo:
            tarefas = list(json.load(arquivo))

    except FileNotFoundError:
        tarefas = []

    tarefas.append(tarefa)

    with open(caminho_json, "w", encoding="utf8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

    tarefas_adicionadas.append(tarefa)

def desfazer_tarefa():
    if tarefas_adicionadas is not None:
        try:
            with open(caminho_json, "r", encoding="utf8") as arquivo:
                tarefas = list(json.load(arquivo))
                tarefa = tarefas.pop()
                tarefas_adicionadas.pop()
                tarefas_removidas.append(tarefa)

            with open(caminho_json, "w", encoding="utf8") as arquivo:
                json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

        except:
            return "Não há tarefas para desfazer."
    
    else:
        return "Não há tarefas para desfazer."

def refazer_tarefa():
    try:
        with open(caminho_json, "r", encoding="utf8") as arquivo:
            tarefas = list(json.load(arquivo))
            tarefa = tarefas_removidas.pop()
            tarefas.append(tarefa)
        
        with open(caminho_json, "w", encoding="utf8") as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)

        tarefas_adicionadas.append(tarefa)

    except:
        return "Não há tarefas para refazer."

def listar_tarefas():
    with open(caminho_json, "r", encoding="utf8") as arquivo:
        tarefas = list(json.load(arquivo))
    
    print(*tarefas, sep=", ")

while True:
    tarefa = input("Escreva se deseja 'desfazer' ou 'refazer' alguma ação. Ou escreva o nome da tarefa a ser adicionada: ").strip().lower()
    if tarefa == "desfazer":
        retorno = desfazer_tarefa()
        if retorno is not None:
            print(retorno)

    elif tarefa == "refazer":
        retorno = refazer_tarefa()
        if retorno is not None:
            print(retorno)

    else:
        escrever_tarefa(tarefa)
    
    listar_tarefas()
    print()