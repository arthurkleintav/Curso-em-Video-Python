def leiaInt(msg):
    while True:
        try:
            val = int(input(msg))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except:
            print('\033[31mERRO! Por favor, digite uma opção válida.\033[m')
            continue
        else:
            return val

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def cabecalho2(txt):
    print(linha())
    print(txt.center(42))
    print(linha(),end='')

def menu(lista):
    from time import sleep
    cont = 1
    cabecalho('MENU PRINCIPAL')
    for item in lista:
        sleep(0.5)
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
        cont += 1
    print(linha(42))
    opt = leiaInt('\033[33mSua opção: \033[m')
    return opt

