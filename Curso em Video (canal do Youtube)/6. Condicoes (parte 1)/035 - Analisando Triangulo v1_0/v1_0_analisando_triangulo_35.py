"""
Programa que lê três segmentos de reta e e exibe na tela
se, com eles, é possível formar um triângulo.
"""

from math import fabs

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if fabs(r2-r3) < r1 < (r2+r3) and fabs(r1-r3) < r2 < (r1+r3) and fabs(r1-r2) < r3 < (r1+r2):
    print('É POSSÍVEL formar um triângulo!')
else:
    print('NÃO é possível formar um triângulo!')
