"""
Algoritmo que faz a leitura de um ângulo e mostra na tela o valor do
seno, cosseno e da tangente.
"""

from math import sin, cos, tan, radians
angulo_em_grau = float(input('Digite um ângulo qualquer: '))
angulo_em_radiano = radians(angulo_em_grau)
seno, cosseno, tangente = sin(angulo_em_radiano), cos(angulo_em_radiano), tan(angulo_em_radiano)
print(f'O seno é {seno:.2f}')
print(f'O cosseno é {cosseno:.2f}')
print(f'A tangente é {tangente:.2f}')
