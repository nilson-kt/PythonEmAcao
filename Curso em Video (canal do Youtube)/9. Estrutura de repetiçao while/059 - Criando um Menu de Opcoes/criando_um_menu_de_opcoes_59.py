"""
Programa que lê dois valores e mostra na tela um menu com opções, como
somar, multiplar, maior, novos número, sair do programa. O usuário poderá
interagir com o menu, escolhendo uma opção. Ao escolher uma opção, o
programa executará a função relacionada a ela.
"""

NUMERO_1 = int(input('Digite o primeiro valor: '))
NUMERO_2 = int(input('Digite o segundo valor: '))
OPCAO = '0'
while OPCAO != '5':
    print('='*30)
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    OPCAO = str(input('Digite uma opção: '))
    print('='*30)
    if OPCAO == '1':
        print(f'A soma entre {NUMERO_1} e {NUMERO_2} é igual a {NUMERO_1 + NUMERO_2}')
    elif OPCAO == '2':
        print(f'O produto entre {NUMERO_1} e {NUMERO_2} é igual a {NUMERO_1 * NUMERO_2}')
    elif OPCAO == '3':
        if NUMERO_1 != NUMERO_2:
            print('Acerca desses dois valores, o maior número é o', end=' ')
            if NUMERO_1 > NUMERO_2:
                print(NUMERO_1)
            elif NUMERO_2 > NUMERO_1:
                print(NUMERO_2)
        else:
            print('Esses números são iguais.')
    elif OPCAO == '4':
        NUMERO_1 = str(input('Digite o primeiro valor: '))
        NUMERO_2 = str(input('Digite o segundo valor: '))
        OPCAO = '0'
    elif OPCAO == '5':
        print('Até mais!')
    else:
        print('Opção inválida. Tente novamente.')
        OPCAO = '0'
