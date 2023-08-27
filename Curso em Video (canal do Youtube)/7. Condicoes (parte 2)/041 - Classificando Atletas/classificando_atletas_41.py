"""
Programa que calcula a idade de uma pessoa baseada no nome e
exibe na tela a classificação em que a pessoa está na Confederação
Nacional de Natação (fictício).
"""

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento: '))
data_atual = str(date.today()).split('-', maxsplit=1)[0]
idade = int(data_atual) - ano_nascimento
CLASSIFICACAO = 'MIRIM'
if 14 > idade >= 9:
    CLASSIFICACAO = 'INFANTIL'
elif 19 > idade >= 9:
    CLASSIFICACAO = 'JÚNIOR'
elif 25 > idade >= 19:
    CLASSIFICACAO = 'SÊNIOR'
elif idade >= 25:
    CLASSIFICACAO = 'MASTER'
print(f"Você tem {idade} anos\nSua classificação é {CLASSIFICACAO}!")
