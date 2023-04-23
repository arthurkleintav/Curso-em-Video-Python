def ficha(nome = 'desconhecido', gols = 0):
    print((f'O Jogador {nome} fez {gols} gols.'))

nom = str(input('Nome do jogador: ')).title().strip()
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nom.strip() == '':
    ficha(gols = gol)
else:
    ficha(nom, gol)

