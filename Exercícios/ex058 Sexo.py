sex = str(input('Informe seu sexo: ')).strip()[0].upper()
while sex not in 'MmFf':
    sex = str(input('\033[31mDados inválidos. Tente novamente: \033[m')).strip()[0].upper()
print('\033[32mSexo {} registrado com sucesso!'.format(sex))
