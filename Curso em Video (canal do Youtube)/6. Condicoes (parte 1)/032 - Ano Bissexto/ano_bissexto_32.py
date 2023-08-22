"""
Programa que lê um ano e mostra na tela se
ele é um ano bissexto.
"""

ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 100 == 0 and ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto.')
