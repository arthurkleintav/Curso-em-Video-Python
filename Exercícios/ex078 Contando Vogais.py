palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR')
for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for l in p:
        if l in 'AEIOU':
            print(l, end=' ')