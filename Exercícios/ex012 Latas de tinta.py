l = (float(input('Largura da Parede: ')))
h = (float(input('Altura da Parede: ')))
a = l * h
(print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, h, a)))
print('Você precisará de {:.3f}l de tinta para pintar esta parede.'.format(a / 2))
