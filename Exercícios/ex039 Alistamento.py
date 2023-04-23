from datetime import date
genero = str(input('Gênero: ')).lower()
ano = int(input('\033[33mAno de nascimento: \033[m'))
idade = date.today().year - ano
print('Você tem {} anos.'.format(idade))
if genero == 'homem' and idade < 18:
    print('\033[31mVocê ainda se alistará no exército!\033[m')
    print('\033[33mFaltam {} anos para você se alistar no exército.\033[m'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + 18))
elif genero == 'homem' and idade == 18:
    print('\033[31mEstá na hora de se alistar no exército!\033[m')
elif genero == 'homem' and idade > 18:
    print('\033[33mJá passou do tempo de você se alistar no exército.\033[m')
    print('\033[31mPassou {} anos do prazo de você se alistar.\033[m'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(ano + 18))
elif genero == 'mulher':
    print('\033[31mVocê não precisa se alistar no exército.\033[m')