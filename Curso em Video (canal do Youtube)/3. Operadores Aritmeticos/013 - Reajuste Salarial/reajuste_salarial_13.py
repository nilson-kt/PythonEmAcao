"""
Algoritmo que lê o salário de uma pessoa e exibe esse salário com um aumento de 15%.
"""

salario = float(input('Digite o seu salário: R$'))
aumento = salario * 0.15
print(f'Seu salário, com 15% de aumento, fica {salario + aumento:.2f}')
