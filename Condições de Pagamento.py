preco = float(input('Digite o preço do produto: R$ '))
print('-_' * 30)
print('CONDIÇÕES:')
print('[1] À Vista dinheiro')
print('[2] À Vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão (com juros 20%)')
condicao = str(input('Digite qual será a condição escolhida: '))
if condicao == '1':
    print('O valor a ser pago será de R${:.2f}'.format(preco - preco * 0.10))
elif condicao == '2':
    print('O valor a ser pago será de R${:.2f}'.format(preco - preco * 0.05))
elif condicao == '3':
    print('O valor a ser pago será de R${:.2f} em 2 prestações'.format(preco / 2))
elif condicao == '4':
    vezes = int(input('Quantas vezes será parcelado: '))
    print('O valor a ser pago será de R$ {:.2f} em {} prestações'.format(((preco + (preco * 0.20)) / vezes), vezes))
else:
    print('Condição errada')
print('MUITO OBRIGADO')