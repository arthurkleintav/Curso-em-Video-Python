numero = int(input('Digite um número: '))
print('Escolha um conversor: ')
print('''[1] = Binário
[2] = Octal
[3] = Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao >= 4:
    print('\033[31mEscolha uma opção válida.\033[m')
else:
    if opcao == 1:
        print('\033[32mO número {} em Binário é {}.\033[m'.format(numero, bin(numero)[2:]))
    elif opcao == 2:
        print('O número {} em Octal é {}.'.format(numero, oct(numero)[2:]))
    elif opcao == 3:
        print('O número {} em Hexadecimal é {}'.format(numero, hex(numero)[2:]))