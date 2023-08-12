"""
Programa que lê um número na tela e exibe sua parte inteira.
"""

from math import  trunc
numero = float(input('Digite um número: '))
print(f'A parte inteira de {numero} é {trunc(numero)}')
