cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = -1
    ask = ' '
    while num < 0 or num > 20:
        num = int(input('Digite um número entre 0 e 20: '))
        if num < 0 or num > 20:
            print('Tente novamente.')
        else:
            print(f'Você digitou o número {cont[num]}.')
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N] ')).upper().strip()
        if ask not in 'SN':
            print('Tente novamente.')
    if ask == 'N':
        break
