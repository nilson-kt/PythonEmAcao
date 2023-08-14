"""
Programa que lê o nome de quatro alunos e exibe, na tela, o nome de um aluno de forma aleatória.
"""

from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
aleatorio = aluno1, aluno2, aluno3, aluno4
print(f'O aluno escolhido foi: {choice(aleatorio)}')
