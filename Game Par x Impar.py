from random import randint
from time import sleep
print('=-='* 20)
print('Vamos jogar PAR ou IMPAR')
print('=-='* 20)
quant = 0
while True:
    computador = randint(0, 11)
    jogador = int(input('Digite um número: '))
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo  = str(input('Você quer PAR ou IMPAR? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total é {soma}', end='')
    print(' DEU PAR' if soma % 2 == 0 else ' DEU IMPAR')
    sleep(1)
    if tipo == 'P':
        if soma % 2 == 0:
            print('Voce Ganhou!!!')
            quant += 1
        else:
            print('Voce Perdeu!!!')
            break
    if tipo == 'I':
        if soma % 2 == 1:
            print('Voce Venceu!!!')
            quant += 1
        else:
            print('Voce Perdeu!!!')
            break
    print('Vamos Jogar novamemente...')
print(f'Você jogou e ganhou {quant} vezes antes de perder.')