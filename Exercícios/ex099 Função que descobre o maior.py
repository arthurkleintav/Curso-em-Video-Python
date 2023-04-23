from time import sleep
def maiornum(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        if cont == 0:
            maior = n
        elif n > maior:
            maior = n
        print(n, end=' ')
        cont += 1
        sleep(0.5)
    print(f'\033[36mForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.\033[m')

maiornum(2, 9, 4, 5, 7, 1)
maiornum(4, 7, 0)
maiornum(1, 2)
maiornum(22)
maiornum()
