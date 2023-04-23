def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}  ')
    print('-' * tam)
while True:
    mensagem = str(input('Mensagem: '))
    escreva(mensagem)
    while True:
        resp = str(input('Repetir? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('\033[31mERRO! Responda apenas com S ou N.')
    if resp == 'N':
        break
