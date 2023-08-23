"""
Programa que lê um salário e mostra na tela o salário com
um aumento de 15% ou 10%.
"""

salario = float(input('Digite seu salário: R$'))
AUMENTO = "10%"
if salario > 1250.00:
    AUMENTO = "15%"
    salario = salario + salario*0.10
if salario <= 1250.00:
    salario = salario + salario*0.15
print(f'Seu salário teve um aumento de {AUMENTO}.\nSeu salário passa a ser R${salario:.2f}')
