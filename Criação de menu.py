from criação_menu import Def1, Def2

arq = 'listamenu.txt'

if arquivoexiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criararquivo(arq)


while True:
    resposta = menu(['Mostrar lista', 'Cadastrar Usuário', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Digite o nome: '))
        idade = leiaint(f'Idade de {nome}: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[7mSaindo do sistema.....Até logo\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)