total = mais = menor = cont = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto R$ '))
    cont += 1
    total += preco
    if preco > 1000: mais += 1
    if cont == 1 or preco < menor:# usa o or quando existem dois blocos iguais para condicionais em Else.
        menor = preco
        barato = nome
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Gostaria de Continuar? [S/N] ').strip().upper()[0])
    if pergunta in 'N':
        break
print('{:^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto foi R$ {total:.2f}')
print(f'Existem {mais} produtos acima de R$ 1000.00')
print(f'O produto mais barato foi {barato} e o preço foi: R${menor}')