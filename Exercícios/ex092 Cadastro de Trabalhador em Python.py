pessoa = dict()
from datetime import datetime
pessoa['Nome'] = str(input('Nome: ')).title()
nasc = int(input('Ano de Nascimento: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['Ctps'] = int(input('Carteira de Trabalho [0 = não tem] '))
if pessoa['Ctps'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = pessoa['Idade'] + pessoa['Contratação'] + 35 - datetime.now().year
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k}: {v}')