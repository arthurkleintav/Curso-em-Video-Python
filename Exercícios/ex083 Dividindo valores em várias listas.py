lista = []
impar = []
par = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    while True:
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if ask not in 'SN':
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
        else:
            break
    if ask == 'N':
        break
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
