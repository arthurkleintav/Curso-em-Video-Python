def leiaInt(msg):
    while True:
        try:
            val = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return val


def leiaFloat(msg):
    while True:
        try:
            val = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        else:
            return val

inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro}')
print(f'O valor real digitado foi {real}')
