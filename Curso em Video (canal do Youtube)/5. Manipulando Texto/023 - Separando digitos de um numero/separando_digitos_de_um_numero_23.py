"""
Programa que lê um número de 0 a 9999 e exibe na tela o
milhar, a centena, dezena e a unidade referente a esse número.
"""

NUMERO = str(input('Digite um número de 0 a 9999: '))
NUMERO = '-0-'.join('00' + NUMERO).split('-')
TAMANHO_STRING = len(NUMERO)
print(f'Unidade: {NUMERO[TAMANHO_STRING - 1]}')
print(f'Dezena: {NUMERO[TAMANHO_STRING - 3]}')
print(f'Centena: {NUMERO[TAMANHO_STRING - 5]}')
print(f'Milhar: {NUMERO[TAMANHO_STRING - 7]}')
