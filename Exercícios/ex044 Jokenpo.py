from time import sleep
from random import choice
print('\033[33m-=-'*11)
print('Eu irei jogar Jokenpo com você!')
print('-=-'*11)
lista = ['Pedra', 'Papel', 'Tesoura']
maquina = choice(lista)
sleep(1)
print('\033[34mJO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!')
user = str(input('\033[32mVocê: ')).title()
if user != 'Pedra' and user != 'Papel' and user != 'Tesoura':
    print('\033[31mJogada inválida.\033[m')
else:
    print('\033[33mMáquina: {}'.format(maquina))
    sleep(1)
    print('\033[33m-=-' * 20)
    print('\033[mVocê escolheu {} e a máquina escolheu {}.'.format(user, maquina))
    print('\033[33m-=-' * 20, '\033[m')
    sleep(0.5)
    if user == 'Pedra' and maquina == 'Tesoura':
        print('\033[32mParabéns! Você ganhou.')
    elif user == 'Pedra' and maquina == 'Papel':
        print('\033[31mOh não! A máquina venceu.')
    elif user == 'Tesoura' and maquina == 'Papel':
        print('\033[32mParabéns! Você ganhou.')
    elif user == 'Tesoura' and maquina == 'Pedra':
        print('\033[31mOh não! A máquina venceu.')
    elif user == 'Papel' and maquina == 'Pedra':
        print('\033[32mParabéns! Você venceu.')
    elif user == 'Papel' and maquina == 'Tesoura':
        print('\033[31mOh não! A máquina venceu.')
    elif user == maquina:
        print('\033[36mEmpate! Ninguém venceu.')