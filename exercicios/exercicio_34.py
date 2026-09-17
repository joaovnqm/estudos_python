# Resolvendo uma questão proposta pelo professor Cícero Garrozi da disciplina de Fundamentos de Problemas Computacionais.
# Questão: Histórico de navegação: Escreva um programa em Python que mantenha o histórico de navegação 
# do usuário em um navegador. O programa deve manter uma pilha de URLs 
# visitados e permitir que o usuário navegue para trás e para frente pressionando teclas 
# específicas. Por exemplo, o usuário pode ter visitado vários sites e o programa deve permitir
# que ele volte para o site anterior pressionando uma tecla.
import os

class Historico_Navegacao:
    def __init__(self, pagina_inicial):
        self.pilha_voltar = []
        self.pilha_avancar = []
        self.url_atual = pagina_inicial

    def visitar_pagina(self, nova_url):
        self.pilha_voltar.append(self.url_atual)
        self.url_atual = nova_url
        self.pilha_avancar.clear()
        print("Acessando a url: ", self.url_atual)

    def voltar(self):
        if not self.pilha_voltar:
            input("Não há páginas para voltar. Aperte qualquer tecla para continuar. . .")
            return

        self.pilha_avancar.append(self.url_atual)
        self.url_atual = self.pilha_voltar.pop()
        print("Voltando para a url: ", self.url_atual)

    def avancar(self):
        if not self.pilha_avancar:
            input("Não há páginas para avançar. Aperte qualquer tecla para continuar. . .")
            return

        self.pilha_voltar.append(self.url_atual)
        self.url_atual = self.pilha_avancar.pop()
        print("Avançando para a url: ", self.url_atual)

    def mostrar_status(self):
        print("Você está na página: ", self.url_atual)

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main():
        navegador = Historico_Navegacao("google.com")
        instrucoes = """
        Comandos disponíveis:
        visitar <url> : Visitar um novo site (ex: visitar github.com)
        voltar        : Voltar
        avançar       : Avançar
        sair          : Sair
        """
        print(instrucoes)

        while True:
            comando = input("Digite um comando: ").strip().lower()
            if comando == 'sair':
                print("Fechando o navegador...")
                break

            elif comando == 'voltar':
                navegador.voltar()
                navegador.limpar_tela()
                print(instrucoes)

            elif comando == 'avançar':
                navegador.avancar()
                navegador.limpar_tela()
                print(instrucoes)

            elif comando.startswith('visitar '):
                nova_url = comando.split(' ', 1)[1]
                navegador.visitar_pagina(nova_url)
                navegador.limpar_tela()
                print(instrucoes)

            else:
                print("Comando inválido!")
                navegador.limpar_tela()
                print(instrucoes)
                
            navegador.mostrar_status()

Historico_Navegacao.main()