from datetime import date
ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('\033[31mO atleta tem {} anos, então é um atleta MIRIM.\033[m'.format(idade))
elif idade <= 14:
    print('\033[32mO atleta tem {} anos, então é um atleta INFANTIL.\033[m'.format(idade))
elif idade <= 19:
    print('\033[33mO atleta tem {} anos, então é um atleta JUNIOR.\033[m'.format(idade))
elif idade <= 25:
    print('\033[34mO atleta tem {} anos, então é um atleta SENIOR.\033[m'.format(idade))
elif idade > 25:
    print('\033[36mO atleta tem {} anos, então é um atleta MASTER.\033[m'.format(idade))
