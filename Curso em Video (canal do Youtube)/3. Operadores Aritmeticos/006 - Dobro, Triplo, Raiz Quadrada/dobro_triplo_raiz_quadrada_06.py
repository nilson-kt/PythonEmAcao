"""
Programa que lê um número e exibe o dobro, triplo e a raiz quadrada dele.
"""

numero = int(input('Digite um número: '))
print(f'Dobro do número {numero}: {numero*2}')
print(f'Triplo de {numero}: {numero*3}')
print(f'Raiz quadrada de {numero}: {numero ** (1/2):.2f}')
