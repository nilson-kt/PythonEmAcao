"""
Programa que lê um número de 0 a 9999 e exibe na tela o
milhar, a centena, dezena e a unidade referente a esse número.
"""

from math import floor

numero = int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {numero-(floor(numero/10)*10)}')
print(f'Dezena: {floor((numero-(floor(numero/100)*100))/10)}')
print(f'Centena: {floor((numero-floor(numero/1000)*1000)/100)}')
print(f'Milhar: {floor(numero/1000)}')
