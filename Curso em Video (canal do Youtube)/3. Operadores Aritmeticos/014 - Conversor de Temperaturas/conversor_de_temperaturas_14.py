"""
Programa que lê uma temperatura em graus Celsius e a exibe convertida em Fahrenheit.
"""

temperatura_em_c = float(input('Digite uma temperatura em graus Celsius: '))
temperatura_em_f = (temperatura_em_c * 9/5) + 32
print(f'A conversão de {temperatura_em_c:.1f}ºC em Fahrenheit fica {temperatura_em_f:.1f}ºF')
