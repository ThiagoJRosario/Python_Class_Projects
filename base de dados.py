jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    tot = int(input(f'Digite quantos jogos o {jogador["nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols ele fez na {c+1}ª partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas) #função para somar todo dentro da lista.
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar: [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador: (999 para cancelar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe este código de jogador {busca}')
    else:
        print(f' -- LEVANTAMENTO  DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i} fez {g}')
    print('-=' * 30)
print('Volte Sempre')