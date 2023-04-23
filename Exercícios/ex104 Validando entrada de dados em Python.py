def leiaInt(msg):
    ok = False
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num = int(num)
            ok = True
        else:
            print('\033[31mERRO! Informe um número inteiro válido.\033[m')
            ok = False
        if ok:
            break
    return num
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')
