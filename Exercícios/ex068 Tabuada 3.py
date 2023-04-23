while True:
    num = int(input('Tabuada de: '))
    if num < 0:
        print('Programa encerrado. Volte sempre!')
        break
    print('-=-'*10)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-=-'*10)