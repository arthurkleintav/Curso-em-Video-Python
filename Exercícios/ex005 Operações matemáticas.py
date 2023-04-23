n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
print('A soma é {:.2f}, a subtração é {:.2f}, a multiplicação é {:.2f}, a divisão é {:.2f},'.format(s, sub, m, d))
print('a potência é {:.2f} e a divisão inteira é {:.2f}'.format(e, di))