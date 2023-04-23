peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
IMC = peso / (altura * altura)
print('Seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('\033[31mVocê está Abaixo do peso!\033[m')
elif IMC < 25:
    print('\033[33mVocê está no peso Ideal!')
elif IMC < 30:
    print('\033[32mVocê está em Sobrepeso.\033[m')
elif IMC < 40:
    print('\033[31mVocê está Obeso!\033[m')
elif IMC > 40:
    print('\033[31mObesidade Mórbida\033[m')
