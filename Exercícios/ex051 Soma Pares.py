soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print('A soma dos {} números pares encontrados é {}'.format(cont, soma))
