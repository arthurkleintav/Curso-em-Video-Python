from random import randint
from time import sleep
wins = 0
print('\033[36m-=-'*9)
print('Vamos jogar Par ou Impar!')
print('-=-'*9, '\033[m')
while True:
    rnd = randint(1, 10)
    player = 0
    while player < 1 or player > 10:
        player = int(input('Digite um valor: '))
        if player < 1 or player > 10:
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
        if escolha not in 'PI':
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
    tot = rnd + player
    print(f'\nVocê escolheu {player} e eu escolhi {rnd}. O total deu {tot}.')
    if escolha == 'P' and tot % 2 == 0 or escolha == 'I' and tot % 2 != 0:
        print('\033[36mVocê VENCEU! Vamos jogar novamente.\033[m')
        wins += 1
    else:
        print('\033[31mVocê PERDEU!', end=' ')
        print(f'Você conseguiu vencer {wins} vezes.\033[m')
        break