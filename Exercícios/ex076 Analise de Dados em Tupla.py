num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite outro valor: ')))
print(f'Os valores digitados foram {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece pela primeira vez na posição {num.index(3) + 1}')
else:
    print('O número 3 não aparece nenhuma vez.')
print('Os valores pares são',end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
