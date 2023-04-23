from time import sleep
print('\033[33m-=-'*5)
print('LOJA DO ARANHA')
print('-=-'*5)
sleep(0.5)
preço = float(input('\033[mPreço do produto: \033[32mR$\033[m'))
sleep(0.1)
print('\nEscolha uma opção:\n'
      '[1] À vista (dinheiro/cheque)\n'
      '[2] À vista no cartão\n'
      '[3] Em até 2x no cartão\n'
      '[4] 3x ou mais\n')
escolha = int(input('\033[33mDigite sua escolha: \033[m'))
if escolha == 1:
    print('\nO preço do produto será \033[32mR${:.2f}\033[m'.format(preço - (preço * 0.1)))
elif escolha == 2:
    print('\nO preço do produto será \033[32mR${:.2f}\033[m'.format(preço - (preço * 0.05)))
elif escolha == 3:
    print('\nO produto será parcelado 2x de \033[32mR${:.2f} \033[m'
          'SEM JUROS e custará \033[32mR${:.2f}\033[m'.format(preço / 2, preço))
elif escolha == 4:
    parcela = int(input('Em quantas vezes irá parcelar?: '))
    print('\nO produto será parcelado {}x de '
          '\033[32mR${:.2f}\033[m com 20% de JUROS e custará'
          ' \033[32mR${:.2f}\033[m'.format(parcela, preço / parcela, preço + (preço * 0.2)))
else:
    print('\n\033[31mArgumento inválido.\033[m')
