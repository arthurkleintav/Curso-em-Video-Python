lista = []
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    cont += 1
    while True:
        ask = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if ask not in 'SN':
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
        else:
            break
    if ask == 'N':
        break
print('-='*30)
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')