from random import randint
from time import sleep
print('\033[0;35m-=-\033[m'*20)
print('\033[0;33mEu irei pensar em um número entre 0 e 5. Tente Adivinhar!\033[m')
print('\033[0;35m-=-\033[m'*20)
numero = randint(0, 5)
escolha = int(input('\nEm qual número pensei? '))
if escolha >= 6:
    print('\033[31mO número deve ser menor ou igual a 5.\033[m')
else:
    print('PENSANDO...')
    sleep(1)
    if escolha == numero:
        print('\033[32mVocê ganhou! O número que pensei foi {}\033[m'.format(numero))
    else:
        print('\033[31mVocê perdeu! O número que pensei foi {}\033[m'.format(numero))





