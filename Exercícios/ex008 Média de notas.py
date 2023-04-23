print('Digite a nota do aluno no Primeiro, Segundo, Terceiro e Quarto bimestre.')
n1 = float(input('Primeiro Bimestre: '))
n2 = float(input('Segundo Bimestre: '))
n3 = float(input('Terceiro Bimestre: '))
n4 = float(input('Quarto Bimestre: '))
m = (n1 + n2 + n3 + n4) / 4
print('Sua média de notas é {:.1f}.'.format(m))
if m <= 6.9:
    print('Você está reprovado!')
else:
    print('Você está aprovado!')

#print('Você está aprovado!' if m >= 7 else ('Você está reprovado!'))