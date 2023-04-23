salario = float(input('Digite o salário: R$'))
aumento = salario * 1.1
if salario < 1250:
    aumento = salario * 1.15
print('Seu antigo salário era de R${:.2f}, então seu novo salário será de R${:.2f}.'.format(salario, aumento))
