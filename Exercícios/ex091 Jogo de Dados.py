from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in jogo.items():
    sleep(0.5)
    print(f'{f"{k} tirou {v}":>20}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('Ranking:')
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{f"{i+1} lugar: {v[0]} com {v[1]}":>25}')
