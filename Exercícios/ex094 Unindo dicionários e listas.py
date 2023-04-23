pessoa = dict()
dados = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).title().strip()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('\033[31mERRO! Responda apenas com M ou F.\033[m')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    dados.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO! Responda apenas com S ou N.\033[m')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
media = soma / len(dados)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram', end = ' ')
for p in dados:
    if p['Sexo'] == 'F':
        print(p['Nome'], end = ' ')
print('\nD) Pessoas com idade acima da média:')
for p in dados:
    if p['Idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v};',end=' ')
        print()
print('<== VOLTE SEMPRE! ==>')
