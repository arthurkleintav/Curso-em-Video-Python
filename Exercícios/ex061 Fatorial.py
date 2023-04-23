num = int(input('Digite um número: '))
resultado = 1
print('{}! = '.format(num), end='')
for n in range(num, 0, -1):
    resultado *= n
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
print(resultado)

'''numero = int(input('Digite um número: '))
c = numero
f = 1
print('{}! = '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''


