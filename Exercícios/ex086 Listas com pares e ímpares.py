numeros = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Lista de números pares: {numeros[0]}')
print(f'Lista de númeors ímpares: {numeros[1]}')
