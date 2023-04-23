def leiaDin(msg):
    ok = False
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO! "{valor}" não é um número válido.\033[m')
        else:
            ok = True
            valor = float(valor)
            return valor
        if ok:
            break