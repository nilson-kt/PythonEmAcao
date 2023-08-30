"""
Programa que faz uma contagem regressiva de 10 a 0 e, no final,
apresenta uma mensagem que denota a explosão de fogos de artifício.
"""

from time import sleep
for numero in range(10, -1, -1):
    print(numero)
    sleep(1)
print('KABOOM!')
