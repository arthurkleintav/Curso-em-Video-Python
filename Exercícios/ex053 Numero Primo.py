num = int(input('Digite um número: '))
primo = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[36m', end=' ')
        primo += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if primo == 2:
    print('\n\033[m{} É um número Primo.'.format(num))
else:
    print('\n\033[m{} NÃO é um número Primo.'.format(num))