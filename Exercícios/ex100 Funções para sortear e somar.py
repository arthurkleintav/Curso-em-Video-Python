from random import randint
from time import sleep
numeros = list()

def sorteia(lista):
    print('Sorteando os valores:', end=' ')
    for c in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=' ')
        sleep(0.5)
    print()

def somapar(lista):
    soma = 0
    print(f'Somando os valores pares de {lista} temos', end=' ')
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)

sorteia(numeros)
somapar(numeros)
