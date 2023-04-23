from ex109 import moeda

valor = float(input('Digite um valor: R$'))
print(f'Aumentando 10% de {valor} fica {moeda.aumentar(valor, 10, True)}')
print(f'A metade de {valor} é {moeda.metade(valor, True)}')
print(f'O dobro de {valor} é {moeda.dobro(valor, True)}')
