"""
Programa que lê a idade de 7 pessoas e exibe na tela a quantidade
de pessoas maiores de idade e de indivíduos que ainda não atingiram
a maioridade.
"""

from datetime import date

ano_atual = int(str(date.today()).split('-', maxsplit=1)[0])
QUANTIDADE_MAIOR = 0
QUANTIDADE_MENOR = 0
print(f'Ano atual: {ano_atual}')
for contador in range(1,  8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {contador}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        QUANTIDADE_MAIOR += 1
    else:
        QUANTIDADE_MENOR += 1
print(f'No total, {QUANTIDADE_MAIOR} são maiores de idade.')
print(f'{QUANTIDADE_MENOR} ainda não chegaram à maioridade.')
