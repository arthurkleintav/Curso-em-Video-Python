resp = 'S'
cont = soma = media = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um valor: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
media = soma / cont
print('Você digitou {} valores e a média foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
