dados = dict()
gols = list()
total = 0
cont = 0
dados['Nome'] = str(input('Nome do jogador: ')).title().strip()
quant = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(1, quant + 1):
    gols.append(int(input(f'{f"Quantos gols na partida {c}? ":>30}')))
    total += gols[cont]
    cont += 1
    dados['Gols'] = gols.copy()
    dados['Total'] = total
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {quant} partidas.')
for i, v in enumerate(gols):
    print(f'{f"=> Na partida {i + 1} fez {v} gols.":>30}')
print(f'Foi um total de {dados["Total"]} gols.')
