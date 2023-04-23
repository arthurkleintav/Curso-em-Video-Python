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


