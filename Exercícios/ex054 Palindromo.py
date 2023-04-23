frase = str(input('Digite uma frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de "{}" é "{}".'.format(junto, inverso))
if junto == inverso:
    print('A frase "{}" É um PALÍNDROMO.'.format(frase))
else:
    print('A frase "{}" NÃO É um PALÍNDROMO.'.format(frase))


'''frase = str(input('Digite uma frase: ')).replace(' ', '').lower()
inverso = frase[::-1]
print('Sua frase ao contrário é "{}".'.format(inverso))
if inverso == frase:
    print('Sua frase é Palíndromo.')
else:
    print('Sua frase NÃO é Palíndromo.')'''