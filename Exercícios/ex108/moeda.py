def aumentar(p, t):
    resp = p + (p * t / 100)
    return resp

def diminuir(p, t):
    resp = p - (p * t / 100)
    return resp

def metade(p):
    resp = p / 2
    return resp

def dobro(p):
    resp = p * 2
    return resp

def moeda(p = 0, m = 'R$'):
    return f'{m}{p:.2f}'.replace('.', ',')


