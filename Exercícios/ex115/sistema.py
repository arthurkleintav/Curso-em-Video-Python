from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        lerArquivo('curso.txt')
        sleep(1)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif resp == 3:
        cabecalho('Saindo do programa... Até logo! ;)')
        sleep(0.5)
        break
    else:
        print('\033[31mERRO! Por favor, digite uma opção válida.\033[m')
        sleep(1)
