vel = float(input('Digite a velocidade do carro. Km/h: '))
acima = (vel - 80) * 7
if vel > 80:
    print('Seu carro foi multado por ultrapassar o limite de 80Km/h!\nVocê pagará {:.2f}R$ de multa.'.format(acima))
else:
    print('Você não foi multado. Continue sua viagem!')
