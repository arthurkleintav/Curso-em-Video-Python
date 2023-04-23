n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('\033[36mO primeiro valor é maior.\033[m')
elif n2 > n1:
    print('\033[35mO segundo valor é maior.\033[m')
elif n1 == n2:
    print('\033[34mOs dois valores são iguais.\033[m')
