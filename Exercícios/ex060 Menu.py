from time import sleep
op = 0
fim = False
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('''Oque quer fazer com os números?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior valor
[ 4 ] Novos números
[ 5 ] Sair do programa.''')
while fim is False:
    op = int(input('>>>> Sua opção: '))
    if op > 5 or op < 1:
        print('\033[31mOpção inválida. Tente novamente:\033[m')
    if op == 1:
        print('\033[32mO resultado de {} + {} é igual a {}.\033[m'.format(n1, n2, n1+n2))
    if op == 2:
        print('\033[32mO resultado de {} x {} é igual a {}.\033[m'.format(n1, n2, n1*n2))
    if op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[32mEntre {} e {}, o maior valor é {}.\033[m'.format(n1, n2, maior))
    if op == 4:
        print('\033[32mInsira novos números: \033[m')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if op == 5:
        sleep(0.5)
        print('-=-' * 5)
        print('\033[33mFinalizando...\033[m')
        print('-=-' * 5)
        sleep(1)
        print('\033[32mPrograma encerrado com sucesso. Volte sempre!\033[m')
        fim = True
