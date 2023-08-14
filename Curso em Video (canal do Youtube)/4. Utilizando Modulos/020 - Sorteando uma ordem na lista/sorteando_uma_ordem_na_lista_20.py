"""
Programa que lê o nome de quatro alunos e exibe na tela, aleatoriamente, os nomes numa ordem.
"""

from random import shuffle

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
aleatorio = [aluno1, aluno2, aluno3, aluno4]
shuffle(aleatorio)
print(f'A ordem de apresentação será: {aleatorio}')
