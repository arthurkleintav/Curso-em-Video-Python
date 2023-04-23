from time import sleep
def cont(i, f, p):
    c = i
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1.5)
    if i < f:
        while c <= f:
            print(c, end=' ')
            sleep(0.5)
            c += p
        print('FIM')
    elif i > f:
        while c >= f:
            print(c, end=' ')
            sleep(0.5)
            c -= p
        print('FIM')

cont(1, 10, 1)
cont(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont(inicio, fim, passo)
