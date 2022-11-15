def notas(*n, sit=False): 
    """função para cálculo de notas do aluno e verificar suas notas e sua situação caso solicitado.

    Args:
        sit (bool, optional): notas inseridas, podem ser várias notas. Defaults to False.

    Returns:
        _type_: Retorna dicionário com a lista de notas, nota máxima, nota miníma, média de notas e situação do aluno
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit == True: #or if sit: pois o espaço em branco já é considerado true
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5: #não preciso por o primeiro poramento de 7 pra baixo pois ja está implicito
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)