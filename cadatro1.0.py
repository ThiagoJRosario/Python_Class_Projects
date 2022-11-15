pessoa = {}
galera = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
média = soma / len(galera)
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print(f'A média de idade no cadastro é {média:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão com a idade acima da média: ',end='')
for p in galera:
    if p['idade'] >= média:
        print('    ',end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<<ENCERRADO>>>')