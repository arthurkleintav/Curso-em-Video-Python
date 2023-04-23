valor = float(input('Qual é o valor da casa? \033[32mR$\033[m'))
salario = float(input('Qual é seu salário? \033[32mR$\033[m'))
anos = int(input('Em quantos anos você irá pagar? '))
presta = valor / (anos * 12)
if presta > (salario * 0.3):
    print('Para comprar a casa, você teria que pagar R${:.2f}'
          ' por mês em {} anos. Isso passa de 30% de seu salário.'.format(presta, anos))
    print('\033[31mEMPRÉSTIMO NEGADO.\033[m'.format(presta))
elif presta < (salario * 0.3):
    print('\033[33mPara comprar a casa, você terá que pagar \033[32mR${:.2f}\033[m'
          '\033[33m por mês em {} anos. Isso é menor do que 30% de seu salário.\033[m'.format(presta, anos))
    print('\033[32mEMPRÉSTIMO ACEITO.\033[m')
