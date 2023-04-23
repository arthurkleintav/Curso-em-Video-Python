totgasto = maismil = maisbarato = cont = nomebarato = 0
print('\033[36m-=-'*8, end=' ')
print('MERCADO', end=' ')
print('-=-'*8, '\033[m')
while True:
    nome = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço do produto: \033[32mR$\033[m'))
    totgasto += preco
    if preco >= 1000:
        maismil += 1
    cont += 1
    if cont == 1 or preco < maisbarato:
        maisbarato = preco
        nomebarato = nome
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if ask not in 'SN':
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
    if ask == 'N':
        print('\033[36m-=-'*8, end=' ')
        print('RESULTADO', end=' ')
        print('-=-'*8, '\033[m')
        break
print(f'\033[33mO total da compra foi de R${totgasto:.2f}.')
print(f'Existem {maismil} produtos custando mais de R$1000.')
print(f'O produto mais barato foi {nomebarato}, custando R${maisbarato:.2f}.\033[m')
