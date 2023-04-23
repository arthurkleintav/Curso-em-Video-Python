from time import sleep

color = {'clear': '\033[m',
         'green': '\033[1;30;42m',
         'blue': '\033[1;30;44m',
         'white': '\033[1;30;107m',
         'cyan': '\033[1;30;46m',
         'red': '\033[1;30;41m'}

def escreva(msg, cor = 'clear'):
    tam = len(msg) + 4
    print(f'{color[f"{cor}"]}~' * tam)
    print(f'  {msg}')
    print('~' * tam,)
    print(color['clear'], end='')

# Programa Principal
while True:
    escreva('SISTEMA DE AJUDA PyHelp', cor='green')
    fb = str(input('Função ou biblioteca > '))
    if fb.upper() == 'FIM':
        escreva('Até logo!', cor='red')
        break
    escreva(f'Acessando manual do comando {fb}', 'blue')
    sleep(1)
    print(color['white'])
    help(fb)
    print(color['clear'],end='')
