lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('\033[36mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado! Não vou adicionar.\033[m')
    ask = ' '
    while ask not in 'SN':
        ask = str(input(f'Quer continuar? [S/N]: ')).upper().strip()[0]
        if ask not in 'SN':
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
    if ask == 'N':
        break
lista.sort()
print('-='*30)
print(f'Você digitou os valores {lista}')