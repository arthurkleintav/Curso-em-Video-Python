real = float(input('Dinheiro na carteira: R$'))
dolar = real / 5.22
euro = real / 5.63
libra = real / 6.43
iene = real / 0.041
bitcoin = real / 108821.06
print('Com {} você poderá comprar:'.format(real))
print('${:.2f}'.format(dolar))
print('€{:.2f}'.format(euro))
print('£{:.2f}'.format(libra))
print('¥{:.2f}'.format(iene))
print('₿{:.4f}'.format(bitcoin))
