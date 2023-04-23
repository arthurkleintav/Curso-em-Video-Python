print('\033[36m-=-'*5, end='')
print(' BANCO ', end='')
print('-=-'*5, '\033[m')
valor = int(input('Valor do saque: \033[32mR$\033[m'))
total = valor
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            if ced == 1:
                print(f'\033[32mTotal de {totced} moedas de R${ced}')
            else:
                print(f'\033[32mTotal de {totced} cédulas de R${ced}.\033[m')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if total == 0:
            break
