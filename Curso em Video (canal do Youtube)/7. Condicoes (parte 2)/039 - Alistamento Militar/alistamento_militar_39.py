"""
Programa que lê o ano de nascimento de uma pessoa e exibe na tela
se a pessoa precisa ou não se alistar. O programa também mostra
o tempo que falta para se alistar, se já passou do prazo ou ou não,
de alistamento.
"""

from datetime import date
from math import fabs
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
data_atual = int(str(date.today()).split('-', maxsplit=1)[0])
idade = data_atual - ano_nascimento

if idade == 18:
    print(f'Você tem {idade} anos. Você precisa se alistar \033[1:33mimediatamente!')
elif idade > 18:
    print(f'Você tinha que se alistar quando tinha 18 anos. Você tem {idade}.', end=' ')
    print(f'Já passou da hora de se alistar! Passou do prazo faz {int(fabs(18 - idade))} ano(s)!')
    print(f'O ano em que você tinha que ter se alistado era {data_atual - (fabs(18-idade)):.0f}.')
else:
    print(f'Você só precisará se alistar quando tiver 18 anos. Você tem {idade}.', end=' ')
    print(f'Falta {18 - idade} ano(s) para chegar em {data_atual + (18 - idade)},', end=' ')
    print('o ano de seu alistamento.')
