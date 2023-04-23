from random import randint
maior = menor = cont = cont1 = 0
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram', end=' ')
for n in num:
    cont += 1
    if cont < 5:
        print(n, end=', ')
    else:
        print(n, end='.')
    cont1 += 1
    if cont1 == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'\nO maior valor foi {maior} e o menor valor foi {menor}.')
