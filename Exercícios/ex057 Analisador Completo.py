somai = 0
maior = 0
hnome = ''
muie = 0
for c in range(1, 5):
    print('---- {}ª Pessoa: ----'.format(c))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somai += idade
    if c == 1:
        maior = idade
        hnome = nome
    else:
        if idade > maior and sexo in 'Mm':
            maior = idade
    if sexo in 'Ff' and idade < 20:
        muie += 1
print('A média de idade das pessoas é {}.'.format(somai / 4))
print('O nome do homem mais velho é {} e ele tem {} anos.'.format(hnome, maior))
print('Ao todo, existem {} mulheres com menos de 20 anos.'.format(muie))
