n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if 7 > media >= 5:
    print('Com a média {:.1f}, você está em \033[33mRECUPERAÇÃO.\033[m'.format(media))
elif media == 10:
    print('Sua média é 10. \033[32mPARABÉNS!\033[m')
elif media >= 7:
    print('Com a média {:.1f}, você está \033[32mAPROVADO.\033[m'.format(media))
elif media < 5:
    print('Com a média {:.1f}, você está \033[31mREPROVADO.\033[m'.format(media))