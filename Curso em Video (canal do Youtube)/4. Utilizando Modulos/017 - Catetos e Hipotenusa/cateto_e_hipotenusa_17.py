"""
Algoritmo que lê o comprimento do cateto oposto e adjacente de um
triângulo retângulo, calcula e exibe  o comprimento da hipotenusa.
"""

from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
comprimento_hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento da hipotenusa é {comprimento_hipotenusa:.2f}')
