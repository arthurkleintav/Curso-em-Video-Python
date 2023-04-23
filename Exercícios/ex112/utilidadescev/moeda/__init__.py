def aumentar(p, t, f = False):
    resp = p + (p * t / 100)
    return resp if f is False else moeda(resp)

def diminuir(p, t, f = False):
    resp = p - (p * t / 100)
    return resp if f is False else moeda(resp)

def metade(p, f = False):
    resp = p / 2
    return resp if f is False else moeda(resp)

def dobro(p, f = False):
    resp = p * 2
    return resp if f is False else moeda(resp)

def moeda(p = 0, m = 'R$'):
    return f'{m}{p:.2f}'.replace('.', ',')

def resumo(p=0, a=25, r=15):
    print('~' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('~' * 30)
    print(f'Preço analisado: \t{moeda(p, "R$")}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True)}')
    print(f'{r}% de redução: \t{diminuir(p, r, True)}')
    print('~' * 30)

