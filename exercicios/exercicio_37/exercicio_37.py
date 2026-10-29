# Exercício 37 - Utilizando Context Manager - Baseado na aula do curso do professor Otávio Miranda.
from pathlib import Path
class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        parent = Path(__file__).parent
        self.caminho_arquivo = parent / caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO O ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO O ARQUIVO')
        self._arquivo.close()

with MyContextManager('exercicio_37.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)