"""
Programa que lê um número inteiro e mostra na tela
se ele é ou não um número primo.
"""

numero = int(input('Digite um número inteiro: '))
QUANTIDADE_DIVISORES = 0
for contador in range(1, numero+1):
    if numero % contador == 0:
        print(f'\033[1:33m{contador}\033[m', end=' ')
        QUANTIDADE_DIVISORES += 1
    else:
        print(f'\033[0:31m{contador}\033[m', end=' ')
print(f'\nO número {numero} tem {QUANTIDADE_DIVISORES} divisores.')
if QUANTIDADE_DIVISORES == 2:
    print('Ele é um número primo!')
else:
    print('Ele NÃO é um número primo!')
