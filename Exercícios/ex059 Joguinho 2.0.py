from random import randint
print('\033[36m-=-'*28)
print('Eu irei pensar em um número entre 1 e 10. Tente adivinhar! (Máximo: 5 Tentativas.)')
print('-=-'*28, '\033[m')
rnd = randint(1, 10)
escolha = ''
palpites = 0
while escolha != rnd and palpites != 5:
    escolha = int(input('\033[33mSua escolha: \033[m'))
    palpites += 1
    if escolha > 10 or escolha < 1:
        print('\033[31mInsira um valor válido.\033[m')
    else:
        if escolha > rnd and palpites != 5:
            print('\033[31mMenos! Tente novamente.\033[m')
        elif escolha < rnd and palpites != 5:
            print('\033[31mMais! Tente novamente.\033[m')
        elif escolha != rnd and palpites == 5:
                print('\033[31mVocê perdeu! O número era {}.\033[m'.format(rnd))
if escolha == rnd:
    print('\033[36mVocê venceu! Você precisou de {} palpites para vencer.'.format(palpites))
