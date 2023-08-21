"""
Programa que lê o nome completo de uma pessoa e exibe na tela
o seu primeiro e último nome.
"""

nome = input('Digite seu nome completo: ').strip().split(' ')
print(f'Primeiro nome: {nome[0]}\n'
      f'Último nome: {nome[-1]} ')
