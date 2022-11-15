def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def triplo(preço=0, formato=False):
    res = preço * 3
    return res if formato is False else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)  # type: ignore


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)  # type: ignore


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)  # type: ignore


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxad=15):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumento de preços: \t{aumentar(preço, 10, True)}')
    print(f'Diminuição do preço: \t{diminuir(preço, 15, True)}')
    print('-' * 30)