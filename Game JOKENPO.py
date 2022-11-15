from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
resposta = str(input('Vamos jogar jokenpô?(Sim / Não): ')).strip().upper()[0]
if resposta == 'S':
    print('Estou pensando na minha escolha...')
    computador = randint(0, 2)
    print('Suas opções: \n[ 0 ] PEDRA \n[ 1 ] PAPEL \n[ 2 ] TESOURA')
    jogador = int(input('Agora sim, Qual você escolhe?: '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ')
    sleep(1)
    print('=-' * 30)
    print('O Computador escolheu {}'.format(itens[computador]))
    print('O Jogador escolheu {}'.format(itens[jogador]))
    print('.=' * 30)
    if computador == 0:
       if jogador == 0:
        print('\033[33mEMPATE\033[m')
       elif jogador == 1:
        print('JOGADOR VENCE')
       elif jogador == 2:
        print('COMPUTADOR VENCE')
       else:
        print('\033[1;4;31mJOGADA INVALIDA\033[m')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('\033[33mEMPATE\033[m')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else:
            print('\033[1;4;31mJOGADA INVALIDA\033[m')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('\033[33mEMPATE\033[m')
        else:
            print('\033[1;4;31mJOGADA INVALIDA\033[m')
else:
    print('Tudo bem, até a próxima =D')