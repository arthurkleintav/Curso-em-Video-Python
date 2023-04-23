from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('\nAo total tivemos {} pessoas maiores de idade\n'
      'E tivemos {} pessoas menores de idade.'.format(maior, menor))
