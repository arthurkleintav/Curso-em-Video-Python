maior = masc = m20 = 0
while True:
    print('\033[36m-='*10)
    print('CADASTRE UMA PESSOA.')
    print('-='*10, '\033[m')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar not in 'SN':
            print('\033[31mArgumento inválido! Tente novamente.\033[m')
    if continuar == 'N':
        break
print(f'\n\033[32mExistem {maior} pessoas maiores de idade.')
print(f'No total, {masc} Homens foram cadastrados.')
print(f'Foram cadastradas {m20} Mulheres com menos de 20 anos.\033[m')